import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QMainWindow
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtCore import Qt, QRectF, QSize, Signal


class CustomSlider(QSlider):
    sectionNotAvailable = Signal()  # Signal emitted when clicking on a red section
    sliderMovedWithTime = Signal(int)  # Signal emitted with the current time in ms

    def __init__(self, orientation=Qt.Horizontal, played_color="green", unplayed_color="lightgreen",
                 played_red_color="red", unplayed_red_color="lightcoral", show_dividers=False,
                 groove_height=10, time_label=None, parent=None):
        super().__init__(orientation, parent)
        self.segments = []  # List of tuples (start, end, color) normalized between 0 and 1
        self.played_color = played_color
        self.unplayed_color = unplayed_color
        self.played_red_color = played_red_color
        self.unplayed_red_color = unplayed_red_color
        self.show_dividers = show_dividers
        self.groove_height = groove_height  # Height of the background (timeline)
        self.time_label = time_label  # Optional QLabel to display time
        self.setTracking(True)  # Track slider movements continuously

        # Disable the default groove and handle styles
        self.setStyleSheet("""
            QSlider::groove:horizontal { background: transparent; }
            QSlider::handle:horizontal { background: transparent; }
        """)

    def set_segments(self, segments):
        self.segments = segments
        self.update()

    def mousePressEvent(self, event):
        """Handle mouse press events to check if the clicked section is green or red."""
        click_position = event.position().x()
        slider_width = self.width()
        self.setSliderDown(True)  # Ensure slider is in 'down' state

        # Convert click position to a normalized value (0 to 1)
        normalized_position = click_position / slider_width

        # Check if the clicked position falls into a red or green section
        for start, end, color in self.segments:
            if start <= normalized_position <= end:
                if color == "red":
                    self.sectionNotAvailable.emit()  # Emit the signal for unavailable section
                    self.setSliderDown(False)  # Reset slider down state
                    return  # Ignore the click and prevent slider from moving
                elif color == "green":
                    # Update the slider value to the clicked position
                    self.setValue(int(normalized_position * self.maximum()))
                    self.emit_time_update()  # Emit the signal with current time
                    return  # Stop after handling the green section

        # If not in any section, continue with the default behavior
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """Limit slider movement to green sections only."""
        if event.buttons() & Qt.LeftButton:
            click_position = event.position().x()
            slider_width = self.width()

            # Convert click position to a normalized value (0 to 1)
            normalized_position = click_position / slider_width

            # Check if the slider handle should be allowed to move to this position
            for start, end, color in self.segments:
                if start <= normalized_position <= end and color == "green":
                    # Move to the exact start of the segment if close enough to it
                    if abs(normalized_position - start) < (1 / slider_width):
                        normalized_position = start
                    # Move to the exact end of the segment if close enough to it
                    elif abs(normalized_position - end) < (1 / slider_width):
                        normalized_position = end

                    # Set the value based on the normalized position
                    self.setValue(int(normalized_position * self.maximum()))
                    self.emit_time_update()  # Emit the signal with current time
                    return  # Allow movement within the green section

        # Ignore movement if outside green sections
        event.ignore()

    def mouseReleaseEvent(self, event):
        """Handle the mouse release event to finalize the movement."""
        if event.button() == Qt.LeftButton:
            self.setSliderDown(False)
            self.emit_time_update()  # Emit the signal with current time
        super().mouseReleaseEvent(event)

    def leaveEvent(self, event):
        """Handle the event when the mouse leaves the slider area."""
        self.setSliderDown(False)  # Stop dragging the slider when the mouse leaves
        super().leaveEvent(event)

    def emit_time_update(self, emit=True):
        """Emit the current time in milliseconds and update the label if provided."""
        current_time_ms = self.value()

        if emit:
            self.sliderMovedWithTime.emit(current_time_ms)

        # Update the QLabel if provided
        if self.time_label:
            self.time_label.setText(self.ms_to_time(current_time_ms))

    @staticmethod
    def ms_to_time(ms):
        """Convert milliseconds to a formatted time string (HH:MM:SS)"""
        seconds = ms // 1000
        minutes = seconds // 60
        hours = minutes // 60
        return f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the slider groove with segments as background
        self.draw_slider_background(painter)

        # Draw the custom handle
        self.draw_handle(painter)

    def draw_slider_background(self, painter):
        """Draw the background of the slider with segments"""
        groove_rect = self.rect()
        groove_x = groove_rect.x()
        groove_width = groove_rect.width()
        groove_height = self.groove_height  # Use the customizable groove height

        # Center the groove vertically
        groove_y = groove_rect.y() + (groove_rect.height() - groove_height) // 2

        # Get the current position of the slider as a normalized value (0 to 1)
        current_position = self.value() / self.maximum() if self.maximum() != 0 else 0

        for segment in self.segments:
            start, end, color = segment

            # Determine the colors for played and unplayed segments based on input colors
            if color == "green":
                played_color = QColor(self.played_color)
                unplayed_color = QColor(self.unplayed_color)
            else:
                played_color = QColor(self.played_red_color)
                unplayed_color = QColor(self.unplayed_red_color)

            # Draw played part with the original color
            if start < current_position:
                played_end = min(end, current_position)
                start_x = groove_x + int(start * groove_width)
                end_x = groove_x + int(played_end * groove_width)
                rect = QRectF(start_x, groove_y, end_x - start_x, groove_height)
                painter.setBrush(played_color)
                painter.setPen(Qt.NoPen)  # Remove borders
                painter.drawRect(rect)

            # Draw unplayed part with a lighter color
            if end > current_position:
                unplayed_start = max(start, current_position)
                start_x = groove_x + int(unplayed_start * groove_width)
                end_x = groove_x + int(end * groove_width)
                rect = QRectF(start_x, groove_y, end_x - start_x, groove_height)
                painter.setBrush(unplayed_color)
                painter.setPen(Qt.NoPen)  # Remove borders
                painter.drawRect(rect)

            # Optionally draw dividers between segments
            if self.show_dividers and end > start:
                painter.setPen(QColor("black"))
                divider_x = groove_x + int(end * groove_width)
                painter.drawLine(divider_x, groove_y, divider_x, groove_y + groove_height)

    def draw_handle(self, painter):
        """Draw the custom handle"""
        # Get the current position of the handle in pixels
        handle_pos = self.value() / self.maximum() * self.width()

        # Define the handle rectangle
        handle_rect = QRectF(handle_pos - 6, (self.height() - 16) / 2, 12, 16)

        # Draw the handle (a rounded rectangle)
        painter.setBrush(QBrush(Qt.white))
        painter.setPen(QPen(QColor("#888888"), 2))
        painter.drawRoundedRect(handle_rect, 4, 4)  # 4px radius for rounded corners

    def sizeHint(self):
        # Adjust the height of the slider for better visibility of the segments and handle
        return QSize(200, self.groove_height + 20)  # Increase height for handle and groove


class TimelineSlider(QWidget):
    def __init__(self, duration_ms, played_color="green", unplayed_color="lightgreen",
                 played_red_color="red", unplayed_red_color="lightcoral", show_dividers=False,
                 groove_height=10, time_label=None, parent=None):
        super().__init__(parent)
        self.duration_ms = duration_ms
        self.signals_blocked = False  # To track if signals are blocked

        # Create the custom slider with the input colors, divider option, and groove height
        self.slider = CustomSlider(Qt.Horizontal, played_color, unplayed_color, played_red_color,
                                   unplayed_red_color, show_dividers, groove_height, time_label)
        self.slider.setRange(0, duration_ms)
        self.slider.sliderMovedWithTime.connect(self.slider_moved_with_time)

        # Connect the signal for unavailable sections
        self.slider.sectionNotAvailable.connect(self.handle_section_not_available)

        # Add the slider to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def slider_moved_with_time(self, current_time_ms):
        """When the slider is moved, handle the current time in ms"""
        if not self.signals_blocked:  # Only emit if signals are not blocked
            print(f"Slider moved to time: {current_time_ms} ms")

    def set_minutes_segments(self, minutes_list):
        """Set green segments based on a list of minutes, other parts will be red"""
        segments = []
        total_minutes = self.duration_ms // (60 * 1000)  # Total duration in minutes

        for i in range(total_minutes):
            start = i / total_minutes
            end = (i + 1) / total_minutes
            color = "green" if i in minutes_list else "red"
            segments.append((start, end, color))

        self.slider.set_segments(segments)

    def set_hours_segments(self, hours_list):
        """Set green segments based on a list of hours, other parts will be red"""
        segments = []
        total_hours = self.duration_ms // (3600 * 1000)  # Total duration in hours

        for i in range(total_hours):
            start = i / total_hours
            end = (i + 1) / total_hours
            color = "green" if i in hours_list else "red"
            segments.append((start, end, color))

        self.slider.set_segments(segments)

    def handle_section_not_available(self):
        """Handle the event when a red section is clicked"""
        print("This section is not available in the video.")

    def move_to_time(self, time_ms, emit_signal=True):
        """Move the slider to the given time in milliseconds.

        If emit_signal is False, the sliderMovedWithTime signal will not be emitted during this move.
        """
        # Block signals temporarily if required

        # Move the slider to the desired position
        self.slider.setValue(time_ms)

        # Manually emit the signal if required
        self.slider.emit_time_update(emit_signal)






# Define the function that prints the time received from the slider
def print_time(time_ms):
    print(f"Current slider time: {time_ms} ms")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Total duration of the timeline in milliseconds (e.g., 2 hours)
    duration_ms = 2 * 3600 * 1000  # 2 hours in milliseconds

    # Create a QLabel to display the current time
    time_label = QLabel("00:00:00")

    # Create the main window
    main_window = QMainWindow()
    main_window.setWindowTitle("Main Window with Timeline Slider")

    # Create a central widget to hold everything
    central_widget = QWidget()

    # Create the TimelineSlider and set segments
    timeline_slider = TimelineSlider(duration_ms, played_color="green", unplayed_color="#b3ffb3",
                                     played_red_color="red", unplayed_red_color="#ffcccc",
                                     show_dividers=False, groove_height=13, time_label=time_label)
    timeline_slider.set_minutes_segments([6, 30])  # Example: Set green segments for minutes 6 to 7 and 30 to 31

    # Connect the print_time function to the slider's sliderMovedWithTime signal
    timeline_slider.slider.sliderMovedWithTime.connect(print_time)
    timeline_slider.move_to_time(419000)

    # Create a layout and add the TimelineSlider and time_label
    layout = QVBoxLayout()
    layout.addWidget(timeline_slider)
    layout.addWidget(time_label)

    # Set the layout to the central widget
    central_widget.setLayout(layout)

    # Set the central widget to the main window
    main_window.setCentralWidget(central_widget)

    # Show the main window
    main_window.resize(600, 200)
    main_window.show()

    sys.exit(app.exec())
