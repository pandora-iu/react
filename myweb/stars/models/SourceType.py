from enum import Enum


class SourceType(Enum):
    UPLOAD = "UPLOAD"
    YOUTUBE = "YOUTUBE"
    URL = "URL"

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, SourceType):
            return self.value == other.value
        else:
            return self == SourceType(other)

    def __get__(self, instance, owner):
        return instance.value

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    @classmethod
    def choices(cls):
        return list(map(lambda x: (x.value, x.value), cls))