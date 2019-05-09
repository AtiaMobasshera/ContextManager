from contextlib import contextmanager

class FileCM():
    @contextmanager
    def open_file(path, mode):
        the_file = open(path, mode)
        yield the_file
        the_file.close()

    files = []

    for x in range(100000):
        with open_file('testFile2.txt', 'w') as infile:
            infile.write('context manager Decorator test file')
            files.append(infile)

    for f in files:
        if not f.closed:
            print('not closed')


if __name__ == "__main__":
    FileCM()

