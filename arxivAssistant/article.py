import re
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from typing import NamedTuple
from html import unescape
from rich.console import Group

def extract_text(html):
    res = re.search(r'>(.*)<', html)
    if res is not None:
        return res.group(1)


def split_authors(authors):

    return [extract_text(author) for author in authors[0]['name'].split(',') if extract_text(author) is not None]


class Article(NamedTuple):
    title: str
    abstract: str
    authors: list[str]
    link: str

    @classmethod
    def from_entry(cls, entry: dict) -> 'Article':
        return cls(
            entry['title'],
            entry['summary'][3:-4].replace('\n', ' '),
            split_authors(entry['authors']),
            entry['link']
        )

    def __rich__(self):

        if len(self.authors) > 10:
            author_list = self.authors[:10] + ["et al."]
        else:
            author_list = self.authors

        # make a string with all the authors separated by commas
        authors = ", ".join(author_list)
        # decode numerical unicode characters in the authors string
        authors = unescape(authors)

        panel_group = Group(
            Panel(Text(self.title, justify="center"), style="bold red"),
            Panel(Text(authors, justify="center"), style="italic green", title='Authors'),
            Panel(Text(self.abstract, justify="full"))
        )

        return panel_group#text

    # make a method to print the article in a rich way as done in today.py
    def to_console(self, console: Console):

        console.rule(self.title, style="bold red")
        # this should be done in the feed class
        # if there are more than 10 authors, keep only the first 10 and replace the rest with "et al."
        if len(self.authors) > 10:
            author_list = self.authors[:10] + ["et al."]
        else:
            author_list = self.authors

        # make a string with all the authors separated by commas
        authors = ", ".join(author_list)
        # decode numerical unicode characters in the authors string
        authors = unescape(authors)

        console.print(f"{authors}", style="italic green")
        console.print(self.abstract)
        console.print()
