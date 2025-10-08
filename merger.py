import os
import time
import yaml
import json
from pathlib import Path

from conf import read_config


def get_dir_name(path):
    dirs = os.path.split(path)
    return dirs[len(dirs) - 1]


def get_name(filename):
    return filename.split('.')[0]


class YamlMerger:
    def __init__(self, files):
        items = read_config()
        self.files = files
        self.read_dir = items["read_directory"]
        self.write_dir = items["write_directory"]
        self.convert_to_JSON = items["convert_to_JSON"] == "True"
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

        print(f"Complete! Merged {len(self.files)} files to {get_dir_name(self.read_dir)}.yaml")
        if self.convert_to_JSON:
            merged.close()
            merged = open(path, "r")
            Path(self.write_dir + "\\json").mkdir(parents=True, exist_ok=True)
            json_path = self.write_dir + f"\\json\\{get_dir_name(self.read_dir)}.json"
            converted = open(json_path, "w")
            yaml_object = yaml.safe_load(merged)
            json.dump(yaml_object, converted)
            print(f"Conversion complete! {get_dir_name(self.read_dir)}.yaml --> {get_dir_name(self.read_dir)}.json")
        self.elapsed = time.perf_counter() - start_time
        merged.close()
