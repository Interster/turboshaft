from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ProgressBar, Label, Static
from textual.reactive import reactive
from textual import on, work
import asyncio

class RevCounter(Static):
    rpm = reactive(0)  # Reactive RPM value (0-8000 for a typical engine redline)

    def compose(self) -> ComposeResult:
        yield Label("RPM: ", id="rpm-label")
        yield ProgressBar(total=8000, show_percentage=False)  # Gauge: 0-8000 RPM
        yield Static("Use ↑/↓ to adjust RPM | Q to quit", id="footer-info")

    def watch_rpm(self, value: int) -> None:
        self.query_one("#rpm-label", Label).update(f"RPM: {value:,}")
        self.query_one(ProgressBar).update(advance=value)

    async def _auto_rpm(self) -> None:
        while True:
            if 0 < self.rpm < 8000:
                self.rpm += 100 if self.rpm < 4000 else -100  # Oscillate
            await asyncio.sleep(0.1)

class RevCounterApp(App):
    CSS = """
    RevCounter {
        align: center middle;
        ProgressBar {
            width: 40;
            height: 1;  /* Adjusted for ProgressBar, which is typically linear */
            background: $background 50%;
            &.high { background: red; }  /* Redline styling */
        }
        #rpm-label {
            content-align: center middle;
            text-style: bold;
            color: white;
        }
    }
    Screen {
        background: black;
    }
    """

    def __init__(self):
        super().__init__()
        self.counter = RevCounter()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield self.counter
        yield Footer()

    def on_mount(self) -> None:
        self.counter.rpm = 1500  # Starting RPM
        # Optional: Start auto RPM simulation (uncomment to enable)
        # asyncio.create_task(self.counter._auto_rpm())

    def on_key(self, event):
        if event.key == "up":
            self.counter.rpm = min(8000, self.counter.rpm + 500)
        elif event.key == "down":
            self.counter.rpm = max(0, self.counter.rpm - 500)
        if self.counter.rpm > 6000:
            self.counter.query_one(ProgressBar).add_class("high")  # Add redline class
        else:
            self.counter.query_one(ProgressBar).remove_class("high")

if __name__ == "__main__":
    app = RevCounterApp()
    app.run()