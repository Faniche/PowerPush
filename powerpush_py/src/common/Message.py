from src.common.Constant import MessageType, ModuleName


class Message:
    def __init__(self, src_module_name: ModuleName, dst_module_name: ModuleName, type: MessageType = MessageType.HEART_ATTACK, content: str = None):
        self.src_module_name = src_module_name
        self.dst_module_name = dst_module_name
        self.type = type
        self.content = content

