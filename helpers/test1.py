import numpy as np
import time
import matplotlib.pyplot as plt

class LivePlot:
    def __init__(self, max_angle_degrees: float, max_range_m: float):
        # max_angle_degrees: maximum supported speed
        # max_range_m:   maximum supported range
        self.h = None
        self.max_angle_degrees = max_angle_degrees
        self.max_range_m = max_range_m

        plt.ion()

        self._fig, self._ax = plt.subplots(nrows=1, ncols=1)

        self._fig.canvas.manager.set_window_title("Range-Angle-Map using Digital Beam Forming")
        self._fig.canvas.mpl_connect('close_event', self.close)
        self._is_window_open = True

    def _draw_first_time(self, data: np.ndarray):
        # First time draw

        minmin = -60
        maxmax = 0

        self.h = self._ax.imshow(
            data,
            vmin=minmin, vmax=maxmax,
            cmap='viridis',
            extent=(-self.max_angle_degrees,
                    self.max_angle_degrees,
                    0,
                    self.max_range_m),
            origin='lower')

        self._ax.set_xlabel("angle (degrees)")
        self._ax.set_ylabel("distance (m)")
        self._ax.set_aspect("auto")

        self._fig.subplots_adjust(right=0.8)
        cbar_ax = self._fig.add_axes([0.85, 0.0, 0.03, 1])

        cbar = self._fig.colorbar(self.h, cax=cbar_ax)
        cbar.ax.set_ylabel("magnitude (a.u.)")

    def _draw_next_time(self, data: np.ndarray):
        # Update data for each antenna

        self.h.set_data(data)

    def draw(self, data: np.ndarray, title: str):
        if self._is_window_open:
            if self.h:
                self._draw_next_time(data)
            else:
                self._draw_first_time(data)
            self._ax.set_title(title)

            self._fig.canvas.draw_idle()
            self._fig.canvas.flush_events()

    def close(self, event=None):
        if not self.is_closed():
            self._is_window_open = False
            plt.close(self._fig)
            plt.close('all')
            print('Application closed!')

    def is_closed(self):
        return not self._is_window_open


# Sample usage of the LivePlot class
class RadarSimulator:
    def __init__(self, max_angle_degrees, max_range_m):
        self.max_angle_degrees = max_angle_degrees
        self.max_range_m = max_range_m
        self.live_plot = LivePlot(max_angle_degrees, max_range_m)

    def simulate_data(self, duration_sec=10, update_interval_sec=0.1):
        # Simulate radar data and update the live plot

        # Number of points in angle and range
        num_points_angle = 64
        num_points_range = 256

        # Create an initial data matrix
        data_matrix = np.random.random((num_points_range, num_points_angle)) * 60 - 60

        # Simulate radar data for a duration
        start_time = time.time()
        while time.time() - start_time < duration_sec and not self.live_plot.is_closed():
            # Generate random data for simulation
            data_matrix = np.random.random((num_points_range, num_points_angle)) * 60 - 60

            # Get current time for the title
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            title = f"Radar Simulation\n{current_time}"

            # Update the live plot
            self.live_plot.draw(data_matrix, title)

            # Wait for the specified interval
            time.sleep(update_interval_sec)

if __name__ == "__main__":
    # Create a radar simulator with specified maximum angle and range
    radar_simulator = RadarSimulator(max_angle_degrees=180, max_range_m=100)

    # Start the simulation
    radar_simulator.simulate_data()
