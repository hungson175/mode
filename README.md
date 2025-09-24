# Mode - Advanced AI Coding Assistant

A powerful Python-based coding agent that provides Claude Code-like functionality using LangChain with support for multiple LLM providers.

## Quick Start

### Option 1: Install globally (Recommended)

1. **Install required dependencies:**
   ```bash
   # Install ripgrep (required for search functionality)
   brew install ripgrep  # macOS
   # sudo apt install ripgrep  # Linux

   # Install Python dependencies
   uv sync
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add at least one API key:
   # - XAI_API_KEY (for Grok - default provider)
   ```

3. **Install mode globally:**
   ```bash
   # Run the installation script to create global 'mode' command
   ./install.sh
   # Or with sudo if needed:
   # sudo ./install.sh

   # After installation, you can use:
   mode                    # Run in current directory (uses Grok by default)
   ```

### Option 2: Run locally without global installation

If you prefer not to install globally, you can run mode directly:

```bash
# Follow steps 1-2 from Option 1 to install dependencies and set up API keys
# Then run directly:
uv run python main.py
```

## Features

- **Multiple LLM Providers**: Support for Grok (default), Claude/Anthropic, and DeepSeek
- **Rich CLI Interface**: Autocomplete for commands, syntax highlighting, and interactive prompts
- **Comprehensive Tools**: File operations (Read, Write, Edit), search (Grep, Glob), execution (Bash), and task management
- **Background Process Management**: Run long-running commands in background with monitoring
- **Smart Caching**: Provider-specific cache optimization for better performance
- **Git Integration**: Intelligent git operations with guidance
- **Package Management**: Prefers Yarn over npm with global cache for faster installs

## Supported LLM Providers

| Provider | Model | Environment Variable | Notes |
|----------|-------|---------------------|--------|
| **Grok** (Default) | grok-code-fast-1 | XAI_API_KEY | Fast inference, auto-cache |
| Claude/Anthropic | claude-sonnet-4-20250514 | ANTHROPIC_API_KEY | Manual cache control |
| DeepSeek | deepseek-chat | DEEPSEEK_API_KEY | Cost-effective, auto-cache |

## Interactive Commands

While using Mode, you can use these commands:

- `/model` - Switch between LLM providers or view current model
- `/commands` - List all available commands
- `/context` - Show context usage visualization
- `/memory` - View current memory context
- `/init` - Analyze codebase and create/update CLAUDE.md
- `pwd` - Show current working directory
- `cd <path>` - Change working directory
- `reset` - Reset conversation history
- `quit`/`exit` - Exit the agent
- `Ctrl+C` or `Esc` - Cancel long-running operations

## Example Prompts

Here are some example prompts to try with Mode:

- Tạo game cờ caro (5 quân thẳng hàng/chéo, không phải tic-tac-toe) cho web sử dụng NextJS/ReactJS với thiết kế tối giản cho 2 người chơi, màu đen trắng - trông như kiểu cờ vây ấy. 2D với shadow đẹp đẹp tí, nhưng vẫn phải simple và elegant nhá ! Tạo thư mục để làm version mới hoàn toàn nhá !
- Create a chess game for 2 players (human vs human) using NextJS/React with minimalist black/white design, beautiful and clear graphics, implementing all chess rules (winning conditions, castling, etc.) - use image or something nice for chess figure, not just font
- Read file expense-tracker-prompt.txt then implement the application
- Analyze this codebase and suggest improvements
- Add dark mode support to my React application
- Help me refactor this code to follow SOLID principles

## Development

For development details, see [CLAUDE.md](CLAUDE.md) which contains:
- Architecture overview
- Tool implementations
- Development commands
- Contributing guidelines

## License

This project is for educational and demonstration purposes.
