from time import monotonic  # Monotonic clock, ideal for measuring elapsed time.
from textual.app import App  # Base class for all Textual TUIs.
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.containers import VerticalScroll
from textual.reactive import (
    reactive,
)  # Allows defining dynamic data display. refres() can be called to reload new data in widget.
from textual.widgets import Footer  # Shows a bar at the bottom of the screen with bound keys.
from textual.widgets import Header  # Shows a little title on the top
from textual.widgets import Button  # Shows a button with given text, id for css (maybe), and variant (pre-built styles)
from textual.widgets import Digits  # Shows a digit-like style widget


class TimeDisplay(Digits):  # Widget that inherits from Digits, showing digit-style widget
    """My first custom widget! It displays elapsed time"""

    # These will be available in self
    start_time = reactive(
        monotonic
    )  # Start time for when the stopwatch starts. reactive first argument can be a default value or a callable. reactive first argument can be a default value or a callable
    time = reactive(0.0)  # Elapsed time since start_time
    total = reactive(0.0)  # Total time elapsed since start_time, including when paussing

    def on_mount(self) -> None:
        """Event handler called when the widget is added to the app"""
        self.update_timer = self.set_interval(
            1 / 60, self.update_time, pause=True
        )  # set_interval ssets a timer which calls a function every 1/60 secs.

    def update_time(self) -> None:
        """Method to update the time to the current time"""
        self.time = self.total + monotonic() - self.start_time  # Updates time

    def watch_time(
        self, time: float
    ) -> None:  # Watch methods start with watch_. Are called every time the attribute changes
        """Called when the time attribute changes"""
        minutes, seconds = divmod(time, 60)  # Calculates minutes and seconds
        hours, minutes = divmod(minutes, 60)  # Calculates hours and minutes
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        """Method to start (or resume) time updating"""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self) -> None:
        """Method to stop the time display updating."""
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total

    def reset(self) -> None:
        """Method to reset the time display to zero"""
        self.total = 0
        self.time = 0


class StopWatch(HorizontalGroup):  # Groups horizontally a group of widgets
    """My second custom widget! It represents a stopwatch widget"""

    def on_button_pressed(self, event: Button.Pressed) -> None:  # Event handler for when a StopWatch button is pressed
        """My first Textual event handler! When a stopwatch button is pressed, add css classes for dynamism."""
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)  # query_one gets a refference to the TimeDisplay widget
        if button_id == "start":
            time_display.start()
            self.add_class("started")  # The add_class method adds a css class to the given instance.
        elif button_id == "stop":
            time_display.stop()
            self.remove_class("started")  # The remove_class method removes a css class from the given instance.
        elif button_id == "reset":
            time_display.reset()

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch"""
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay()


class StopwatchApp(App):  # My first app
    """A simple stopwatch app, created with the purpose of learning Textual UI :)"""

    CSS_PATH = "stopwatch03.tcss"  # The path of my .tcss Textual styling sheet
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_stopwatch", "Add"),
        ("r", "remove_stopwatch", "Remove"),
    ]  # This assigns buttons to actions

    def compose(self) -> ComposeResult:  # Here is where an user interface is constructed with widgets.
        """Create child widgets for the main app."""
        yield Header()  # Does what I commented on the import statement :)
        yield Footer()  # Does what I commented on the import statement :)
        yield VerticalScroll(
            StopWatch(), StopWatch(), StopWatch(), id="timers"
        )  # Adds vertical scroll when the given items don't fit

    def action_toggle_dark(
        self,
    ) -> None:  # Action method. Actions start with action_ followed by the method defined in BINDINGS.
        """Action to toggle UI dark mode"""
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"

    def action_add_stopwatch(self) -> None:
        """Action to add a new stopwatch"""
        new_stopwatch = StopWatch()  # Create the new component
        self.query_one("#timers").mount(new_stopwatch)  # Mount the new component to the widget with id=timers
        new_stopwatch.scroll_visible()  # Move view to where the new stopwatch is

    def action_remove_stopwatch(self) -> None:
        """Removes a stopwatch"""
        timers = self.query("StopWatch")  # Search for all StopWatch items, return iterable (?)
        if timers:
            timers.last().remove()  # Remove last instance of timers


if __name__ == "__main__":
    my_app = StopwatchApp()
    my_app.run()
