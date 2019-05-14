import random


def make_alphabet():
    A_to_Z = 26
    A_to_a = 32
    a_to_z = 26
    num_1 = 49
    num_9 = 58

    alphabet = []
    for i in range(A_to_Z):
        alphabet.append(ord('A') + i)

    for i in range(a_to_z):
        alphabet.append(ord('a') + i)

    for i in range(num_1, num_9):
        alphabet.append(i)

    for i, element in enumerate(alphabet):
        alphabet[i] = chr(element)

    return alphabet


def correct_places(current_pw, pw):
    correct = []
    for i, char in enumerate(current_pw):
        if char == pw[i]:
            correct.append(i)
    return correct


def is_found(curr_pw, pw):
    return curr_pw == pw


def get_random_char(alphabet):
    pos = random.randint(0, len(alphabet)-1)
    return alphabet[pos]


def make_new_pw(curr_pw, pw, alphabet):
    cor_places = correct_places(curr_pw, pw)
    new_pw = ""
    for i in range(len(pw)):
        new_pw += get_random_char(alphabet)

    new_pw = list(new_pw)
    for i in cor_places:
        new_pw[i] = curr_pw[i]

    return "".join(new_pw)

pw= "PrograMiraNje1"
curr_pw = "aaaaaaaaaaaaaa"
alphabet = make_alphabet()
counter = 0
print(curr_pw, counter)

while not is_found(curr_pw, pw):
    curr_pw = make_new_pw(curr_pw, pw, alphabet)
    counter += 1
    print(curr_pw, counter)

# print(make_alphabet())
# print(correct_places("programiranje2", password))
