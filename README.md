# Vibe Coding: Mobile-to-Laptop AI Agent Environment

"Vibe Coding" is a project designed to allow developers to control their laptop and manage coding tasks entirely through a mobile device (via SSH/Tailscale), powered by an AI Agent (Opencode).

## 🚀 Key Features
- **Mobile Friendly:** Optimized for SSH terminals like Termius.
- **Autonomous Agent:** A terminal-based chat interface that can run commands and edit files.
- **System Monitoring:** Keep track of laptop battery and performance remotely.
- **Git Integration:** Automatic syncing with GitHub.

## 🛠 Usage
Run these commands in your mobile terminal:
- `vstatus`: Check laptop's CPU, RAM, and Battery.
- `vrun`: Execute the main project code.
- `vchat`: Start interacting with the AI Agent.
- `vsync`: Commit and push changes to GitHub.

## ⚠️ Requirements
- **Tailscale:** Must be active on both laptop and mobile.
- **SSH Server:** OpenSSH should be running on Windows.
- **API Key:** Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` in Windows environment variables for the agent's brain.

---
*Created by Opencode Agent*
