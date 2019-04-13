from src.seq import stern_brocot


@profile
def print_sequence():
    for x in stern_brocot():
        print(x)


print_sequence()
