import feedparser
from .article import Article


class ArxivFeed:

    def __init__(self, feed_url='http://arxiv.org/rss/astro-ph'):
        self.feed_url = feed_url
        self.feed = feedparser.parse(self.feed_url)

        articles = []

        for entry in self.feed['entries']:
            articles.append(Article.from_entry(entry))
        self.articles = articles


today: ArxivFeed = ArxivFeed()
