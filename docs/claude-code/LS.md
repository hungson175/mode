# LS Tool

## Description

Lists files and directories in a given path. The path parameter must be an absolute path, not a relative path. You can optionally provide an array of glob patterns to ignore with the ignore parameter. You should generally prefer the Glob and Grep tools, if you know which directories to search.

## Usage Notes

- **Path must be absolute**, not relative
- Optional `ignore` parameter with array of glob patterns to exclude
- Generally prefer Glob and Grep tools when you know which directories to search
- Useful for exploring directory structure and verifying paths exist

## Schema

```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string",
      "description": "The absolute path to the directory to list (must be absolute, not relative)"
    },
    "ignore": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of glob patterns to ignore"
    }
  },
  "required": [
    "path"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```