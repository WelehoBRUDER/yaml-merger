import os

def get_dir_name(path):
    print(path)
    dirs = os.path.split(path)
    return dirs[len(dirs) - 1]

def get_name(filename):
    return filename.split('.')[0]

class YamlMerger:
    def __init__(self, files, read_dir, write_dir):
        self.files = files
        self.read_dir = read_dir
        self.write_dir = write_dir

    def merge_files(self):
        path = self.write_dir + f"\\{get_dir_name(self.read_dir)}.yaml"
        merged = open(path, "w")
        for filename in self.files:
            file = open(self.read_dir + "\\" + filename, "r")
            merged.write(f"{get_name(filename)}:\n")
            for line in file:
                merged.write(f"  {line}")
            file.close()

        merged.close()
