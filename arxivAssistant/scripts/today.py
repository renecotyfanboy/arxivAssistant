from arxivAssistant.feed import ArxivFeed
from rich.console import Console
from html import unescape

def main() -> None:

    console = Console()

    with console.status("Fetching today's arxiv..."):
        today = ArxivFeed()


    for entry in today.entries:

        #remove what is between parenthesis in the title string
        console.rule(entry['title'].split('(')[0], style="bold red")

        #if there are more than 10 authors, keep only the first 10 and replace the rest with "et al."
        if len(entry['authors']) > 10:
            entry['authors'] = entry['authors'][:10] + ["et al."]
        #make a string with all the authors separated by commas
        authors = ", ".join(entry['authors'])
        #decode numerical unicode characters in the authors string
        authors = unescape(authors)

        console.print(f"{authors}", style="italic green")
        console.print(entry['abstract'])
        console.print()
