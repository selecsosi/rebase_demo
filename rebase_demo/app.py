import argparse
import os
import sys


def new_function(args):
    print("Hello")
    print(args)
    print(f"PythonPath: {sys.path}")


def app():
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=str,
                        help="value to display")
    parser.add_argument("-v", "--verbosity", action="count",
                        help="increase output verbosity")
    args = parser.parse_args()
    new_function(args)


if __name__ == "__main__":
    app()
