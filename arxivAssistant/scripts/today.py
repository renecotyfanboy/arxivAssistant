from arxivAssistant.feed import ArxivFeed


def main() -> None:

    today = ArxivFeed()
    for entry in today.entries:

        print(entry['title'])
        print(entry['authors'])
        print(entry['abstract'])
