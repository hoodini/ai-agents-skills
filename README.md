<p align="center">
  <img src="https://img.shields.io/badge/AI-Agent%20Skills-blueviolet?style=for-the-badge&logo=robot&logoColor=white" alt="AI Agent Skills"/>
  <img src="https://img.shields.io/badge/GitHub-Star-yellow?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Star"/>
  <img src="https://img.shields.io/badge/AWS-GenAI%20Superstar-orange?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS GenAI Superstar"/>
</p>

<p align="center">
  <img src="hero-skills.jpg" alt="AI Agent Skills Hero"/>
</p>

<h1 align="center">🧠 Agent Skills Repository</h1>

<p align="center">
  <strong>A curated collection of AI agent skills for enhanced coding assistance</strong>
</p>

<p align="center">
  <em>Supercharge your AI coding agents with specialized knowledge and production-ready patterns</em>
</p>

<p align="center">
  <a href="#-available-skills">Skills</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 👤 Author

<table>
<tr>
<td width="150">
<img src="https://avatars.githubusercontent.com/yuval-avidani" width="150" alt="Yuval Avidani"/>
</td>
<td>

### **Yuval Avidani**
**AI Builder & Speaker** | **GitHub Star ⭐** | **AWS GenAI Superstar 🌟**

Building the future with AI agents, automation, and cutting-edge technology.  
20+ years turning complex ideas into production-ready solutions.

[![Website](https://img.shields.io/badge/YUV.AI-Website-blue?style=flat-square&logo=safari)](https://yuv.ai)
[![GitHub](https://img.shields.io/badge/GitHub-yuval--avidani-181717?style=flat-square&logo=github)](https://github.com/yuval-avidani)
[![Projects](https://img.shields.io/badge/Open%20Source-110%2B%20Projects-green?style=flat-square&logo=opensourceinitiative)](https://github.com/yuval-avidani)

🎤 **Speaker & Enterprise AI Trainer**  
🏆 **Recognized for open-source contributions**

</td>
</tr>
</table>

> 🤖 *This repository was created by Yuval Avidani using **GitHub Copilot** via **VS Code Insiders** — demonstrating the power of AI-assisted development!*

---

## ✨ What Are Agent Skills?

Agent skills are **specialized knowledge modules** that enhance AI coding agents with domain-specific expertise. They provide:

- 🎯 **Focused Knowledge** — Only what the AI doesn't already know
- 📝 **Production-Ready Code** — Working examples, not abstract concepts  
- ⚡ **Quick Activation** — Trigger keywords for instant context
- 🔄 **Reusable Patterns** — Copy once, use everywhere

---

## �️ Understanding Agent Skills (Open Standard)

### What is SKILL.md?

**SKILL.md** is a simple, open format for giving AI agents new capabilities and expertise. It's an open standard that works across multiple AI coding agents and platforms.

> **Agent Skills** are folders of instructions, scripts, and resources that your AI agent can discover and use to perform tasks more accurately and efficiently.

### Why Use Agent Skills?

**For You (Developer)**:
- 📚 **Learn Faster** — Pre-built knowledge from experts in your domain
- 🎯 **Better Results** — Agents have context to work more accurately
- ♻️ **Reuse Everywhere** — Same skill works across Copilot, Claude Code, Cursor, Windsurf, and more
- 🔐 **Version Control** — Skills are part of your repository, tracked in git

**For Your Team**:
- 📖 **Capture Knowledge** — Document processes and best practices
- 🚀 **Share Skills** — Distribute expertise across projects
- 🏢 **Enterprise Use** — Centralize organizational knowledge

**For AI Agents**:
- 🧠 **Domain Expertise** — Perform specialized tasks reliably
- 🔧 **New Capabilities** — Enable new workflows and automations
- 🎓 **Context** — Access procedures, scripts, and examples on demand

### What Can You Do With Agent Skills?

Agent skills enable AI agents to:
- **Domain Expertise**: Package specialized knowledge (legal review, data analysis, deployment procedures)
- **New Capabilities**: Create presentations, build MCP servers, analyze datasets, debug failures
- **Repeatable Workflows**: Turn multi-step tasks into consistent, auditable processes
- **Interoperability**: Reuse skills across different compatible agent products

---

## 📚 How Agent Skills Work (Step-by-Step for Beginners)

### Step 1: Understanding the File Structure

Each skill is a simple folder with a `SKILL.md` file inside:

```
your-project/
├── .github/skills/          # GitHub Copilot project skills location
│   └── my-skill-name/
│       ├── SKILL.md         # Main skill file (required)
│       ├── script.js        # Optional: supporting scripts
│       └── examples.md      # Optional: more examples
├── .claude/skills/          # Claude Code project skills location
│   └── my-skill-name/
│       └── SKILL.md
└── ~/.copilot/skills/       # Personal skills (available across all projects)
    └── my-skill-name/
        └── SKILL.md
```

### Step 2: Understanding SKILL.md Format

Every `SKILL.md` file has two parts:

**YAML Frontmatter** (metadata):
```yaml
---
name: my-skill-name           # Unique identifier (lowercase, hyphens for spaces)
description: What this skill  # When should the agent use this skill?
license: MIT                  # Optional: license information
---
```

**Markdown Body** (instructions):
The rest of the file contains instructions and examples for the AI agent.

### Step 3: A Real Example

Here's what a simple `SKILL.md` looks like:

```markdown
---
name: github-actions-debugging
description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug CI/CD failures or workflow issues.
---

# Debugging GitHub Actions Workflows

When debugging a failing workflow:

1. **Check the job logs** - Look for error messages and stack traces
2. **Review recent changes** - What changed since the last successful run?
3. **Test locally** - Reproduce the issue in your local environment
4. **Fix and validate** - Make changes and verify they work

## Common Issues and Solutions

### Issue: Workflow fails with "Command not found"
**Solution**: Install the required tool in your workflow step

### Issue: Permission denied when running scripts
**Solution**: Add `chmod +x script.sh` before running the script
```

### Step 4: Agent Discovers and Uses Your Skill

When you ask your AI agent to do something:

```
"Debug why our GitHub Actions workflow is failing"
```

The agent will:
1. ✅ **Recognize** that you're asking about GitHub Actions
2. ✅ **Find** the `github-actions-debugging` skill in your project
3. ✅ **Load** the `SKILL.md` file into its context
4. ✅ **Follow** the instructions to help you debug

### Step 5: Supported Locations

**Project Skills** (specific to one repository):
- `your-repo/.github/skills/` — For GitHub Copilot
- `your-repo/.claude/skills/` — For Claude Code

**Personal Skills** (available across all projects on your machine):
- `~/.copilot/skills/` — For GitHub Copilot (Copilot CLI and VS Code)
- `~/.claude/skills/` — For Claude Code

**Organization/Enterprise Skills** (coming soon):
- Enterprise-level skills support is in development

---

## 🤝 Supported AI Agents

Agent Skills work with these AI coding agents:

| Agent | Support | Location |
|:------|:--------|:---------|
| **GitHub Copilot** | ✅ Full Support | `.github/skills/` or `~/.copilot/skills/` |
| **Claude Code** | ✅ Full Support | `.claude/skills/` or `~/.claude/skills/` |
| **Cursor** | ✅ Full Support | `.cursor/rules/` |
| **Windsurf** | ✅ Full Support | `.windsurf/rules/` |
| **VS Code Insiders** | ✅ Full Support | Agent mode with skills |
| **VS Code (Stable)** | ⏳ Coming Soon | Support coming in future release |

---

## 📦 Available Skills

| Skill | Description | Keywords |
|:------|:------------|:---------|
| **[aws-agentcore](skills/aws-agentcore/SKILL.md)** | AWS Bedrock AgentCore development patterns | `AgentCore`, `Bedrock Agent`, `AWS agent` |
| **[aws-strands](skills/aws-strands/SKILL.md)** | Model-agnostic agent framework with Strands SDK | `Strands`, `ReAct agent`, `model-agnostic` |
| **[aws-account-management](skills/aws-account-management/SKILL.md)** | AWS Organizations, IAM, billing & multi-account | `AWS Organizations`, `IAM`, `SCPs`, `Cost Explorer` |
| **[langchain](skills/langchain/SKILL.md)** | LangChain/LangGraph pipelines and agent workflows | `LangChain`, `LangGraph`, `RAG`, `LCEL` |
| **[vercel](skills/vercel/SKILL.md)** | Vercel deployment, serverless, and edge functions | `Vercel`, `serverless`, `edge function` |
| **[railway](skills/railway/SKILL.md)** | Railway platform deployment and configuration | `Railway`, `deploy container` |
| **[cloudflare](skills/cloudflare/SKILL.md)** | Cloudflare Workers, Pages, D1, R2, KV & AI | `Cloudflare`, `Workers`, `D1`, `R2`, `edge computing` |
| **[figma](skills/figma/SKILL.md)** | Figma API, component code generation & design tokens | `Figma API`, `design tokens`, `Figma to code` |
| **[fal-ai](skills/fal-ai/SKILL.md)** | Serverless AI image/video generation with fal.ai | `fal.ai`, `Flux`, `SDXL`, `AI image generation` |
| **[mongodb](skills/mongodb/SKILL.md)** | MongoDB & Mongoose queries, aggregation pipelines | `MongoDB`, `Mongoose`, `aggregation`, `NoSQL` |
| **[bun](skills/bun/SKILL.md)** | Bun JavaScript runtime, bundler & test runner | `Bun`, `bun.sh`, `JavaScript runtime` |
| **[owasp-security](skills/owasp-security/SKILL.md)** | OWASP Top 10 security vulnerabilities & prevention | `OWASP`, `security`, `XSS`, `SQL injection`, `CSRF` |
| **[shabbat-times](skills/shabbat-times/SKILL.md)** | Jewish calendar data and Shabbat times integration | `Shabbat times`, `Hebcal`, `Zmanim` |
| **[copilot-docs](skills/copilot-docs/SKILL.md)** | GitHub Copilot custom instructions reference | `copilot-instructions.md` |
| **[nano-banana-pro](skills/nano-banana-pro/SKILL.md)** | Google Gemini 3 Pro Image generation | `Nano Banana Pro`, `Gemini 3 Pro Image` |
| **[github-trending](skills/github-trending/SKILL.md)** | GitHub trending repositories scraping | `GitHub trending`, `trending repos` |
| **[ux-design-systems](skills/ux-design-systems/SKILL.md)** | Design systems and component libraries | `design system`, `design tokens`, `theming` |
| **[web-accessibility](skills/web-accessibility/SKILL.md)** | WCAG compliance and accessibility patterns | `accessibility`, `a11y`, `WCAG`, `ARIA` |
| **[mobile-responsiveness](skills/mobile-responsiveness/SKILL.md)** | Responsive design and mobile-first patterns | `responsive`, `mobile-first`, `breakpoints` |
| **[analytics-metrics](skills/analytics-metrics/SKILL.md)** | Data visualization and analytics dashboards | `analytics`, `dashboard`, `charts`, `KPI` |
| **[mermaid-diagrams](skills/mermaid-diagrams/SKILL.md)** | Mermaid diagram syntax for visualizations | `Mermaid`, `flowchart`, `sequence diagram` |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yuval-avidani/ai-agents-skills.git
```

### 2. Copy Skills to Your Project

Choose your AI coding agent and follow the instructions below.

---

## 💻 Setup Guide: Using Skills in Your Agent (For Beginners)

This guide walks you through setting up Agent Skills in your favorite coding agent, step by step.

### 🎯 Prerequisites

Before you start, you need:
- A coding agent installed (Copilot, Claude Code, Cursor, or Windsurf)
- A project folder on your computer
- Basic familiarity with command line or your agent's UI

### 📍 Step-by-Step Setup

#### **Option 1: GitHub Copilot** (Most Popular)

<details>
<summary><strong>🟢 Setup GitHub Copilot with Skills</strong></summary>

**For Project Skills** (specific to one repository):

1. **In your project folder**, create the skills directory:
   ```bash
   mkdir -p .github/skills
   ```

2. **Copy the skills you want** from this repository:
   ```bash
   # Copy a single skill
   cp -r skills/vercel .github/skills/
   
   # Or copy all skills
   cp -r skills/* .github/skills/
   ```

3. **Or manually create a skill**:
   ```
   your-project/
   └── .github/
       └── skills/
           └── my-custom-skill/
               └── SKILL.md
   ```

4. **Open your project in VS Code** and start using Copilot Agent
5. **Ask Copilot a question** related to your skill, and it will automatically load it!

**For Personal Skills** (available across all your projects):

1. **Find your home directory** (`~` or `C:\Users\YourUsername`)

2. **Create personal skills folder**:
   ```bash
   mkdir -p ~/.copilot/skills
   ```

3. **Copy skills there**:
   ```bash
   cp -r skills/vercel ~/.copilot/skills/
   ```

4. **Now all your projects** can use these skills automatically!

**Verify it's working:**
- Open Copilot Agent
- Ask about something covered in your skill (e.g., "How do I deploy to Vercel?")
- Copilot will use the skill to help you

</details>

---

#### **Option 2: Claude Code**

<details>
<summary><strong>🟣 Setup Claude Code with Skills</strong></summary>

**For Project Skills**:

1. **In your project folder**, create the skills directory:
   ```bash
   mkdir -p .claude/skills
   ```

2. **Copy the skills you want**:
   ```bash
   # Single skill
   cp -r skills/langchain .claude/skills/
   
   # All skills
   cp -r skills/* .claude/skills/
   ```

3. **Open your project in Claude Code**
4. **Chat with Claude** about tasks covered in your skills - it will automatically use them!

**For Personal Skills** (available everywhere):

1. **Create personal skills folder**:
   ```bash
   mkdir -p ~/.claude/skills
   ```

2. **Copy skills there**:
   ```bash
   cp -r skills/aws-agentcore ~/.claude/skills/
   ```

**Verify it's working:**
- Open Claude Code in your project
- Ask about something in your skill
- Claude will reference and use the skill

</details>

---

#### **Option 3: Cursor**

<details>
<summary><strong>🔵 Setup Cursor with Skills</strong></summary>

**For Project Rules**:

1. **In your project folder**:
   ```bash
   mkdir -p .cursor/rules
   ```

2. **Copy SKILL.md files** (rename them as rules):
   ```bash
   # Copy a skill as a rule file
   cp skills/figma/SKILL.md .cursor/rules/figma.md
   
   # Or copy multiple
   cp skills/*/SKILL.md .cursor/rules/
   ```

3. **In Cursor Settings**, configure which rules to use:
   - Settings → Rules → Add project rules
   - Point to `.cursor/rules/` folder

4. **Start using Cursor** - it will apply these rules to your context automatically

</details>

---

#### **Option 4: Windsurf**

<details>
<summary><strong>🟡 Setup Windsurf with Skills</strong></summary>

**For Project Rules**:

1. **In your project folder**:
   ```bash
   mkdir -p .windsurf/rules
   ```

2. **Copy skills as rules**:
   ```bash
   # Copy specific skills
   cp skills/vercel/SKILL.md .windsurf/rules/vercel.md
   
   # Or copy all skills
   cp skills/*/SKILL.md .windsurf/rules/
   ```

3. **Windsurf automatically** discovers rules in `.windsurf/rules/`
4. **Start building** - Windsurf will use these rules contextually

</details>

---

### 🎓 What Happens After Setup?

Once you've set up your skills:

1. **Agent Detects Skills**: Your AI agent scans the skill directories
2. **Agent Reads SKILL.md**: It reads the name and description from frontmatter
3. **Agent Activates on Relevance**: When you ask a question matching the description, the agent loads the skill
4. **Agent Follows Instructions**: Your agent now has the context to help you accurately

### 💡 Example: Using a Vercel Skill

**You have this SKILL.md**:
```yaml
---
name: vercel-deployment
description: Deploying applications to Vercel. Use this when asked about deploying, hosting, or managing Vercel projects.
---
```

**You ask your agent**:
> "Help me deploy my React app to Vercel"

**Agent automatically**:
- ✅ Finds `vercel-deployment` skill
- ✅ Loads SKILL.md into context
- ✅ Follows the deployment instructions
- ✅ Helps you deploy successfully!

### 🐛 Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Agent not using skill | Restart your agent, or make sure folder path is correct |
| Skill file not found | Verify `SKILL.md` is in the right folder and named exactly "SKILL.md" |
| Agent using wrong skill | Make sure skill descriptions are descriptive enough to match your request |

---

## 💻 Usage (Advanced)

---

## 📐 Skill Format

Each skill follows a consistent structure:

```markdown
---
name: skill-name
description: Brief description with trigger keywords
---

# Skill Title

Quick start and core patterns...
```

### 🎯 Key Principles

| Principle | Description |
|:----------|:------------|
| **Concise is key** | Only include what the AI doesn't already know |
| **Progressive disclosure** | Start with quick start, then advanced patterns |
| **Concrete examples** | Working code over abstract descriptions |
| **Trigger keywords** | Include words that activate the skill |

---

## 📁 Repository Structure

```
ai-agents-skills/
├── 📄 README.md
├── 📁 skills/
│   ├── 📁 aws-agentcore/
│   │   └── 📄 SKILL.md
│   ├── 📁 aws-strands/
│   │   └── 📄 SKILL.md
│   ├── 📁 aws-account-management/
│   │   └── 📄 SKILL.md
│   ├── 📁 langchain/
│   │   └── 📄 SKILL.md
│   ├── 📁 vercel/
│   │   └── 📄 SKILL.md
│   ├── 📁 railway/
│   │   └── 📄 SKILL.md
│   ├── 📁 cloudflare/
│   │   └── 📄 SKILL.md
│   ├── 📁 figma/
│   │   └── 📄 SKILL.md
│   ├── 📁 fal-ai/
│   │   └── 📄 SKILL.md
│   ├── 📁 mongodb/
│   │   └── 📄 SKILL.md
│   ├── 📁 bun/
│   │   └── 📄 SKILL.md
│   ├── 📁 owasp-security/
│   │   └── 📄 SKILL.md
│   ├── 📁 shabbat-times/
│   │   └── 📄 SKILL.md
│   ├── 📁 copilot-docs/
│   │   └── 📄 SKILL.md
│   ├── 📁 nano-banana-pro/
│   │   └── 📄 SKILL.md
│   ├── 📁 github-trending/
│   │   └── 📄 SKILL.md
│   ├── 📁 ux-design-systems/
│   │   └── 📄 SKILL.md
│   ├── 📁 web-accessibility/
│   │   └── 📄 SKILL.md
│   ├── 📁 mobile-responsiveness/
│   │   └── 📄 SKILL.md
│   ├── 📁 analytics-metrics/
│   │   └── 📄 SKILL.md
│   └── 📁 mermaid-diagrams/
│       └── 📄 SKILL.md
└── 📁 templates/
    └── 📁 skill-template/
        └── 📄 SKILL.md
```

---

## 🤝 Contributing

We welcome contributions! Here's how to add a new skill:

1. **Fork** this repository
2. **Create** a new skill in `skills/your-skill-name/SKILL.md`
3. **Follow** the [skill template](templates/skill-template/SKILL.md)
4. **Submit** a pull request

### Contribution Guidelines

- ✅ Include practical, production-ready code examples
- ✅ Add trigger keywords in the description
- ✅ Test all code snippets before submitting
- ✅ Keep explanations concise but complete
- ❌ Don't include basic concepts the AI already knows
- ❌ Don't use placeholder code or TODOs

---

## 🌟 Star History

If you find this repository useful, please consider giving it a ⭐!

---

## 📄 License

MIT License — Feel free to use, modify, and distribute.

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://yuv.ai">Yuval Avidani</a></strong>
</p>

<p align="center">
  <em>Building AI agents that matter</em>
</p>

<p align="center">
  <a href="https://github.com/yuval-avidani">
    <img src="https://img.shields.io/badge/Follow-@yuval--avidani-181717?style=social&logo=github" alt="Follow on GitHub"/>
  </a>
</p>
