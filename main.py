from merger import YamlMerger
from reader import YamlReader


def main():
    reader = YamlReader()
    files = reader.read_files()
    merger = YamlMerger(files)
    merger.merge_files()
    print(
        f"Took {(reader.elapsed + merger.elapsed):.4f}s in total (read {reader.get_elapsed()}, merge {merger.get_elapsed()})")


if __name__ == '__main__':
    main()
