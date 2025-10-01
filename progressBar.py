from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ProgressBar, Label, Static

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Label("Progress Example")
        yield ProgressBar(total=100)  # Example usage of ProgressBar
        yield Static("Static content")

if __name__ == "__main__":
    app = MyApp()
    app.run()