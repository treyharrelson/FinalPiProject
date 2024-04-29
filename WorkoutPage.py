import tkinter as tk
import time

# This class contains the functions for the stopwatch that
# is present on each page. It was created to prevent repetitive
# code.
class WorkoutPage:

    def __init__(self, root = None):
        self.root = root

    def run_stop_watch(self):
        start_time = time.time()
        global running; running = True

        while running:
            elapsed_time = time.time() - start_time
            minute, second = (elapsed_time // 60, elapsed_time % 60)
            second = f"{second:05.2f}"
            minute = int(minute)
            minute = f"{minute:02d}"

            self.displayed_time.set(f"{minute}:{second}")

            # update the time
            self.root.update()
            time.sleep(.01)

    def stop_stop_watch(self):
        global running; running = False

    def reset_stop_watch(self):
        self.displayed_time.set('00:00.00')

    
