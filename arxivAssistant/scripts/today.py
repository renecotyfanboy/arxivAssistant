from arxivAssistant.feed import ArxivFeed
from rich.console import Console


def main() -> None:

    console = Console()

    with console.status("Fetching today's arxiv..."):
        today = ArxivFeed()

    for article in today.articles:
        article.to_console(console)
