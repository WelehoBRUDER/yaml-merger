from merger import YamlMerger
from reader import YamlReader


def main():
    reader = YamlReader()
    files = reader.read_files()
    merger = YamlMerger(files, reader.read_directory, reader.write_directory)
    merger.merge_files()


if __name__ == '__main__':
    main()
