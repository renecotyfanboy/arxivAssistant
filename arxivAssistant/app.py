from textual.app import App
from textual.widgets import Footer, Placeholder, Header
from arxivAssistant.list import ListViewUo
from arxivAssistant.feed import ArxivFeed
from textual.reactive import Reactive
from textual.widgets import ScrollView
from textual.widgets import Button, ButtonPressed
from rich.panel import Panel
from rich.text import Text


class ArticleName(Button):

    mouse_over = Reactive(False)

    def __init__(self, text: str):
        super().__init__(text)
        self.text = text

    def render(self) -> Panel:
        return Panel(self.text, style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class ArxivApp(App):

    async def on_mount(self) -> None:
        today = ArxivFeed()
        self.body = ScrollView()
        self.articles = {article.title:article for article in today.articles}

        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(
            ListViewUo([ArticleName(article.title) for article in today.articles]), edge="left", size=60)
        await self.view.dock(self.body, edge="right")

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("q", "quit", "Quit")

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        """A message sent by the button widget"""

        assert isinstance(message.sender, Button)
        button_name = message.sender.name

        await self.body.update(self.articles[button_name])
