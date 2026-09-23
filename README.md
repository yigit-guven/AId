# AId - AI-Powered Discord Server Management & Architecture

[![Release](https://img.shields.io/github/v/release/yigit-guven/AId?include_prereleases&style=flat-square&color=blue)](https://github.com/yigit-guven/AId/releases)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg?style=flat-square)](https://www.python.org/)

**AId** is an open-source, generative AI assistant for Discord. From scaffolding fully permissioned channels and categories to executing granular administrative tasks via natural language, AId streamlines complex server operations safely. It replaces manual configuration dashboards with an intelligent, prompt-driven engine protected by human-in-the-loop confirmation systems.

---

## 1. Overview and Core Features

AId is designed to translate plain-English intent into strictly validated Discord API actions. Rather than relying on rigid server templates or manual command syntax, AId leverages LLM tool-calling to deduce context, generate required infrastructure, and execute moderation tasks dynamically.

* **Generative Server Scaffolding:** Prompt AId with a concept (e.g., *"Create an esports tournament hub with private team voice channels and a read-only announcements category"*). The bot dynamically generates the optimal channel hierarchy, topic descriptions, and permission overwrites.
* **Conversational Administration:** Execute bulk or complex administrative tasks through natural language. Request actions like *"Assign the @Member role to everyone who joined today"* or *"Lock down all public text channels for the next hour."*
* **Intelligent Moderation:** Move beyond static regex filters. AId can be instructed to perform context-aware automod tasks, such as muting users, detecting sophisticated profanity/toxicity, and issuing timeouts based on conversational context.
* **Interactive Approval UI:** AId operates on a strict "Zero-Surprise" policy. Before any structural change is executed, the bot presents a step-by-step native Discord interface (Buttons and Modals) allowing the administrator to **Approve**, **Edit**, **Skip**, or **Cancel** pending actions.

## 2. System Architecture & Safety Guardrails

AId bridges the gap between probabilistic LLM outputs and deterministic Discord API requirements by routing all AI generation through a strict validation and throttling pipeline.

**Execution Workflow**

1. **Ingestion:** Administrator issues a natural language prompt via `/aid`.
2. **Structured Output (Tool Calling):** The prompt is sent to the LLM (e.g., OpenAI/Anthropic) using a strict JSON schema defining standard Discord entities (categories, channels, roles, permission bitwise values).
3. **Pre-Flight Check:** AId evaluates the generated JSON against its own current `guild.me.guild_permissions`. If the bot lacks required permissions (e.g., `Manage Roles`), it halts the queue and serves an OAuth2 reinvite link to the admin.
4. **Human-in-the-Loop (HITL) Review:** The parsed plan is presented via ephemeral Discord messages. Actions marked as *destructive* (channel deletion, role wiping) require secondary confirmation.
5. **Throttled Deployment:** Approved actions are pushed to an asynchronous token-bucket queue.

**Safety and Throttling Mechanisms**

* **Dynamic Rate Limiting:** Discord aggressively limits channel and role modifications (typically 2–5 actions per 10 seconds). AId’s execution engine utilizes an async token-bucket algorithm to automatically inject `asyncio.sleep()` intervals, ensuring the bot never triggers `429 Too Many Requests` or IP bans.
* **Role Hierarchy Validation:** Before attempting to modify a user or channel locked by a specific role, AId calculates `target_role.position < bot_top_role.position`. If the target is higher in the hierarchy, AId cleanly aborts the specific action and notifies the user, preventing `403 Forbidden` API crashes.
* **Transactional Rollbacks:** Active generation sessions are stored in memory. If a queue is aborted mid-deployment, AId offers an automated rollback to delete entities created during that specific session ID.

## 3. Installation and Configuration

AId requires a Python 3.10+ environment and relies on `discord.py` for gateway connections and API interactions.

**Local Setup**

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/AId.git
cd AId

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

```

**Environment Variables**
Create a `.env` file in the root directory. You must supply both a Discord Bot Token (with Message Content, Server Members, and Presence intents enabled in the Developer Portal) and your preferred LLM API key.

```env
DISCORD_TOKEN=your_discord_bot_token_here
LLM_API_KEY=your_openai_or_anthropic_key_here
MAX_ACTIONS_PER_10S=3
SESSION_TIMEOUT_SECONDS=300
DEBUG_MODE=False

```

**Required Discord Permissions**
To function fully, AId requires the following OAuth2 scopes and permissions. Generating an invite link with integer value `268435472` grants the necessary baseline:

* `Manage Channels`
* `Manage Roles`
* `Moderate Members` (for timeouts/mutes)
* `Read Messages / View Channels`
* `Send Messages` (with `Embed Links` and `Use External Emojis`)

## 4. Usage, Interaction Flow & Contributing

Interacting with AId is driven entirely through application slash commands and component interactions. The bot operates ephemerally to prevent spamming public channels during complex configurations.

**Example Command Workflows**

* `/aid build [prompt]` - Initiates a structural scaffolding session.
* *Example:* `/aid build "Create an internal staff category with a mod-logs channel and a private voice chat"`


* `/aid admin [prompt]` - Initiates a moderation or user-management task.
* *Example:* `/aid admin "Mute @User for 2 hours and delete their messages from the last 15 minutes for toxicity"`



**The Step-by-Step UI**
When a structural plan is generated, AId will return an embed detailing the first proposed action (e.g., `Create Category: 🛡️ Staff Area`). Below the embed, administrators interact with four persistent buttons:

1. **[ ✅ Execute ]** Instantly fires the API call and advances the queue.
2. **[ ⏭️ Skip ]** Drops the current action from the queue and advances.
3. **[ ✏️ Edit ]** Opens a native Discord Modal, allowing the admin to rewrite the channel name, topic, or permission state before executing.
4. **[ ❌ Abort ]** Purges the active session queue entirely.

**Contributing to AId**
Contributions to expand AId's LLM schemas, optimize rate-limiting algorithms, or support additional database backends for logging are welcome. Please ensure all pull requests pass `flake8` linting and include `pytest` coverage for any new rate-limiting logic. Fork the repository, create a feature branch (`git checkout -b feature/new-schema`), and submit a Pull Request detailing the changes to the JSON generation pipeline. All code is licensed under the GPLv3 License.

---

## 5. Legal & Policies

For bot hosting, verification, and Discord Developer Portal compliance:
- [Terms of Service](TERMS_OF_SERVICE.md)
- [Privacy Policy](PRIVACY_POLICY.md)
- [Security Policy](SECURITY.md)
