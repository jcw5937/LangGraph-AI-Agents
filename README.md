# AI Agent Progression

# Part 1: ReAct Agent from Scratch

A simple AI agent built from scratch in Python, following the **ReAct (Reasoning + Acting)** pattern introduced in the paper [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2303.17651).

This is Part 1 of an ongoing project built while following the [DeepLearning.AI AI Agents in LangGraph](https://learn.deeplearning.ai) course.

---

## What It Does

The agent answers questions by reasoning through them step by step rather than responding immediately. Each turn follows a structured loop:

1. **Thought** — the agent reasons about what it needs to do
2. **Action** — it calls one of its available tools
3. **PAUSE** — it waits for the result
4. **Observation** — the tool result is fed back in
5. **Answer** — once it has enough information, it responds

Conversation history is maintained across turns, so the agent always has full context when deciding what to do next.

## Key Takeaways

**What is the ReAct pattern, and why does it outperform single-shot prompting on multi-step tasks?**

ReAct stands for Reasoning and Acting. Instead of answering in one shot, the agent loops through Thought, Action, PAUSE, and Observation steps repeatedly until it reaches a final answer. This outperforms single-shot prompting on multi-step tasks because the model can pause after each tool call, incorporate the result, and decide what to do next based on new information rather than having to guess everything upfront.

**How is conversation history structured and passed to the model?**

Conversation history is passed as a list of dictionaries, where each dictionary has a `role` and `content` field. The role is either `system`, `user`, or `assistant`. The system message sets the agent's behavior upfront. User messages contain either the human's input or observations fed back in from tool calls. Assistant messages contain the model's responses. The full list is passed to the model on every call so it has complete context.

**Why does constraining tools improve agent reliability?**

Giving an agent a smaller, well-defined set of tools makes its behavior more predictable and easier to test. If the agent has unlimited tools or vague tool definitions, it's harder to anticipate what it will do and harder to catch errors. Constrained tools also make it easier to write evals, because you can test whether the agent is choosing the right tool for a given input.

**How do system prompts shape agent behavior and tool usage?**

The system message is the first thing in the conversation history and sets the rules for everything that follows. It tells the model what persona to adopt, what tools are available and how to use them, and what format to respond in. In this ReAct agent, the system prompt teaches the model the Thought/Action/PAUSE/Observation format and defines the exact syntax for calling each tool — without it the model would respond conversationally with no structure.

---

## Tools

The agent currently has access to two intentionally simple tools:

- `calculate` — evaluates a math expression
- `average_dog_weight` — returns the average weight of a dog breed

Keeping the tool set small was a deliberate choice for this first version — the goal was to understand the agent loop clearly before adding complexity. Future parts of this project will expand the tool set and add logging and evals.

---

## Tech Stack

- Python 3.14
- OpenAI SDK
- Docker dev container (via VS Code Dev Containers)

---

## Getting Started

### Prerequisites
- [VS Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- An OpenAI API key

### Setup

1. Clone the repo
```bash
   git clone https://github.com/yourusername/AI-Agent-Basics.git
   cd AI-Agent-Basics
```

2. Open in VS Code and reopen in container when prompted

3. Create a `.env` file in the project root:
