import re
from typing import NamedTuple


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
