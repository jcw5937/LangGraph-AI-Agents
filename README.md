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
