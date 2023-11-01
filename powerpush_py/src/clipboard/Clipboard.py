import logging
import threading

from src.common.Constant import ModuleName, Platform, MessageType
from src.common.Message import Message
from src.common.Module import Module
import win32clipboard


class Clipboard(Module):
    def __init__(self):
        super().__init__(ModuleName.CLIPBOARD)

    def run(self):
        # super().run()
        logging.info(f'Start get clipboard content ...')
        # get message from other modules
        get_clip_content = threading.Thread(self._thrd_func_get_content_from_clipboard())
        get_clip_content.start()

    def _thrd_func_get_content_from_clipboard(self):
        if self.os_type == Platform.WIN:
            type, data = self._get_win_clip()
            logging.debug(f'type: {type}, data: {data}')
            self.snd_queue_lock.acquire()
            self.snd_queue.put(Message(ModuleName.LOCAL_HUB, ModuleName.SERVER_HUB, MessageType.TEXT, data))
            self.snd_queue_lock.release()

    def _get_win_clip(self):
        win32clipboard.OpenClipboard()
        try:
            # 获取文本内容
            if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
                data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
                clipboard_type = "text/plain"

            # 获取图片内容
            elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_BITMAP):
                data = win32clipboard.GetClipboardData(win32clipboard.CF_BITMAP)
                clipboard_type = "image/bmp"

            # 获取文件内容
            elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_HDROP):
                data = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
                clipboard_type = "application/octet-stream"

            else:
                data = None
                clipboard_type = None

        except Exception as e:
            print("获取剪贴板内容出错:", e)
            data = None
            clipboard_type = None
        win32clipboard.CloseClipboard()
        return type, data

    def _get_linux_clip(self):
        pass
        # clip = QClipboard()
        # mime_data = clip.mimeData()
        # clip_data_type = mime_data.formats()[0]
        # clip_data = mime_data.data(clip_data_type)
        # return clip_data_type, clip_data
