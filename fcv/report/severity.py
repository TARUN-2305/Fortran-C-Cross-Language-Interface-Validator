import enum

class Severity(str, enum.Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"

    def __str__(self):
        return self.value
