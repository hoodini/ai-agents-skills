---
name: aws-strands
description: Build AI agents with the Strands Agents SDK - the open-source framework (the agent "brain") for writing agent logic, tools, and multi-agent systems in Python. Model-agnostic, AWS Bedrock by default. Covers Agent, the @tool decorator, model providers (BedrockModel), multi-agent patterns (agents-as-tools, Swarm, Graph), conversation management, and streaming. Every import verified against official Strands docs. To DEPLOY a Strands agent on AWS, use the aws-harness skill. Triggers on Strands, Strands Agents, Strands SDK, agent framework, agents as tools, Swarm, Graph multi-agent, BedrockModel.
---

# Strands Agents SDK

The open-source framework you write an agent's logic in - the "brain." Model-agnostic, AWS Bedrock by default. Runs anywhere (laptop, container, Lambda, EC2).

> **How this fits with the other AWS skill:** Strands is the FRAMEWORK (what your agent does). To HOST and DEPLOY a Strands agent on AWS, use [aws-harness](../aws-harness/SKILL.md) (the AgentCore runtime). They compose: write with Strands, ship with AgentCore. You can also run Strands with no AWS deployment at all.

## Install

```bash
pip install strands-agents strands-agents-tools
```

(A TypeScript SDK also exists - see the docs. Examples below are Python.)

## Quick Start

```python
from strands import Agent

agent = Agent()                       # defaults to Bedrock, Claude 4 Sonnet
print(agent("What is the capital of France?"))
```

`agent(...)` returns an `AgentResult`. `str(result)` gives the text; `result.message` is the structured dict (`role` + `content`).

## Model configuration

Bedrock is the default provider and no model argument is needed - Strands picks a region-appropriate Claude 4 Sonnet. To override, pass a model id string or a `BedrockModel` provider:

```python
from strands import Agent
from strands.models import BedrockModel

# Simple: a Bedrock model id (copy the exact id from the Bedrock model catalog)
agent = Agent(model="<your-bedrock-model-id>")

# Full control:
agent = Agent(model=BedrockModel(
    model_id="<your-bedrock-model-id>",
    temperature=0.3,
    region_name="us-west-2",
))
```

Strands is model-agnostic - other providers (Anthropic direct, OpenAI, etc.) are available via their own provider classes; see the model-providers docs.

## Custom tools

The `@tool` decorator turns a function into something the model can call. The **docstring is read by the model** (first paragraph = description, `Args:` = parameter docs):

```python
from strands import Agent, tool

@tool
def word_count(text: str) -> str:
    """Count the number of words in a piece of text.

    Args:
        text: The text to analyze.
    """
    return f"{len(text.split())} words"

agent = Agent(tools=[word_count])
```

Return recoverable strings on failure (`"Error: ... ask the user to rephrase"`) instead of raising - the model reads the return value and can recover.

## Prebuilt tools

```python
from strands_tools import calculator   # from the strands-agents-tools package
agent = Agent(tools=[calculator])
```

## Multi-agent patterns

Three verified patterns. Start with **agents-as-tools** (simplest delegation): wrap an agent in a `@tool`.

```python
from strands import Agent, tool

researcher = Agent(system_prompt="You research topics thoroughly.")

@tool
def research(query: str) -> str:
    """Delegate a research question to the research specialist."""
    return str(researcher(query))     # str(AgentResult) = the text output

coordinator = Agent(tools=[research])
coordinator("Research the history of espresso and summarize it.")
```

For structured orchestration, use `Swarm` (agents hand off to each other dynamically) or `Graph` (a deterministic DAG where one node's output feeds the next):

```python
from strands.multiagent import Swarm, GraphBuilder

# Swarm - dynamic handoffs
swarm = Swarm([researcher, writer, editor])
swarm("Draft and polish an article about espresso.")

# Graph - deterministic pipeline
builder = GraphBuilder()
builder.add_node(researcher, "research")
builder.add_node(writer, "write")
builder.add_edge("research", "write")     # research output -> writer input
graph = builder.build()
graph("Write an article about espresso.")
```

See the multi-agent docs for the full Graph/Swarm API.

## Conversation management (context window)

Strands manages the conversation window for you (this is NOT long-term memory). The default is a sliding window:

```python
from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager

agent = Agent(conversation_manager=SlidingWindowConversationManager(window_size=20))
```

For durable, cross-session memory, use AgentCore Memory (see [aws-harness](../aws-harness/SKILL.md)) or the memory tools in `strands-agents-tools`.

## Streaming

```python
async for event in agent.stream_async("Explain quantum computing"):
    print(event)
```

## Deploy on AWS

Strands runs anywhere. To put a Strands agent on AWS as a serverless endpoint with managed memory, identity, and observability, use the AgentCore harness: **[aws-harness](../aws-harness/SKILL.md)**.

## Resources

- Strands docs: https://strandsagents.com/
- Python quickstart: https://strandsagents.com/docs/user-guide/quickstart/python/
- Multi-agent patterns: https://strandsagents.com/docs/user-guide/concepts/multi-agent/multi-agent-patterns/
- Model providers: https://strandsagents.com/docs/user-guide/concepts/model-providers/
- GitHub: https://github.com/strands-agents/sdk-python
