from arxivAssistant.feed import ArxivFeed
from textual.app import App, ComposeResult
from textual.constants import BORDERS
from textual.widgets import Button, Label
from textual.containers import Vertical

today = ArxivFeed()

key_to_renderable = {article.title:article.abstract for article in today.articles}

TEXT = """This is a prototype of arxivAssistant, click any button to checkout an article"""


class BorderButtons(Vertical):
    DEFAULT_CSS = """
    BorderButtons {
        dock: left;
        width: 24;
        overflow-y: scroll;
    }
    BorderButtons > Button {
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        for article in today.articles:
            yield Button(article.title, id=article.title)


class ArxivApp(App):
    """Demonstrates the border styles."""

    CSS = """
    #text {
        margin: 2 4;
        padding: 2 4;
        border: solid $secondary;
        height: auto;
        background: $panel;
        color: $text;
    }
    """

    def compose(self):
        yield BorderButtons()
        self.text = Label(TEXT, id="text")
        yield self.text

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.text.update(key_to_renderable[event.button.id])
        self.bell()
