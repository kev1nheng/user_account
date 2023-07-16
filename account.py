class TextFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def create_file(self):
        self.file = open(self.filename, 'a')

    def write_text(self, name, account_number):
        if self.file is None:
            raise ValueError("File not created. Call create_file() method first.")
        self.file.write(name)
        self.file.write(",")
        self.file.write(account_number)
        self.file.write(",")

    def close_file(self):
        if self.file is not None:
            self.file.close()
            self.file = None


    
