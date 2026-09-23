---
name: LLM Tool / Prompt Schema Proposal
about: Propose a new LLM schema, tool-calling capability, or prompt optimization
title: '[SCHEMA]: '
labels: ['enhancement', 'ai/llm']
assignees: ''
---

**Area of LLM Capability**
- [ ] Server Scaffolding (`/aid build`)
- [ ] Moderation / Administration (`/aid admin`)
- [ ] Permission / Hierarchy Validation
- [ ] Other:

**Proposed Prompt or Tool Definition**
Describe the prompt, function signature, or JSON schema you want the model to output:

```json
{
  "action": "...",
  "parameters": {}
}
```

**Expected Discord API Translation**
How should AId map this LLM output to Discord API calls? (e.g. `guild.create_text_channel`, `member.timeout`):

**Safety Considerations**
Does this action involve destructive operations (deletions, role stripping, ban waves)? If so, what confirmation or safety checks should be enforced?
