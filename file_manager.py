class FileManager:

    def __init__(self):
        self.names: str = "files/names.txt"
        self.shadow: str = "files/shadow1.txt"

    def load_names(self):
        results: list = []
        with open(self.names, "r") as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                results.append(line)
        return results

    def load_file(self):
        results: list = []
        with open(self.shadow, "r") as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                results.append(line)
        return results
