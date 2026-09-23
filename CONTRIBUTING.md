# Contributing to AId

Thank you for your interest in contributing to **AId**! 

Whether you want to fix a bug, suggest an LLM capability, optimize Discord API rate limits, or improve the documentation, all contributions are welcome.

---

## Code of Conduct
Please be polite, constructive, and respectful to all contributors and community members.

---

## Development Setup

### Prerequisites
- Python 3.10+
- Git
- A Discord Developer Application (with Bot Token and Gateway Intents enabled)

### Local Environment
```bash
# 1. Fork the repo and clone your fork
git clone https://github.com/your-username/AId.git
cd AId

# 2. Create and activate a virtual environment
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Install development dependencies
pip install -r requirements.txt
pip install pytest flake8 black
```

---

## Workflow & Git Guidelines

1. **Create a branch**:
   ```bash
   git checkout -b feat/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
2. **Coding Standards**:
   - Write clean, readable Python following PEP 8.
   - Run `flake8` to check formatting and linting.
   - For discord commands or permission logic, ensure safety checks (role hierarchy, Discord API permission bounds) are preserved.
3. **Commit Messages**:
   - Use clear conventional commit style where possible:
     - `feat: add timeout action to /aid admin`
     - `fix: prevent 429 when creating channels sequentially`
     - `docs: update setup guide in wiki`
4. **Push & Open a Pull Request**:
   - Push your branch to your fork and submit a PR against `main`.
   - Provide a clear description of what changed and reference any related issues (e.g. `Fixes #12`).

---

## Reporting Issues

- **Bugs**: Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template.
- **Feature Ideas**: Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template.
- **Prompts & LLM Schemas**: Use the [Prompt / Tool Schema Proposal](.github/ISSUE_TEMPLATE/prompt_proposal.md) template.
- **Security Vulnerabilities**: Do **not** open a public issue. See [SECURITY.md](SECURITY.md).
