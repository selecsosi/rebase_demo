def new_function2(maybe_or_not):
    print("Hear I come")

def new_function(arg=None):
    new_function2(arg)


def app():
    new_function()


if __name__ == "__main__":
    app()
