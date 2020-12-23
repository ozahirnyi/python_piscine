import pandas


class FileLoader:
    file_data = pandas.DataFrame
    columns = 0
    lines = 0

    def __init__(self, path):
        self.path = path

    def load(self):
        self.file_data = pandas.read_csv(self.path)
        self.lines = len(self.file_data)
        self.columns = self.file_data.shape[1]

    @staticmethod
    def display(df, n):
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(n * -n))
