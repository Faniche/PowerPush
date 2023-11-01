from strenum import StrEnum


class ModuleName(StrEnum):
    LOCAL_HUB = 'LOCAL_HUB'
    SERVER_HUB = 'SERVER_HUB'
    CLIPBOARD = 'CLIPBOARD'
    MESSAGE_DISPATCHAR = 'MESSAGE_DISPATCHAR'

    def __str__(self):
        return format(self.value)


class Platform(StrEnum):
    WIN = 'Windows'
    LINUX = 'Linux'
    MAC_OS = 'Darwin'

    def __str__(self):
        return format(self.value)


class MessageType(StrEnum):
    HEART_ATTACK = 'HEART_ATTACK'
    TEXT = 'TEXT'

    def __str__(self):
        return format(self.value)
