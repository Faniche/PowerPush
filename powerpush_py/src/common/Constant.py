from enum import Enum


class ModuleName(str, Enum):
    LOCAL_HUB = 'LOCAL_HUB'
    SERVER_HUB = 'SERVER_HUB'
    CLIPBOARD = 'CLIPBOARD'
    MESSAGE_DISPATCHAR = 'MESSAGE_DISPATCHAR'


class Platform(str, Enum):
    WIN = 'Windows'
    LINUX = 'Linux'
    MAC_OS = 'Darwin'


class MessageType(Enum):
    HEART_ATTACK = 'HEART_ATTACK'
