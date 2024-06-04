import itertools as it
import random
import pyperclip
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.OKBLUE + "Starting Password Generator..." + bcolors.ENDC)
print("")
characters = {
    "Uppercases": 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    "Lowercases": 'abcdefghijklmnopqrstuvwxyz',
    "Numbers": '0123456789',
    "Symbols": '!@#$&*?_-',
}
while True:
    try:
        n = int(input("\tLength of Password: "))
        break
    except ValueError:
        print(bcolors.FAIL + "Entered Value should be an integer only" + bcolors.ENDC)
        print("Restarting the program...")
        print("")
def gen_pass(n):
    print(bcolors.OKGREEN + "Select Character type number from the list: " + bcolors.ENDC)
    arr = ["Numbers", "Uppercases", "Lowercases", "Symbols"]
    combinations = []
    for i in range(1, len(arr) + 1):
        combinations.extend(it.combinations(arr, i))

    for idx, combo in enumerate(combinations):
        print(f"\t{idx + 1} --- {combo}")

    print("")
    while True:
        try:
            c_type = int(input("Type any serial number from the above list of combinations: "))
            if 1 <= c_type <= len(combinations):
                break
            else:
                print(bcolors.HEADER + "Serial number should be from 1 to " + str(
                    len(combinations)) + "..." + bcolors.ENDC)
        except ValueError:
            print(bcolors.FAIL + "Entered Value should be an integer only" + bcolors.ENDC)

    selected_combo = combinations[c_type - 1]
    c_per_pass = n // len(selected_combo)
    extra_c = n - (c_per_pass * len(selected_combo))

    password_chars = []
    all_char = []

    for category in selected_combo:
        chars = characters[category]
        all_char.extend(chars)
        password_chars.extend(random.choices(chars, k=c_per_pass))

    password_chars.extend(random.choices(all_char, k=extra_c))
    random.shuffle(password_chars)

    password = "".join(password_chars)
    print(bcolors.HEADER + "Your password: " + password + bcolors.ENDC)
    pyperclip.copy(password)
    print(bcolors.OKCYAN + "Your password is copied to your clipboard." + bcolors.ENDC)
gen_pass(n)
