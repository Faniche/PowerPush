from src.clipboard.Clipboard import Clipboard
from src.common.Beehive import Beehive


def exec():
    local_hub = Beehive()
    local_hub.modules.append(Clipboard())



    local_hub.run()