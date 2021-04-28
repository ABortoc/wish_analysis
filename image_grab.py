from PIL import ImageGrab
import datetime
import threading
import ctypes
import win32api
import win32gui
import sys
import keyboard

# Image is cropped based on 2560x1440 screen resolution with hard-coded values.
# Other resolutions will require different values. Can add another function argument that
# will indicate which resolution is being used allowing for if/else statement with proper
# crop values. Creates a text file with names of the images for batch processing.


def image_grab_crop(num):
    img = ImageGrab.grabclipboard()
    img_cropped = img.crop((216, 361, 2322, 1196))
    img_cropped.save(f'screenshots/scr_{num}.png', 'PNG')
    with open('screenshots/screenshots.txt', 'a') as file:
        file.write(f'screenshots/scr_{num}.png\n')


# Code taken from https://abdus.dev/posts/monitor-clipboard/
# Used to monitor clipboard changes
class Clipboard:
    def _create_window(self) -> int:
        """
        Create a window for listening to messages
        :return: window hwnd
        """
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self._process_message
        wc.lpszClassName = self.__class__.__name__
        wc.hInstance = win32api.GetModuleHandle(None)
        class_atom = win32gui.RegisterClass(wc)
        return win32gui.CreateWindow(class_atom, self.__class__.__name__, 0, 0, 0, 0, 0, 0, 0, wc.hInstance, None)

    def _process_message(self, hwnd: int, msg: int, wparam: int, lparam: int):
        WM_CLIPBOARDUPDATE = 0x031D
        if msg == WM_CLIPBOARDUPDATE:
            now = datetime.datetime.now()
            current_time = now.strftime('%H_%M_%S')
            image_grab_crop(current_time)
        return 0

    def listen(self):
        def runner():
            hwnd = self._create_window()
            ctypes.windll.user32.AddClipboardFormatListener(hwnd)
            win32gui.PumpMessages()

        th = threading.Thread(target=runner, daemon=True)
        th.start()
        is_alive = True
        while is_alive:
            if keyboard.is_pressed('p'):
                is_alive = False
            th.join(0.5)


def clipboard_listen():
    clipboard = Clipboard()
    clipboard.listen()


# clipboard_listen()
