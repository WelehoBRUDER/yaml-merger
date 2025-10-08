import os
import time

from conf import read_config


class YamlReader:
    def __init__(self):
        items = read_config()
        self.read_directory = items["read_directory"]
        self.write_directory = items["write_directory"]
        self.sort_files = items["sort_files"] == "True"
        self.files = []
        self.elapsed = 0

    def get_elapsed(self):
        return f"{self.elapsed:.4f}s"

    def read_files(self):
        start_time = time.perf_counter()
        self.files = []
        for file in os.listdir(self.read_directory):
            if file.endswith(".yaml"):
                self.files.append(file)
        print(f"Found {len(self.files)} YAML files in {self.read_directory}.")
        if self.sort_files:
            self.files.sort()
        self.elapsed = time.perf_counter() - start_time
        return self.files
