# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

def run(minutes: int = 0.1):
    start = time.time()
    delta_2 = -1
    while True:  # Press Ctrl+F8 to toggle the breakpoint.
        delta = time.time() - start
        if delta_2 != -1:
            if int(delta) != int(delta_2):
                print(delta)
        if delta > minutes * 60:
            break

        delta_2 = delta
