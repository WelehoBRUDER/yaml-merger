import os


def read_config():
    conf = open("config.txt")
    next_line = conf.readline()
    items = {}
    while next_line:
        values = next_line.strip().split("=")
        # Value 0 is key and value 1 is data
        items[values[0]] = values[1]
        next_line = conf.readline()

    conf.close()
    return items


class YamlReader:
    def __init__(self):
        items = read_config()
        self.read_directory = items["read_directory"]
        self.write_directory = items["write_directory"]
        self.files = []

    def read_files(self):
        for file in os.listdir(self.read_directory):
            self.files.append(file)
        print(self.files)

