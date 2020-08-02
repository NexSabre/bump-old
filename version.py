class Version:
    def __init__(self):
        self.major: int = 0
        self.minor: int = 0
        self.patch: int = 0
        self.additinal: string = None
        self.build: int = 0

        self._list_version = self.list_version()
        self._len_version: int = None

    def list_version(self):
        return [self.major, self.minor, self.patch, self.additinal, self.build]

    def read_version_file(self):
        with open('VERSION', 'r') as version_file: 
            ver_information = version_file.read().split('.')
            self._len_version = len(ver_information)

            for i, v in enumerate(ver_information):
                self._list_version[i] = v

    def __str__(self):
        types = []
        for i in self._len_version:
            types.append(self.list_version[i])
        return '.'.join(types)


if __name__ == "__main__":
    v = Version().read_version_file()
