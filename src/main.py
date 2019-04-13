from src.seq import stern_brocot


@profile
def print_sequence():
    for x in stern_brocot(10):
        print(x)


print_sequence()
