from sys import version
from typing import Any, AnyStr, List

import os


class Version:
    def __init__(self, raw: AnyStr) -> None:
        self.raw: AnyStr = raw
        self.raw_list: List[Any] = []
        self.major: int = None
        self.minor: int = None
        self.patch: int = None

        self.__resolve_from_raw()

    def __str__(self) -> str:
        return f"Version {self.major}.{self.minor}.{self.patch}"

    def __resolve_from_raw(self):
        self.raw_list = self.raw.split(".")
        len_of_version = len(self.raw_list)

        if len_of_version == 1:
            self.major = int(self.raw_list[0])
        elif len_of_version == 2:
            self.major = int(self.raw_list[0])
            self.minor = int(self.raw_list[1])
        elif len_of_version == 3:
            self.major = int(self.raw_list[0])
            self.minor = int(self.raw_list[1])
            self.patch = int(self.raw_list[2])

    def minor_bump(self):
        self.minor += 1

    def patch_bump(self):
        self.patch += 1


class Bump:
    def __init__(self, filepath: AnyStr = None) -> None:
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
        with open(self.filepath) as f:
            self.version = f.read()


def reset_version(version: AnyStr = "0.1"):
    with open("VERSION", "w") as version_file:
        version_file.write(version)


if __name__ == "__main__":
    reset_version()
    bump = Bump()
    bump()
    version = Version(raw=bump.version)
    assert version.raw == "0.1"

    assert version.major == 0
    assert version.minor == 1

    # bump minor
    version.minor_bump()
    assert version.minor == 2
