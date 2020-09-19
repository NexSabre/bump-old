from argparse import ArgumentTypeError, PARSER


class Version:
    def __init__(self, potential_version: str = None):
        self.major: int = 0
        self.minor: int = 0
        self.patch: int = 0
        self.additinal: str = None
        self.build: int = 0

        self._list_version = self.list_version()
        self._len_version: int = None

        if potential_version:
            set_version(potential_version)

    def set_version(self, potential_v) -> None:
        version = potential_v.split('.')
        for element in len(version):
            if element >= 1:
                self.major = version(element)
            elif element >= 2:
                self.minor = version(element)
            elif element >= 3:
                self.patch = version(element)

    def list_version(self):
        return [self.major, self.minor, self.patch, self.additinal, self.build]

    def __str__(self):
        types = []
        for i in range(self._len_version):
            try:
                types.append(self._list_version[i])
            except TypeError:
                continue
        return '.'.join(types)

    def save_to_file(self, filename: str = 'VERSION'):
        with open(filename, 'w') as version_file:
            version_file.write(self.__str__())

    def read_version_file(self):
        try:
            with open('VERSION', 'r') as version_file: 
                ver_information = version_file.read().split('.')
                self._len_version = len(ver_information)

                for i, v in enumerate(ver_information):
                    self._list_version[i] = v
        except FileNotFoundError as error:
            print(error)

def check_version(potential_value: str):
    if not potential_value:
        return potential_value
    try:
        version = Version(potential_value.split('.'))
    except:
        raise ArgumentTypeError
    return potential_value

if __name__ == "__main__":
    import argparse
    argument_parser = argparse.ArgumentParser("Bump action")
    argument_parser.add_argument('--set-version', type=check_version, help="Set specific version", default=None)

    args = argument_parser.parse_args()
    v = Version(potential_version=args.set_version)
    # v.list_version()

    print(v)
