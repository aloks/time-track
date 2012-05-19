import win32gui
import time


def getForegroundWindowTitle():
    foreground = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(foreground)
    return title


if __name__ == '__main__':
    while 1:
	print getForegroundWindowTitle()
	time.sleep(4)

