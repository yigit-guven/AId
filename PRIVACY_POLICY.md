# Privacy Policy for AId

**Last Updated:** September 23, 2026

This Privacy Policy explains how **AId** ("the Bot", "we", "our") collects, uses, and protects information when you invite and use the Bot within your Discord guild (server).

---

## 1. Information We Collect

To function properly, AId processes minimal data strictly necessary for fulfilling administrator prompts:

1. **Discord Entity Identifiers**:
   - Guild IDs, Channel IDs, Role IDs, and User IDs required to route commands and execute requested operations.
2. **Command Prompts & User Input**:
   - The text provided in slash commands (e.g., `/aid build [prompt]` or `/aid admin [prompt]`).
3. **Guild Hierarchy & Permissions**:
   - Bot permission sets and role hierarchy positions to ensure safe execution without triggering API errors.
4. **Temporary Session Data**:
   - In-memory state of active scaffolding queues (session IDs, pending actions, rollback targets).

---

## 2. Information We Do NOT Collect

- We do **not** log, store, or sell user chat message histories.
- We do **not** collect personal identification information (e.g., real names, physical addresses, payment details, or email addresses) through Discord.
- We do **not** harvest voice channel audio.

---

## 3. How We Use Information

The collected data is used exclusively for:
- Interpreting administrator requests into structured Discord API operations via LLM tool-calling.
- Performing pre-flight role hierarchy and permission validation.
- Enforcing rate-limiting token buckets to avoid API threshold breaches.
- Providing transactional session rollbacks upon user cancellation.

---

## 4. Third-Party Services (LLM Providers)

When you run a generative command, prompt text and relevant structural context (e.g., channel names or role titles) are sent to configured LLM APIs (such as OpenAI or Anthropic). 

- Data handled by third-party LLMs is subject to the respective provider's data usage and retention policies.
- Under default enterprise/API policies, data submitted via APIs is not used by providers to train foundation models.

---

## 5. Data Retention & Deletion

- **In-Memory Retention**: Generation queues and approval states are ephemeral and automatically expire after the session timeout (default: 300 seconds).
- **Data Deletion**: When AId is removed or kicked from a Discord server, active in-memory session data for that guild is instantly wiped.
- To request deletion of any persisted logs or inquire about stored metadata, please contact `contact@yigitguven.net`.

---

## 6. Security

We take reasonable technical measures to protect bot tokens, API keys, and server interaction flows. No human credentials or tokens are stored in unencrypted public repositories.

---

## 7. Changes to This Policy

We may update this Privacy Policy as new features and capabilities are introduced. Changes will be committed directly to this repository.

---

## 8. Contact

If you have any questions or concerns regarding this Privacy Policy, please contact us at:
- **Email:** `contact@yigitguven.net`
- **Discord:** [Community & Support Server](https://discord.gg/24Ea8ssnKj)
