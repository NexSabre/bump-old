from typing import Any, AnyStr

import os


class Version:
    def __init__(self) -> None:
        self.major: int = 0
        self.minor: int = 0
        self.path: int = 0

    def minor_bump():
        pass

    def patch_bump():
        pass


class Bump:
    def __init__(self, filepath=None) -> None:
        self.filepath: AnyStr = None
        self.version: AnyStr = None

    def __call__(self, *args, **kwargs) -> Any:
        self.__find_version()
        self.__open_version_file()

    def __find_version(self):
        listdir = os.listdir(os.path.dirname(os.path.realpath(__file__)))
        if "VERSION" in listdir:
            self.filepath = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "VERSION")

    def __open_version_file(self):
        with open(self.filepath, "w") as f:
            file_version = f.read()



if __name__ == "__main__":
    bump = Bump()
    bump()

    