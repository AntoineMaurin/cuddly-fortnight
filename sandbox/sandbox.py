from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label

my_label = Label("bla")

class MyLittleButtons(Button):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        my_label.content = str(self.label).split("HA")

b1 = MyLittleButtons("HAHAHA")

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
                my_label,
            ),
        )

if __name__ == "__main__":
    app = SandBox()
    app.run()
