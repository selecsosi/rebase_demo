import sys


class PrintingClass:

    def __init__(self, message, args=None):
        self.message = message
        self.args = args

    def print(self):
        print("Hello from printing class")
        print(f"This was my message: {self.message}")
        print(f"PythonPath: {sys.path}")
