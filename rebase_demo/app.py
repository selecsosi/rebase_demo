from .new_module import PrintingClass


def new_cool_subfuntion_for_printing(what_to_print):
    pc = PrintingClass("Coming from app.new_cool_subfuntion_for_printing", what_to_print)
    pc.print()


def new_function(args=None):
    new_cool_subfuntion_for_printing(args)


def app():
    # TODO: I know bob will be adding in the arg parsing, working on other cool function for now
    new_function()


if __name__ == "__main__":
    app()
