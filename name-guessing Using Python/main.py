
print("\t\t\t\t\t\t\t<====== CODE WITH AMINA ======>\n")
print("\t\t\t\t\t\t\t<-------- WELCOME TO NAME GUESSING -------->\n")
1

first_no = []
second_no = []
first_name = []
second_name = []
final_name = []

sample1 = "AEIMQU"
sample2 = "BFJNRVY"
sample3 = "CGKOSWZ"
sample4 = "DHLPTX"

letters_in_name = int(input("Let me know how many letters are in your name, please tell... "))

nums = "       1   2   3   4"
alphabets = ("      | A | B | C | D |\n"
             "      | E | F | G | H |\n"
             "      | I | J | K | L |\n"
             "      | M | N | O | P |\n"
             "      | Q | R | S | T |\n"
             "      | U | V | W | X |\n"
             "          | Y | Z |")

print("\n", nums, "\n")
print(alphabets, "\n")

for i in range(1, letters_in_name + 1):
    ordinal = str(i)
    if ordinal.endswith("1") and not ordinal.endswith("11"):
        ordinal = f"{i}st"
    elif ordinal.endswith("2") and not ordinal.endswith("12"):
        ordinal = f"{i}nd"
    elif ordinal.endswith("3") and not ordinal.endswith("13"):
        ordinal = f"{i}rd"
    else:
        ordinal = f"{i}th"
    
    first_turn = int(input(f"Enter the column number of the {ordinal} letter of your name.. "))
    first_no.append(first_turn)

first = "         | A | E | I | M | Q | U |"
second = "         | B | F | J | N | R | V | Y |"
third = "         | C | G | K | O | S | W | Z |"
fourth = "         | D | H | L | P | T | X |"


for val in first_no:
    if val == 1:
        first_name.append(first)
        second_name.append(sample1)
    elif val == 2:
        first_name.append(second)
        second_name.append(sample2)
    elif val == 3:
        first_name.append(third)
        second_name.append(sample3)
    elif val == 4:
        first_name.append(fourth)
        second_name.append(sample4)
    else:
        continue

print("\nCould You repeat that pattern for the same name...?\n")

num = "           1   2   3   4   5   6   7"
print(num, "\n")

for letters in first_name:
    print(letters)

for i in range(1, letters_in_name + 1):
    ordinal = str(i)
    if ordinal.endswith("1") and not ordinal.endswith("11"):
        ordinal = f"{i}st"
    elif ordinal.endswith("2") and not ordinal.endswith("12"):
        ordinal = f"{i}nd"
    elif ordinal.endswith("3") and not ordinal.endswith("13"):
        ordinal = f"{i}rd"
    else:
        ordinal = f"{i}th"


    
    second_turn = int(input(f"Enter the column number of the {ordinal} letter of your name... "))
    second_no.append(second_turn)

for i in range(len(second_no)):
    final_name.append(second_name[i][second_no[i] - 1])

name = "".join(final_name)
print(f"\n          THE NAME YOU THOUGHT OF: {name}")




