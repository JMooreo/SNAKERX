class ConsoleOutput:
    def write_line(self, line):
        print(line)

class FileOutput:
    def __init__(self, fileName):
        self.file = open(fileName, "w")

    def write_line(self, line):
        self.file.write(f"{line}\n")