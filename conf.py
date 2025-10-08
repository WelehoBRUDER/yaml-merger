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