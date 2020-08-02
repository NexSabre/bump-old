class Version:
    def __init__(self):
        self.major: int = 0
        self.minor: int = 0
        self.patch: int = 0
        self.additinal: str = None
        self.build: int = 0

        self._list_version = self.list_version()
        self._len_version: int = None

    def list_version(self):
        return [self.major, self.minor, self.patch, self.additinal, self.build]

    def read_version_file(self):
        try:
            with open('VERSION', 'r') as version_file: 
                ver_information = version_file.read().split('.')
                self._len_version = len(ver_information)

                for i, v in enumerate(ver_information):
                    self._list_version[i] = v
        except FileNotFoundError as error:
            print(error)

    def __str__(self):
        types = []
        for i in range(self._len_version):
            types.append(self._list_version[i])
        return '.'.join(types)

    def save_to_file(self, filename: str = 'VERSION'):
        with open(filename, 'w') as version_file:
            version_file.write(self.__str__())

if __name__ == "__main__":
    v = Version()
    v.
    
    ()
    v.save_to_file()
    print(v)
