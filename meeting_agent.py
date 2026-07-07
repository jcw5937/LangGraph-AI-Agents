"""Meeting notes agent, extracted from Meeting-Notes-Agent.ipynb into an importable module.

The model is never constructed here -- callers pass in a chat model instance (ChatAnthropic,
ChatOpenAI, or anything with the same .invoke interface), which is what lets run_agent be used
to compare providers.
"""

from functools import partial
from typing import TypedDict, List

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver


class MeetingState(TypedDict):
    transcript: str
    action_items: str
    decisions: str
    open_questions: str
    reasoning_log: List[str]


def parse_response(content) -> tuple[str, str]:
    """Split a REASONING/ANSWER formatted model response into its two parts."""
    text = content if isinstance(content, str) else str(content)
    if "ANSWER:" in text:
        reasoning_part, answer_part = text.split("ANSWER:", 1)
        reasoning = reasoning_part.replace("REASONING:", "", 1).strip()
        answer = answer_part.strip()
    else:
        # Model didn't follow the format -- treat the whole thing as the answer.
        reasoning = "(no reasoning section returned)"
        answer = text.strip()
    return reasoning, answer


ACTION_ITEMS_PROMPT = """You are analyzing a meeting transcript to extract action items.

Think step by step through the transcript and identify every commitment, task, or follow-up
that someone agreed to do. Note who owns each item if a name is attached. Show your reasoning
first, then give the final answer.

Respond in exactly this format:
REASONING:
<your step-by-step reasoning>

ANSWER:
<bulleted list, one per line, in the form "- <task> (Owner: <name or "unspecified">)">

Transcript:
{transcript}
"""

DECISIONS_PROMPT = """You are analyzing a meeting transcript to extract decisions that were made.

Think step by step through the transcript and identify every explicit decision or agreement the
group reached -- something that was proposed and confirmed, not just discussed. Show your
reasoning first, then give the final answer.

Respond in exactly this format:
REASONING:
<your step-by-step reasoning>

ANSWER:
<bulleted list of decisions actually made, one per line>

Transcript:
{transcript}
"""

OPEN_QUESTIONS_PROMPT = """You are analyzing a meeting transcript to extract open questions.

Think step by step through the transcript and identify every question, unresolved issue, or
item the group explicitly deferred or flagged for follow-up -- things that were raised but not
answered or decided. Show your reasoning first, then give the final answer.

Respond in exactly this format:
REASONING:
<your step-by-step reasoning>

ANSWER:
<bulleted list of open questions, one per line>

Transcript:
{transcript}
"""


def ingest(state: MeetingState) -> MeetingState:
    """Normalize the raw transcript and reset the reasoning log."""
    cleaned = state["transcript"].strip()
    return {"transcript": cleaned, "reasoning_log": []}


def extract_action_items(state: MeetingState, model) -> MeetingState:
    prompt = ACTION_ITEMS_PROMPT.format(transcript=state["transcript"])
    response = model.invoke([HumanMessage(content=prompt)])
    reasoning, answer = parse_response(response.content)

    return {
        "action_items": answer,
        "reasoning_log": state["reasoning_log"] + [f"[action_items] {reasoning}"],
    }


def extract_decisions(state: MeetingState, model) -> MeetingState:
    prompt = DECISIONS_PROMPT.format(transcript=state["transcript"])
    response = model.invoke([HumanMessage(content=prompt)])
    reasoning, answer = parse_response(response.content)

    return {
        "decisions": answer,
        "reasoning_log": state["reasoning_log"] + [f"[decisions] {reasoning}"],
    }


def extract_open_questions(state: MeetingState, model) -> MeetingState:
    prompt = OPEN_QUESTIONS_PROMPT.format(transcript=state["transcript"])
    response = model.invoke([HumanMessage(content=prompt)])
    reasoning, answer = parse_response(response.content)

    return {
        "open_questions": answer,
        "reasoning_log": state["reasoning_log"] + [f"[open_questions] {reasoning}"],
    }


def synthesize(state: MeetingState) -> MeetingState:
    """Combine the three extracted sections into one structured report."""
    report = f"""MEETING SUMMARY
================

ACTION ITEMS
------------
{state['action_items']}

DECISIONS MADE
--------------
{state['decisions']}

OPEN QUESTIONS
--------------
{state['open_questions']}
"""
    return {
        "reasoning_log": state["reasoning_log"] + [f"[synthesize] {report}"]
    }


def build_graph(model):
    """Wire the 5 nodes into a sequential StateGraph bound to the given model."""
    builder = StateGraph(MeetingState)

    builder.add_node("ingest", ingest)
    builder.add_node("extract_action_items", partial(extract_action_items, model=model))
    builder.add_node("extract_decisions", partial(extract_decisions, model=model))
    builder.add_node("extract_open_questions", partial(extract_open_questions, model=model))
    builder.add_node("synthesize", synthesize)

    builder.add_edge(START, "ingest")
    builder.add_edge("ingest", "extract_action_items")
    builder.add_edge("extract_action_items", "extract_decisions")
    builder.add_edge("extract_decisions", "extract_open_questions")
    builder.add_edge("extract_open_questions", "synthesize")
    builder.add_edge("synthesize", END)

    return builder


def run_agent(transcript: str, model) -> dict:
    """Run the full meeting-notes pipeline against `transcript` using `model`.

    Uses an in-memory SqliteSaver for checkpointing -- fresh per call, so concurrent or
    repeated calls (e.g. batch evaluation across transcripts and providers) never share state.
    """
    builder = build_graph(model)

    with SqliteSaver.from_conn_string(":memory:") as checkpointer:
        app = builder.compile(checkpointer=checkpointer)

        config = {"configurable": {"thread_id": "meeting-notes-agent"}}
        initial_state: MeetingState = {
            "transcript": transcript,
            "action_items": "",
            "decisions": "",
            "open_questions": "",
            "reasoning_log": [],
        }

        result = app.invoke(initial_state, config=config)

    return result
