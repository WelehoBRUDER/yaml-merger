import os
import time


def get_dir_name(path):
    dirs = os.path.split(path)
    return dirs[len(dirs) - 1]


def get_name(filename):
    return filename.split('.')[0]


class YamlMerger:
    def __init__(self, files, read_dir, write_dir):
        self.files = files
        self.read_dir = read_dir
        self.write_dir = write_dir
        self.elapsed = 0

    def get_elapsed(self):
        return f"{self.elapsed:.4f}s"

    def merge_files(self):
        start_time = time.perf_counter()
        path = self.write_dir + f"\\{get_dir_name(self.read_dir)}.yaml"
        merged = open(path, "w")
        for index, filename in enumerate(self.files):
            file = open(self.read_dir + "\\" + filename, "r")
            merged.write(f"{get_name(filename)}:\n")
            for line in file:
                merged.write(f"  {line}")
            file.close()
            print(f"Merged {index + 1}/{len(self.files)} ({filename})")

        print(f"Complete! Merged {len(self.files)} files to {get_dir_name(self.read_dir)}.yaml");
        self.elapsed = time.perf_counter() - start_time
        merged.close()
