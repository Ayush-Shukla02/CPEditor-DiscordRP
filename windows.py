import psutil
import win32gui
import os

win = win32gui


def open_app(app: str) -> None:
    os.startfile("C:\Program Files (x86)\cpeditor\cpeditor.exe")


def is_running() -> bool:
    f = "cpeditor.exe" in (p.name() for p in psutil.process_iter())
    return f


def get_front_window_name(app: str) -> str:
    title = win.GetWindowText(win.GetForegroundWindow())
    return title[-9:]
