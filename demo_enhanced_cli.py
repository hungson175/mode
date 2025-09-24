#!/usr/bin/env python3
"""
Demo script to showcase the enhanced CLI features
Run with: python demo_enhanced_cli.py
"""

import time
from coding_agent.ui.enhanced_cli import enhanced_cli
from rich.console import Console

console = Console()


def demo_startup():
    """Demo the enhanced startup panel"""
    print("\n1. STARTUP PANEL DEMO")
    print("-" * 40)

    agent_count = {
        'total': 12,
        'built_in': 8,
        'user_defined': 4
    }

    enhanced_cli.show_startup_panel("/Users/demo/project", agent_count)
    time.sleep(2)


def demo_phases():
    """Demo phase transitions"""
    print("\n2. PHASE TRANSITIONS DEMO")
    print("-" * 40)

    phases = [
        ("Initialization", "Setting up environment and loading configuration", "blue"),
        ("Analysis", "Analyzing codebase and identifying patterns", "yellow"),
        ("Implementation", "Writing code and making changes", "magenta"),
        ("Verification", "Running tests and validating changes", "green")
    ]

    for phase_name, desc, color in phases:
        enhanced_cli.show_phase_transition(phase_name, desc, color)
        time.sleep(1)


def demo_progress():
    """Demo progress indicators"""
    print("\n3. PROGRESS INDICATORS DEMO")
    print("-" * 40)

    # Spinner progress (indeterminate)
    with enhanced_cli.progress_context("Searching for files...") as update:
        for _ in range(5):
            time.sleep(0.5)
            update()

    enhanced_cli.show_status_message("File search completed", "success")

    # Bar progress (determinate)
    with enhanced_cli.progress_context("Processing files...", total=10) as update:
        for _ in range(10):
            time.sleep(0.3)
            update(1)

    enhanced_cli.show_status_message("File processing completed", "success")


def demo_tool_execution():
    """Demo tool execution display"""
    print("\n4. TOOL EXECUTION DEMO")
    print("-" * 40)

    tools = [
        ("Read", "Reading configuration file", {"file_path": "/config/settings.json", "limit": 100}),
        ("Bash", "Running test suite", {"command": "pytest tests/", "timeout": 30000}),
        ("Grep", "Searching for patterns", {"pattern": "TODO|FIXME", "path": "src/"}),
    ]

    for tool_name, desc, params in tools:
        enhanced_cli.show_tool_execution(tool_name, desc, params)
        time.sleep(1)


def demo_todo_list():
    """Demo todo list display"""
    print("\n5. TODO LIST DEMO")
    print("-" * 40)

    todos = [
        {"content": "Set up development environment", "status": "completed", "activeForm": "Setting up development environment"},
        {"content": "Analyze requirements", "status": "completed", "activeForm": "Analyzing requirements"},
        {"content": "Implement core functionality", "status": "in_progress", "activeForm": "Implementing core functionality"},
        {"content": "Write unit tests", "status": "pending", "activeForm": "Writing unit tests"},
        {"content": "Run integration tests", "status": "pending", "activeForm": "Running integration tests"},
        {"content": "Deploy to staging", "status": "pending", "activeForm": "Deploying to staging"}
    ]

    enhanced_cli.show_todo_list(todos)
    time.sleep(2)


def demo_results():
    """Demo result panels"""
    print("\n6. RESULT PANELS DEMO")
    print("-" * 40)

    # Success result
    success_content = """
## Operation Completed Successfully

✓ All tests passed (15/15)
✓ No linting errors found
✓ Build completed in 2.3 seconds

**Next Steps:**
- Review the changes
- Commit to repository
- Deploy to staging
"""

    enhanced_cli.show_result_panel("✨ Build Success", success_content, "green")
    time.sleep(2)

    # Error result
    error_content = """
## Build Failed

❌ Test failures: 3
❌ Linting errors: 5
❌ Type errors: 2

Please fix the issues and try again.
"""

    enhanced_cli.show_result_panel("⚠️ Build Failed", error_content, "red")
    time.sleep(2)


def demo_status_messages():
    """Demo status messages with semantic colors"""
    print("\n7. STATUS MESSAGES DEMO")
    print("-" * 40)

    messages = [
        ("Project initialized successfully", "success"),
        ("Configuration file not found, using defaults", "warning"),
        ("Failed to connect to database", "error"),
        ("Loading dependencies...", "processing"),
        ("Analysis in progress", "info"),
        ("All tasks completed!", "complete")
    ]

    for message, status_type in messages:
        enhanced_cli.show_status_message(message, status_type)
        time.sleep(0.5)


def demo_file_operations():
    """Demo file operation displays"""
    print("\n8. FILE OPERATIONS DEMO")
    print("-" * 40)

    operations = [
        ("read", "src/main.py", {"lines": 150, "cached": True}),
        ("write", "output/report.md", {"size": "2.3KB"}),
        ("edit", "config.json", {"changes": 3, "lines_modified": 12}),
        ("search", "**/*.py", {"matches": 42, "files": 8})
    ]

    for op, path, details in operations:
        enhanced_cli.show_file_operation(op, path, details)
        time.sleep(0.5)


def demo_model_switch():
    """Demo model switching display"""
    print("\n9. MODEL SWITCH DEMO")
    print("-" * 40)

    enhanced_cli.show_model_switch(
        "claude-sonnet-4-20250514",
        "grok-code-fast-1"
    )
    time.sleep(2)


def demo_command_summary():
    """Demo command execution summary"""
    print("\n10. COMMAND SUMMARY DEMO")
    print("-" * 40)

    # Successful command
    enhanced_cli.show_command_execution_summary("npm test", 0, 5.2)
    time.sleep(1)

    # Failed command
    enhanced_cli.show_command_execution_summary("npm build", 1, 3.8)
    time.sleep(1)


def main():
    """Run all demos"""
    console.print("[bold cyan]ENHANCED CLI FEATURES DEMO[/bold cyan]")
    console.print("[yellow]Showcasing Rich UI improvements for sonph-code[/yellow]\n")

    demos = [
        demo_startup,
        demo_phases,
        demo_progress,
        demo_tool_execution,
        demo_todo_list,
        demo_results,
        demo_status_messages,
        demo_file_operations,
        demo_model_switch,
        demo_command_summary
    ]

    for demo_func in demos:
        demo_func()
        enhanced_cli.print_separator()
        time.sleep(0.5)  # Auto-advance instead of waiting for input

    console.print("\n[bold green]✨ Demo Complete![/bold green]")
    console.print("[dim]All enhanced CLI features have been demonstrated.[/dim]")


if __name__ == "__main__":
    main()