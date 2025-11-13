from textual.app import App, ComposeResult
from textual.widgets import Button, Label
from textual.containers import Horizontal, Vertical

my_label = Label("see me ?")

class MyLittleButtons(Button):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        my_label.content = str(self.label)

b1 = MyLittleButtons("Default")

class StopwatchApp(App):
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
    app = StopwatchApp()
    app.run()
