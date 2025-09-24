#!/bin/bash
# Install script for mode command

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="/usr/local/bin"

echo "🔧 Installing 'mode' command globally..."

# Check if we have write permission to /usr/local/bin
if [ -w "$INSTALL_DIR" ]; then
    # Create symlink to the main launcher
    ln -sf "$SCRIPT_DIR/mode" "$INSTALL_DIR/mode"
    echo "✅ mode installed to $INSTALL_DIR/mode"
    echo "🚀 You can now run 'mode' from any directory!"
else
    echo "❌ No write permission to $INSTALL_DIR"
    echo "💡 Try running with sudo: sudo ./install-mode.sh"
    echo "💡 Or manually add to your PATH:"
    echo "   export PATH=\"$SCRIPT_DIR:\$PATH\""
    echo "   # Add this line to your ~/.bashrc or ~/.zshrc"
fi

echo ""
echo "📖 Usage:"
echo "  mode                    # Run in current directory"
echo "  mode /path/to/project   # Run in specified directory"
echo "  mode --llm claude       # Use Claude/Anthropic"
echo "  mode --llm deepseek     # Use DeepSeek"
echo "  mode --llm grok         # Use Grok/xAI (default)"
echo "  mode --help             # Show help"