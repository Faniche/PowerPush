from src.common.Constant import ModuleName
from src.common.Module import Module


class MessageDispatcher(Module):
    def __init__(self):
        super().__init__(ModuleName.MESSAGE_DISPATCHAR)