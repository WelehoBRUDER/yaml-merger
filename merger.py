import os
import time
import yaml
import json
from pathlib import Path

from rich.pretty import pprint

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
        self.fails = 0

    def get_elapsed(self):
        return f"{self.elapsed:.4f}s"

    def merge_files_test(self):
        start_time = time.perf_counter()
        print(f"\033[92mSTARTING MERGE PROCESS -> '{self.read_dir}")
        self.merge_files_recursively(self.files, "", "")
        self.elapsed = time.perf_counter() - start_time
        if self.fails > 0:
            print(f"\033[93mWARNING! THERE WERE {self.fails} ERRORS DURING THE MERGE PROCESS!\033[0m")

    def merge_files_recursively(self, obj, path, name):
        for directory in obj["dirs"]:
            self.merge_files_recursively(obj["dirs"][directory], f"{path}\\{directory}", directory)
        if len(obj["files"]) > 0:
            file_count = len(obj["files"])
            current_path = f"{self.write_dir}\\{path}"
            Path(current_path).mkdir(parents=True, exist_ok=True)
            merged = open(f"{current_path}\\{name}.yaml", "w")
            for index, filename in enumerate(obj["files"]):
                line_index = 1
                try:
                    file = open(f"{self.read_dir}\\{path}\\{filename}", "r")
                    merged.write(f"{get_name(filename)}:\n")
                    for line in file:
                        merged.write(f"  {line}")
                        line_index += 1
                    file.close()
                except Exception:
                    print(f"\033[91mERROR! FAILED TO MERGE {filename}")
                    print(f"\033[91mTHE ERROR OCCURED ON LINE {line_index}")
                    print(f"Path to file -> {self.read_dir}\\{path}\\{filename}\033[92m")
                    self.fails += 1
                print(f"Merged {index + 1}/{file_count} ({filename})")
            if self.convert_to_JSON:
                print(f"\033[96mStarting to convert {name}.yaml to JSON...")
                merged.close()
                merged = open(f"{current_path}\\{name}.yaml", "r")
                json_path = f"{current_path}\\{name}.json"
                converted = open(json_path, "w")
                yaml_object = yaml.safe_load(merged)
                json.dump(yaml_object, converted)
                print(f"Conversion complete! {name}.yaml --> {name}.json\033[92m")
            merged.close()