# 🛠️ Glassforge

**Glassforge** is a CLI-first, context-aware development framework for building digital minds like [Blackglass](https://github.com/jonhill90/blackglass).  
It helps humans and AI collaborate intelligently by tracking development state—so the process of building an agent becomes structured, transparent, and learnable.

---

## 🧠 What It Does

Glassforge provides a persistent Model Context Protocol (MCP) to:
- Store your current dev goal, file focus, notes, and outcome history
- Build smart, self-updating prompts for LLMs like GPT, Claude, or Ollama
- Enable tools or local agents to reason about your code like a real assistant
- Act as a cognitive prosthetic so you can focus on *intent*, not micromanagement

---

## 🧩 Core Components

- `client_mcp.json` — Your live development context
- `client_mcp.py` — CLI for setting goals, files, notes, and history
- `server_mcp.py` — Assembles full LLM-ready prompt context
- `agent_driver.py` — Handles API interaction with your chosen AI model

---

## 🔁 Dev Loop Example

```bash
# Set your goal
glassforge goal "Add retry logic to script writer"

# Tell it what file you’re in
glassforge file seed_core/tools/script_writer.py

# Add a note
glassforge note "Preserve existing structure, add fallback path"

# Then run it:
glassforge run gpt4
```

Behind the scenes, it builds the full context from your dev state and feeds it to the model of your choice.  
The result: a suggestion or code diff that is context-aware, reproducible, and logged.

---

## 🧬 Why Glassforge?

When building evolving, reflective systems like AGI Seeds, **you need a mind of your own**—something that remembers what you’re doing, why, and what’s already been tried.

Glassforge is not a project scaffolder.  
It’s a **dev-side intelligence framework** that grows with your intentions.

---

## 📦 File Structure

```
glassforge/
├── client_mcp.json        # Current goal, file, notes, and outcomes
├── client_mcp.py          # CLI commands to manipulate the MCP
├── server_mcp.py          # Prompt builder
├── agent_driver.py        # Sends to GPT, Claude, Ollama, etc.
├── examples/              # Usage patterns and LLM workflows
└── README.md
```

---