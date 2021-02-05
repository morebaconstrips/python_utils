class colors:
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    END = "\033[0m"


def symmetric_group():
    Sn = int(input("Select the degree of the symmetric group: "))
    print(f"\n{colors.GREEN}Symmetric group of degree {Sn}.\n"
          f"S{Sn} = {{{str([_ for _ in range(1, Sn + 1)])[1:-1]}}}{colors.END}\n")
    return Sn


permutations = []


def permute(array, start=0):
    if start == len(array) - 1:
        permutations.append(list(array))
        return
    for i in range(start, len(array)):
        array[start], array[i] = array[i], array[start]
        permute(array, start + 1)
        array[start], array[i] = array[i], array[start]


def build_array(Sn):
    perm = []
    for i in range(1, Sn + 1):
        n = int(input(f"insert the {i}^ number: "))
        while n in perm or not 0 < n <= Sn:
            if n in perm:
                print(f"{colors.RED}Insert a number you did not use yet{colors.END}")

            if not 0 < n <= Sn:
                print(f"{colors.RED}Insert a number between 1 and {Sn}{colors.END}")

            n = int(input(f"\ninsert the {i}^ number: "))
        perm.append(n)
        print(f"\n({str([_ for _ in range(1, Sn + 1)])[1:-1]})\n"
              f"({str(perm)[1:-1]})\n")
    print(f"\n{colors.GREEN}Your permutation is: ({str(perm)[1:-1]}){colors.END}")
    return perm


def print_elements(Sn):
    array = [_ for _ in range(1, int(Sn) + 1)]
    permute(array)
    print(f"The order of the group is: {Sn}! = {len(permutations)}\n")
    for i in permutations:
        print(f"({str(i)[1:-1]})")
    print("\n")


def inverse(perm):
    print(f"- The permutation's inverse is: ({str([perm.index(i) + 1 for i in range(1, len(perm) + 1)])[1:-1]})")


def disjoint_cycles(perm):
    used = set()
    cycles = []
    minimum = 1
    while len(used) < len(perm):
        ciclo = [minimum]
        used.add(minimum)
        elt = perm[minimum - 1]
        while not elt in ciclo:
            ciclo.append(elt)
            used.add(elt)
            elt = perm[elt - 1]
        if len(set(perm).symmetric_difference(used)) != 0:
            minimum = min(set(perm).symmetric_difference(used))
        cycles.append(ciclo)
    return cycles


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def period(cycles):
    a = len(cycles[0])
    for i in cycles[1:]:
        b = len(i)
        GCD = gcd(a, b)
        a = a * b / GCD
    print(f"- Period: {int(a)}")
    return a


def parity(cycles):
    res = 0
    for i in cycles:
        if len(i) > 1:
            res += len(i) - 1
    if res % 2 == 0:
        print("- Parity of the permutation: even")
    else:
        print("- Parity of the permutation: odd")
    return res % 2


def informations(perm):
    cycles = disjoint_cycles(perm)
    info_perm = input("\n1 ==> Calculate the permutation's inverse\n"
                      "2 ==> Calculate the disjoint cycles of the permutation\n"
                      "3 ==> Calculate the period of the permutation\n"
                      "4 ==> Calculate the parity of the permutation\n"
                      "5 ==> Calculate all the previous steps\n"
                      "6 ==> Exit\n")

    if info_perm == "1":
        inverse(perm)

    elif info_perm == "2":
        s = ""
        for cycle in cycles:
            s += f"({str(cycle)[1:-1]}) "
        print(f"- Disjoint cycles: {s}")

    elif info_perm == "3":
        period(cycles)

    elif info_perm == "4":
        parity(cycles)

    elif info_perm == "5":

        print("------------------------------------")
        inverse(perm)

        s = ""
        for cycle in cycles:
            s += f"({str(cycle)[1:-1]}) "
        print(f"- Disjoint cycles: {s}")

        period(cycles)

        parity(cycles)
        print("------------------------------------")

    else:
        print("See you soon!")
        return

    informations(perm)


def start(Sn):
    choice = input(
        f"1 ==> Calculate all the elements of S{Sn}\n"
        f"2 ==> Insert a permutation of S{Sn}\n"
        f"3 ==> Exit\n"
    )
    if choice == "1":
        print_elements(Sn)
    elif choice == "2":
        perm = build_array(Sn)
        informations(perm)
        return
    else:
        return

    start(Sn)


if __name__ == "__main__":
    Sn = symmetric_group()
    start(Sn)
