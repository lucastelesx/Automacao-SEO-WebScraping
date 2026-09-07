from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.pretty import Pretty
from rich.traceback import install

console = Console()
install(show_locals=True)

def display_html(html_content, title="Output HTML"):
    """
    Recebe uma string HTML e renderiza no terminal com syntax highlighting.
    """
    # Se o conteúdo vier de um soup.prettify(), ele já é string.
    syntax = Syntax(
        str(html_content), 
        "html", 
        theme="monokai", 
        line_numbers=True,
        word_wrap=True # Evita que o HTML quebre o layout do terminal
    )
    
    # Criamos um painel para o conteúdo não ficar "solto" no terminal
    panel = Panel(
        syntax, 
        title=f"[bold magenta]{title}[/bold magenta]", 
        border_style="blue",
        expand=False
    )
    
    console.print(panel)

def log(message):
    console.log(f"[bold blue]ℹ[/bold blue] [light_slate_grey]{message}[/light_slate_grey]")

def log_success(message):
    console.log(f"[green]✔[/green] {message}")

def log_error(message):
    console.log(f"[bold red]✘:[/bold red] {message}")

def log_pretty(code):
    console.print(Pretty(code, expand_all=True, indent_guides=True,justify='left'))