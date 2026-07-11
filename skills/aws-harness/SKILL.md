---
name: aws-harness
description: Build a new AI agent on AWS and deploy it easily, OR wrap and deploy an agent you already have, using the Amazon Bedrock AgentCore harness. Explains what an "agent harness" is (the runtime scaffolding around a model - agent loop, tool execution, memory, identity, observability), then gives two fully-working, verified paths - (A) scaffold + ship a new agent with the AgentCore CLI (create/dev/deploy/invoke), and (B) deploy a prepared agent (Strands, LangGraph, or custom) via the SDK wrapper or a FastAPI + Docker + ECR container. Every import and command is verified against official AWS/Strands docs. Use when the goal is to create, wrap, or deploy an agent on AWS AgentCore. Triggers on agent harness, AWS harness, AgentCore, AgentCore CLI, agentcore create, agentcore deploy, deploy agent on AWS, bring your own agent, Bedrock AgentCore runtime, serverless agent.
---

# AWS Agent Harness (Bedrock AgentCore)

Take an AI agent from an empty folder - or from code you already have - to a live, serverless endpoint on AWS. Every command and import below is verified against official docs (sources at the bottom).

> Companion skill: [aws-strands](../aws-strands/SKILL.md) is the agent framework (the "brain" - how to write the agent). **This** skill is the harness: how to run and deploy that agent on AWS. Write with Strands, ship with AgentCore.

## What "harness" means (read this first)

A language model, alone, only turns text into text. It cannot call an API, remember yesterday, run code, or browse the web. The **harness** is the scaffolding around the model that makes it act:

- **Agent loop** - call the model, read the tool it wants, run that tool, feed the result back, repeat until done. The model *decides*; the harness *executes and loops*.
- **Tool execution, memory, identity, guardrails, sandboxing, observability** - everything that makes it useful and production-safe.

**Amazon Bedrock AgentCore** is AWS's managed set of these harness pieces. You bring the agent (built with [Strands](../aws-strands/SKILL.md), LangGraph, or anything); AgentCore hosts, secures, and scales it. The components, composable and framework-agnostic:

| Component | What it gives you |
|---|---|
| **Runtime** | Serverless, isolated agent execution (any framework, any model) |
| **Memory** | Short-term (session) + long-term (cross-session) memory |
| **Identity** | Let the agent act on behalf of a user (Cognito, Okta, Google, EntraID, OAuth) |
| **Gateway** | Turn APIs / Lambda functions into agent tools (MCP) |
| **Code Interpreter** | Sandboxed code execution |
| **Browser** | Managed headless browser for web tasks |
| **Observability** | Tracing, logs, metrics (CloudWatch / OpenTelemetry) |

You adopt these one at a time via `agentcore add` (Path A) or the SDK/API (Path B) - not all-or-nothing.

## Which path are you on?

| | You want to... | Go to |
|---|---|---|
| **Path A** | Build a NEW agent from scratch, easiest possible | [Path A](#path-a---build-and-deploy-a-new-agent-cli) - the AgentCore CLI |
| **Path B** | Deploy an agent you ALREADY have (Strands / LangGraph / anything) | [Path B](#path-b---deploy-an-agent-you-already-have) - wrap + ship |

## Prerequisites

**Both paths need:**

| Requirement | Why |
|---|---|
| AWS account + `aws configure` credentials | Everything below provisions real, billable infrastructure in *your* account. |
| Bedrock model access | Enable a Claude model (for example Claude Sonnet 4) in the Bedrock console, in your target region, before the agent can call it. |
| Python 3.10+ | The agent code is Python. |

**Path A also needs:** Node.js 20+ (the CLI is an npm package) and AWS CDK (`npm i -g aws-cdk`, then `cdk bootstrap` once per account/region - the CLI deploys via CDK).

**Path B (container option) also needs:** Docker with `buildx` (for ARM64 images).

---

## Path A - Build and deploy a new agent (CLI)

The AgentCore CLI scaffolds a working agent, runs it locally, and deploys it.

> Two CLIs exist. Use the **new** one: `@aws/agentcore` (npm), commands `create`/`dev`/`deploy`/`invoke`. The older `bedrock-agentcore-starter-toolkit` (pip) uses `configure`/`launch` and is marked legacy - it is handy for Path B (wrapping an existing file), shown later.

### 1. Install

```bash
npm install -g @aws/agentcore
agentcore --help
```

### 2. Create the project

```bash
# interactive wizard:
agentcore create

# or non-interactive:
agentcore create --name MyAgent --framework Strands --model-provider Bedrock --memory none

# or accept all defaults (Python, Strands, Bedrock, no memory):
agentcore create --name MyAgent --defaults
```

Each flag shapes the agent:

| Flag | Verified options | Meaning |
|---|---|---|
| `--framework` | `Strands`, `LangChain_LangGraph`, `GoogleADK`, `OpenAIAgents` | The brain. Strands is AWS-native and simplest. |
| `--model-provider` | `Bedrock`, `Anthropic`, `OpenAI`, `Gemini` | Bedrock = Claude inside AWS (no external key). Others call out with an API key. |
| `--memory` | `none`, `shortTerm`, `longAndShortTerm` | none = amnesiac; shortTerm = within a session; longAndShortTerm = across sessions. |
| `--protocol` | `HTTP`, `MCP`, `A2A` | HTTP for normal request/response; MCP to expose the agent as tools; A2A for agent-to-agent. |
| `--build` | `CodeZip`, `Container` | CodeZip = zip to S3, no Docker. Container = Docker image, for custom system deps. |

It generates:

```
MyAgent/
  agentcore/
    agentcore.json      # project + agent config
    aws-targets.json    # AWS account / region
    .env.local          # local secrets (gitignored)
  app/
    MyAgent/
      main.py           # your starter agent, in the chosen framework
      pyproject.toml
  README.md
```

### 3. The agent code (this is all an AgentCore agent is)

The scaffolded `main.py` follows this verified minimal shape - a framework agent wrapped by the harness:

```python
from bedrock_agentcore import BedrockAgentCoreApp   # the harness wrapper
from strands import Agent                           # the framework (brain)

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint                       # every request lands here
def invoke(payload):
    user_message = payload.get("prompt", "Hello! How can I help you today?")
    result = agent(user_message)      # this one call IS the entire agent loop
    return {"result": result.message}

if __name__ == "__main__":
    app.run()                         # `agentcore dev` runs exactly this
```

To give the agent a real capability, add a tool. The `@tool` decorator turns a function into something the model can call, and **the docstring is read by the model** to decide when to call it and what to pass (Strands parses the first paragraph as the description and the `Args:` section as parameter docs):

```python
from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent, tool

app = BedrockAgentCoreApp()

@tool
def word_count(text: str) -> str:
    """Count the number of words in a piece of text.

    Args:
        text: The text to count words in.
    """
    return f"The text has {len(text.split())} words."

agent = Agent(tools=[word_count])     # add/remove tools here = change abilities

@app.entrypoint
def invoke(payload):
    user_message = payload.get("prompt", "Hello!")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
```

Design note: a tool's return value is read by the model. Return recoverable strings on failure (`"Error: no city 'X'. Ask the user to rephrase."`) rather than raising an unhandled exception, which crashes the turn. Prebuilt tools are available too: `pip install strands-agents-tools`, then `from strands_tools import calculator` and pass it in `Agent(tools=[calculator])`.

### 4. Test locally (free) before deploying

```bash
cd MyAgent
agentcore dev                         # hot-reload server on localhost:8080 + browser inspector
agentcore dev "count the words here"  # invoke the local agent
```

### 5. Deploy to AWS

```bash
agentcore deploy --plan   # dry run: preview the infra
agentcore deploy          # provision for real
```

Under the hood this reads `agentcore.json`, packages `app/` (CodeZip or Docker) built for **ARM64/Graviton** (required by the runtime; the CLI handles the arch), uses **CDK to synthesize CloudFormation** provisioning the Runtime + an **IAM execution role** + S3 staging, and returns an **Agent ARN**.

### 6. Invoke

```bash
agentcore invoke "Tell me a joke" --stream
agentcore invoke --session-id my-session "and another"   # continuity across calls
```

From application code (verified verbatim pattern):

```python
import json, uuid, boto3

client = boto3.client("bedrock-agentcore")
response = client.invoke_agent_runtime(
    agentRuntimeArn="<AGENT_ARN>",         # from `agentcore status`
    runtimeSessionId=str(uuid.uuid4()),    # must be 33+ chars; uuid4 is 36
    payload=json.dumps({"prompt": "Tell me a joke"}).encode(),
    qualifier="DEFAULT",
)
content = []
for chunk in response.get("response", []):
    content.append(chunk.decode("utf-8"))
print(json.loads("".join(content)))
```

### 7. Add production harness components

Snap pieces in with `agentcore add`, then re-deploy (run `agentcore add --help` for the full list):

```bash
agentcore add memory --name MyMemory --strategies SEMANTIC       # long-term recall
agentcore add agent  --name SecondAgent --framework Strands       # multi-agent
# also available: identity, target (gateway), evaluator
agentcore deploy                                                  # provision the additions
```

Observability is built in:

```bash
agentcore logs           # stream runtime logs
agentcore traces list    # inspect steps, tokens, latency
```

### 8. Clean up (do NOT skip - this costs money)

```bash
agentcore remove all   # mark resources for deletion
agentcore deploy       # apply teardown via CloudFormation
```

---

## Path B - Deploy an agent you already have

You already wrote an agent (Strands, LangGraph, OpenAI Agents, or plain Python). Two ways to ship it.

### Option B1 - Wrap it with the SDK (fewest lines)

AgentCore Runtime just needs your agent behind an entrypoint. Wrap your existing agent object:

```python
# main.py - the only new file you write
from bedrock_agentcore import BedrockAgentCoreApp
from my_agent import agent          # <-- your already-built agent (any framework)

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    result = agent(payload.get("prompt", ""))
    return {"result": result.message if hasattr(result, "message") else str(result)}

if __name__ == "__main__":
    app.run()
```

```bash
pip install bedrock-agentcore
```

Then deploy it. Easiest: `agentcore create` a project (Path A) and paste your logic into the generated entrypoint - you reuse all of Path A's deploy/invoke tooling. Alternatively, the legacy starter toolkit points straight at an existing file:

```bash
pip install bedrock-agentcore-starter-toolkit
agentcore configure --entrypoint main.py    # generates IAM role, ECR repo, Dockerfile
agentcore launch                             # build + deploy
agentcore invoke '{"prompt": "hello"}'       # note: JSON string argument
```

### Option B2 - Full container control (no SDK, no CLI)

For maximum control, meet the runtime contract yourself: an HTTP server exposing **`/invocations` (POST)** and **`/ping` (GET)** on **port 8080**, packaged as an **ARM64** Docker image. This is the verified official path.

**1. Project setup (uv):**

```bash
mkdir my-custom-agent && cd my-custom-agent
uv init --python 3.11
uv add fastapi 'uvicorn[standard]' pydantic httpx strands-agents
```

**2. `agent.py` (FastAPI meeting the runtime contract):**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime
from strands import Agent

app = FastAPI(title="Strands Agent Server", version="1.0.0")
strands_agent = Agent()   # replace with your prepared agent

class InvocationRequest(BaseModel):
    input: Dict[str, Any]

class InvocationResponse(BaseModel):
    output: Dict[str, Any]

@app.post("/invocations", response_model=InvocationResponse)
async def invoke_agent(request: InvocationRequest):
    user_message = request.input.get("prompt", "")
    if not user_message:
        raise HTTPException(status_code=400, detail="No 'prompt' in input.")
    result = strands_agent(user_message)
    return InvocationResponse(output={
        "message": result.message,
        "timestamp": datetime.utcnow().isoformat(),
    })

@app.get("/ping")
async def ping():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
```

**3. `Dockerfile` (ARM64 - required):**

```dockerfile
FROM --platform=linux/arm64 ghcr.io/astral-sh/uv:python3.11-bookworm-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache
COPY agent.py ./
EXPOSE 8080
CMD ["uv", "run", "uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]
```

**4. Build for ARM64, push to ECR:**

```bash
docker buildx create --use
aws ecr create-repository --repository-name my-strands-agent --region us-west-2
aws ecr get-login-password --region us-west-2 \
  | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-west-2.amazonaws.com
docker buildx build --platform linux/arm64 \
  -t <account-id>.dkr.ecr.us-west-2.amazonaws.com/my-strands-agent:latest --push .
```

**5. Create the runtime (boto3, `bedrock-agentcore-control`):**

```python
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")
response = client.create_agent_runtime(
    agentRuntimeName="strands_agent",
    agentRuntimeArtifact={"containerConfiguration": {
        "containerUri": "<account-id>.dkr.ecr.us-west-2.amazonaws.com/my-strands-agent:latest"
    }},
    networkConfiguration={"networkMode": "PUBLIC"},
    roleArn="arn:aws:iam::<account-id>:role/AgentRuntimeRole",
)
print(response["agentRuntimeArn"], response["status"])
```

**6. Invoke (note the `input` wrapper matches the FastAPI contract):**

```python
import boto3, json

client = boto3.client("bedrock-agentcore", region_name="us-west-2")
response = client.invoke_agent_runtime(
    agentRuntimeArn="<AGENT_RUNTIME_ARN>",
    runtimeSessionId="a" * 40,   # must be 33+ chars
    payload=json.dumps({"input": {"prompt": "Explain machine learning simply"}}),
    qualifier="DEFAULT",
)
print(json.loads(response["response"].read()))
```

**7. Stop the session to avoid runaway cost:**

```python
import boto3
boto3.client("bedrock-agentcore", region_name="us-west-2").stop_runtime_session(
    agentRuntimeArn="<AGENT_RUNTIME_ARN>",
    runtimeSessionId="a" * 40,
    qualifier="DEFAULT",
)
```

Runtime contract summary: platform `linux/arm64`, endpoints `/invocations` POST + `/ping` GET, port 8080, image in ECR, and Strands agents need AWS credentials at runtime.

---

## Gotchas (all verified)

- **Wrong CLI**: `agentcore configure`/`launch` = legacy pip toolkit; the new npm CLI uses `create`/`deploy`. Don't mix their command names.
- **CDK not bootstrapped**: Path A `agentcore deploy` fails until you run `cdk bootstrap` once per account/region.
- **Model access denied**: enable the Claude model in the Bedrock console, in the *same region* as your deploy.
- **Payload shape mismatch**: an SDK/`BedrockAgentCoreApp` entrypoint reads `payload.get("prompt")` so you send `{"prompt": ...}`; the custom FastAPI contract reads `request.input.get("prompt")` so you send `{"input": {"prompt": ...}}`. Match them.
- **`runtimeSessionId` too short**: it must be 33+ characters (`str(uuid.uuid4())` is 36).
- **Not ARM64**: containers must be `linux/arm64` or the runtime rejects them.
- **`result.message` is a dict** (`{"role": ..., "content": [{"text": ...}]}`), not a plain string. Use `result.message` for JSON responses, or `str(result)` / `result.message["content"][0]["text"]` for plain text.
- **Cost**: deployed runtimes bill until torn down. Path A: `agentcore remove all && agentcore deploy`. Path B: `stop_runtime_session`, then delete the runtime and ECR repo.

## Resources

- AgentCore CLI (new): https://github.com/aws/agentcore-cli
- Get started with the AgentCore CLI: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-cli.html
- Deploy without the CLI (custom/BYO agent): https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-custom.html
- Bedrock AgentCore Python SDK: https://github.com/aws/bedrock-agentcore-sdk-python
- Strands custom tools (`@tool`): https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/
- Official samples: https://github.com/awslabs/amazon-bedrock-agentcore-samples
