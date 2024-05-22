import datetime
from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()
tasks = []


def add_task():
    task_description = Prompt.ask("[bold blue]Enter task description[/]")
    due_date_str = Prompt.ask("[bold blue]Enter due date (YYYY-MM-DD)[/]", default=None)
    due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
    tasks.append({"description": task_description, "due_date": due_date, "completed": False})
    console.print(Panel("[bold green]Task added successfully![/]"))


def view_tasks():
    table = Table(title="To-Do List", show_header=True, header_style="bold magenta")
    table.add_column("No.", justify="right", style="dim", width=5)
    table.add_column("Description")
    table.add_column("Due Date", justify="center")
    table.add_column("Status", justify="center")

    for index, task in enumerate(tasks, start=1):
        due_date_str = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else ""
        status = "[bold green]Done[/]" if task["completed"] else "[bold red]Pending[/]"
        table.add_row(str(index), task["description"], due_date_str, status)

    console.print(table)


def mark_complete():
    view_tasks()
    task_index = int(Prompt.ask("[bold blue]Enter task number to mark complete[/]")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        console.print(Panel("[bold green]Task marked as complete![/]"))
    else:
        console.print(Panel("[bold red]Invalid task number![/]"))


while True:
    console.print(Panel("[bold yellow]Choose an action:[/]\n1. Add Task\n2. View Tasks\n3. Mark Complete\n4. Exit"))
    choice = Prompt.ask("[bold blue]Enter your choice[/]")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        console.print(Panel("[bold yellow]Exiting...[/]"))
        break
    else:
        console.print(Panel("[bold red]Invalid choice![/]"))
