from merger import YamlMerger
from reader import YamlReader


def main():
    reader = YamlReader()
    reader.read_all()
    merger = YamlMerger(reader.files)
    merger.merge_files_test()
    print(f"Merge complete! Merged a total of {reader.file_count} yaml files.")
    print(
        f"Took {(reader.elapsed + merger.elapsed):.4f}s in total (read {reader.get_elapsed()}, merge {merger.get_elapsed()})")


if __name__ == '__main__':
    main()
