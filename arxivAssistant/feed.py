import feedparser
from article import Article


class ArxivFeed:

    def __init__(self, feed_url='http://arxiv.org/rss/astro-ph'):
        self.feed_url = feed_url
        self.feed = feedparser.parse(self.feed_url)

        entries = []

        for entry in self.feed['entries']:
            entries.append(Article.from_entry(entry))
        self.entries = entries


today: ArxivFeed = ArxivFeed()
