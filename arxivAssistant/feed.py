import feedparser
import re


# Extract text from a html hyperlink
def extract_text(html):
    res = re.search(r'>(.*)<', html)
    if res is not None:
        return res.group(1)


class ArxivFeed:

    def __init__(self, feed_url='http://arxiv.org/rss/astro-ph'):
        self.feed_url = feed_url
        self.feed = feedparser.parse(self.feed_url)

        entries = []

        for entry in self.feed['entries']:
            entries.append({'title': entry['title'],
                            'link': entry['link'],
                            'abstract': entry['summary'][3:-4].replace('\n', ' '),
                            'authors': [extract_text(author) for author in entry['authors'][0]['name'].split(',') if extract_text(author) is not None]})
        self.entries = entries

today: ArxivFeed = ArxivFeed()
