from pypresence import Presence
import time
import platform
from windows import *
from dotenv import load_dotenv

load_dotenv()

win = win32gui
window_name = win.GetWindowText(win.GetForegroundWindow())


def get_active_file() -> str:
    return (window_name[:-12]).split('/')[-1]


RPC = Presence(os.getenv('client_id'))

open_app("cpeditor")
RPC.connect()
st = time.time()
pf = platform.system()
RPC.update(start=st, large_image="cpeditor", state="Just Launched")

current_file = None
while True:
    if not is_running():
        print("cp-editor has been closed")
        RPC.close()
        break

    if window_name.strip() != 'New update available':
        f = get_active_file()
        if f != current_file:
            current_file = f
            RPC.update(start=st, large_image="cpeditor", details=f"Editing {f}", state="HACKERMANS")
    time.sleep(1.5)
