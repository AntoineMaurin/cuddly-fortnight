import time

from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Footer, Header, Digits, Input
from textual.containers import Center

from textual.widget import Widget
from textual.reactive import reactive

MINUTES = 0.1

class Hello(Widget):

    name = "base name"

    def render(self) -> RenderResult:
        return f"Hello, [b]{self.name}[/b]!"


class TextInput(Input):
    placeholder = "write something"
    name = "input placeholder"

    def on_input_changed(self, c):
        Hello.name = self.value

class MyApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    CSS = """
    Screen {
        align: center middle;       
    }
    
    #center {
        width: 120;
    }
    """

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        self.title = "Tamada"
        yield Header(show_clock=True, name="header name")
        # with Center(id="center"):
        yield TextInput()
        yield Hello()

        # yield Footer(name="foota")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "catppuccin-mocha" if self.theme == "textual-light" else "textual-light"
        )

def main():
    print("Hello from clock!")
    app = MyApp()
    app.run()
    # run(0.1)


if __name__ == "__main__":
    main()
