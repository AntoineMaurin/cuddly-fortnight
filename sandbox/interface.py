import json

from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Static

top_label = Label("On top")

class MyLittleButtons(Button):

    pass

b1 = MyLittleButtons('yep that"s me')

class SandBox(App):
    DEFAULT_CSS = """
    Screen {
        layout: vertical;
        }

    .box {
        height: 1fr;
        border: solid green;
    }
    """

    def load_data(self):
        return json.loads("data.json")

    def compose(self) -> ComposeResult:

        data = self.load_data()

        yield Static(data["top_label"], classes="box")
        yield Static(data["mid_label"], classes="box")
        yield Static(data["bot_label"], classes="box")
