## Description
<!-- Provide a clear, concise summary of the changes introduced in this pull request. -->

## Related Issues
<!-- Link to any related issues: e.g. Fixes #123, Resolves #45 -->

## Type of Change
- [ ] 🐛 Bug fix (non-breaking change fixing an issue)
- [ ] ✨ New feature (non-breaking change adding functionality)
- [ ] ⚠️ Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update
- [ ] ⚡ Performance optimization / rate limit adjustment

## Changes Made
- 

## Safety & Permissions Checklist
- [ ] Discord API rate-limiting guardrails and token-bucket delays respected.
- [ ] Bot role hierarchy validations remain intact (`target_role.position < bot_role.position`).
- [ ] Destructive actions retain human-in-the-loop (HITL) confirmation prompts.
- [ ] No tokens, API keys, or sensitive secrets are committed.

## Testing & Verification
<!-- Describe testing done locally or in a sandbox Discord guild. -->
- [ ] Tested with Python 3.10+
- [ ] Ran linter (`flake8`) without errors
