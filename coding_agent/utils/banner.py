"""ASCII art banner and startup screen for sonph-code."""

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def get_ascii_banner():
    """Get the ASCII art banner for sonph-code."""
    return """
 ██████  ██████  ███    ██ ██████  ██   ██      ██████  ██████  ██████  ███████ 
██      ██    ██ ████   ██ ██   ██ ██   ██     ██      ██    ██ ██   ██ ██      
███████ ██    ██ ██ ██  ██ ██████  ███████     ██      ██    ██ ██   ██ █████   
     ██ ██    ██ ██  ██ ██ ██      ██   ██     ██      ██    ██ ██   ██ ██      
███████  ██████  ██   ████ ██      ██   ██      ██████  ██████  ██████  ███████ 
"""


def get_stylized_banner():
    """Get a stylized banner with block characters similar to Gemini CLI."""
    return """
██████  ████████ ███    ██ ██████  ██   ██           ██████  ████████ ███████  ████████ 
██      ██    ██ ████   ██ ██   ██ ██   ██          ██      ██    ██ ██       ██       
████████ ██  ██  ██ ██  ██ ██████  ███████          ██      ██  ██   ███████  ████████ 
      ██ ██  ██  ██  ██ ██ ██      ██   ██          ██      ██  ██        ██  ██       
██████   ██  ██  ██   ████ ██      ██   ██           ██████  ██  ██   ███████  ████████ 
"""


def get_gradient_banner():
    """Get a colorful gradient version of the banner."""
    lines = get_ascii_banner().strip().split("\n")
    colored_lines = []

    colors = [Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.GREEN]

    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        colored_lines.append(color + line)

    return "\n".join(colored_lines)


def show_startup_screen(agent_count=None, working_dir=None):
    """Show the complete startup screen with banner and tips."""
    # Create a gradient background effect
    print()

    # Show the main banner with gradient colors - SONPH CODE
    banner_lines = [
        " ████  ███  █   █ ████  █   █       ███   ███  ████  █████",
        "█     █   █ ██  █ █   █ █   █      █     █   █ █   █ █    ",
        " ███  █   █ █ █ █ ████  █████      █     █   █ █   █ ████ ",
        "    █ █   █ █  ██ █     █   █      █     █   █ █   █ █    ",
        "████   ███  █   █ █     █   █       ███   ███  ████  █████",
    ]

    colors = [Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.RED, Fore.YELLOW]

    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        print(color + Style.BRIGHT + line)

    print()
    print(Fore.WHITE + Style.BRIGHT + "Claude Code Clone - AI-Powered Coding Assistant")
    print()

    if working_dir:
        print(
            Fore.CYAN + Style.BRIGHT + "Working Directory: " + Fore.WHITE + working_dir
        )

    if agent_count:
        print(
            Fore.GREEN
            + Style.BRIGHT
            + "Available Agents: "
            + Fore.WHITE
            + f"{agent_count['total']} total "
            + Fore.CYAN
            + f"({agent_count['built_in']} built-in, {agent_count['user_defined']} user-defined)"
        )

    print()
    print(Fore.YELLOW + Style.BRIGHT + "Tips for getting started:")
    tips = [
        "Ask questions, edit files, or run commands.",
        "Be specific for the best results.",
        "Use '/init' to analyze codebase and create CLAUDE.md.",
        "Type '/help' for more information.",
    ]

    for i, tip in enumerate(tips, 1):
        print(Fore.WHITE + f"{i}. " + Style.DIM + tip)

    print()

    # Show example prompts in a more compact format
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "> "
        + Fore.WHITE
        + "Write a short paragraph about why Sonph CLI is awesome"
    )
    print()
    print(
        Fore.WHITE
        + Style.DIM
        + '• I will start by searching the web for "Sonph CLI" to understand its main features and purpose. Following'
    )
    print(
        Fore.WHITE
        + Style.DIM
        + "  that, I'll then search for file utils in project overview. I will then consult docs/overview.md"
    )
    print(
        Fore.WHITE
        + Style.DIM
        + "  and docs/CLI/Commands.md to gain a deeper understanding of its capabilities. Finally, I will write a short"
    )
    print(Fore.WHITE + Style.DIM + "  paragraph summarizing why Sonph CLI is awesome.")

    print()
    print(
        Fore.BLUE
        + Style.BRIGHT
        + "WebSearch "
        + Fore.WHITE
        + Style.DIM
        + 'Searching the web for: "Sonph CLI features and purpose"'
    )
    print()


def show_compact_banner():
    """Show a compact version for when space is limited."""
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "🚀 "
        + Fore.WHITE
        + "SONPH-CODE"
        + Fore.CYAN
        + " - Claude Code Clone"
    )
