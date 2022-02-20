# decorator


def copyright(func):
    def new_func():
        print("copyright")
        func()

    return new_func()


@copyright
def smile():
    print("smiley face")


@copyright
def angry():
    print("angry face")


@copyright
def love():
    print("lovely face")


@copyright
def poo():
    print("poo")


@copyright
def hate():
    print("hate face")


@copyright
def dog():
    print("dog face")


@copyright
def one():
    print("one")


@copyright
def two():
    print("two")


@copyright
def three():
    print("three")


@copyright
def four():
    print("four")


@copyright
def five():
    print("five")


@copyright
def six():
    print("six")


@copyright
def seven():
    print("seven")


@copyright
def eight():
    print("eight")


@copyright
def nine():
    print("nine")


@copyright
def ten():
    print("ten")


@copyright
def eleven():
    print("eleven")
