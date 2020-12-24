class Matrix:
    def __init__(self, matrix_string):
        new_line = len(matrix_string[:matrix_string.find("\n")].split())
        self.width = new_line if new_line else 1
        self.value = [int(i) for i in matrix_string.split()]

    def row(self, index):
        return self.value[self.width * (index - 1): self.width * index]

    def column(self, index):
        return [self.value[i] for i in range(len(self.value)) if i % self.width == index - 1]
