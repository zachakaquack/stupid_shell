import enum


class StatusCode(enum.Enum):
    EXIT = -1  # exit
    OKAY = 0  # continue shell
    ERROR = 1  # kill entire shell
