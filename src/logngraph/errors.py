__all__ = [
    "InvalidArgsError",
    "FeatureNotInstalledError",
    "InvalidKeyError",
]


class InvalidArgsError(Exception):
    def __init__(self, message):
        super().__init__(message)

class FeatureNotInstalledError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidKeyError(Exception):
    def __init__(self, message):
        super().__init__(message)
