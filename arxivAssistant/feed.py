import feedparser

class ArxivFeed:

    def __init__(self, feed_url='http://arxiv.org/rss/astro-ph'):
        self.feed_url = feed_url
        self.feed = feedparser.parse(self.feed_url)

    @property
    def entries(self):

        entries = []

        for entry in self.feed['entries']:

            entries.append({'title': entry['title'],
                            'link': entry['link'],
                            'abstract': entry['summary'],
                            'authors': entry['authors']})

        return entries
