# Get the time for tracking the amount of time passes between functions
import time


def time_at_now(thetime):
    now = time.time()
    print("completed function: ", round(now - thetime, 2), " seconds\n")
