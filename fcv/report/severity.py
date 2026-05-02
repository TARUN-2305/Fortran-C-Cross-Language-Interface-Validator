import enum

class Severity(enum.Enum):
    ERROR = 3
    WARNING = 2
    INFO = 1

    def __str__(self):
        return self.name
