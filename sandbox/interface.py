from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label

top_label = Label("On top")

class MyLittleButtons(Button):

    pass

b1 = MyLittleButtons('yep that"s me')

class SandBox(App):
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                b1,
                Button.success("Success!"),
                Button.warning("Warning!"),
                Button.error("Error!"),
            ),
            Vertical(
                top_label,
            ),
        )
