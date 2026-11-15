from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Static

top_label = Label("On top")

class MyLittleButtons(Button):

    pass

b1 = MyLittleButtons('yep that"s me')

ext_data = {
    "top_label": "top One",
    "mid_label": "MID",
    "bot_label": "ART",
}

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

    def get_data(self):
        return ext_data

    def compose(self) -> ComposeResult:

        data = self.get_data()

        yield Static(data["top_label"], classes="box")
        yield Static(data["mid_label"], classes="box")
        yield Static(data["bot_label"], classes="box")
