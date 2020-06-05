import argparse
from .new_module import PrintingClass


def new_function2(maybe_or_not):
    print("Hear I come")


def new_cool_subfuntion_for_printing(what_to_print):
    pc = PrintingClass("Coming from app.new_cool_subfuntion_for_printing", what_to_print)
    pc.print()


def new_function(args=None):
    new_cool_subfuntion_for_printing(args)
    new_function2(args)


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
