# ExitPlanMode Tool

## Description

Use this tool when you are in plan mode and have finished presenting your plan and are ready to code. This will prompt the user to exit plan mode.

## When to Use

**IMPORTANT**: Only use this tool when the task requires planning the implementation steps of a task that requires writing code. For research tasks where you're gathering information, searching files, reading files or in general trying to understand the codebase - do NOT use this tool.

## Examples

### ✅ Use ExitPlanMode
- Initial task: "Help me implement yank mode for vim" - Use the exit plan mode tool after you have finished planning the implementation steps of the task.

### ❌ Don't Use ExitPlanMode  
- Initial task: "Search for and understand the implementation of vim mode in the codebase" - Do not use the exit plan mode tool because you are not planning the implementation steps of a task.

## Schema

```json
{
  "type": "object",
  "properties": {
    "plan": {
      "type": "string",
      "description": "The plan you came up with, that you want to run by the user for approval. Supports markdown. The plan should be pretty concise."
    }
  },
  "required": [
    "plan"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```