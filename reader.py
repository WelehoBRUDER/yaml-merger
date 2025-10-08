import os
import time

from rich.pretty import pprint

from conf import read_config


class YamlReader:
    def __init__(self):
        items = read_config()
        self.read_directory = items["read_directory"]
        self.write_directory = items["write_directory"]
        self.sort_files = items["sort_files"] == "True"
        self.search_depth = int(items["search_depth"])
        self.files = {}
        self.elapsed = 0
        self.file_count = 0
        self.directory_count = -1

    def get_elapsed(self):
        return f"{self.elapsed:.4f}s"

    def read_all(self):
        start_time = time.perf_counter()
        self.files["dirs"] = {}
        self.files["files"] = []
        self.files = self.read_directory_to_object(self.read_directory, 1)
        self.elapsed = time.perf_counter() - start_time
        print(f"Found {self.file_count} YAML files in {self.directory_count} folders.")

    def read_directory_to_object(self, path, depth):
        if depth > self.search_depth:
            print("Search depth reached! Aborting search.")
            return None
        obj = {"dirs": {}, "files": []}
        self.directory_count += 1
        print(f"Reading directory {path}...")
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path) and entry.endswith(".yaml"):
                self.file_count += 1
                obj["files"].append(entry)
            elif os.path.isdir(full_path):
                obj["dirs"][entry] = self.read_directory_to_object(full_path, depth + 1)
        return obj
