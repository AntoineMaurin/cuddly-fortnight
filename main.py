from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Digits
from textual.containers import Center

from clock import run

class MyApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True, name="header name")
        yield Footer(name="foota")
        self.title="test title"
        yield  Digits("3.141,592,653,5897", id="pi")
        # yield Center(name="Center name")

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
