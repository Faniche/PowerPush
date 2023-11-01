import unittest

from config.log_conf import setup_logger
from src.clipboard.Clipboard import Clipboard


class TestClipboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        setup_logger()

    def test_text_paste(self):
        clip = Clipboard()
        clip.start()
        # clip.run()