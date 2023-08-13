import random

small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
special = [".","_",":","-","#","!","?"]
nums = ["0","1","2","3","4","5","6","7","8","9"]


def generate(length, small_check, special_check, nums_check, big_check, label):
    pw = ""

    # all options
    if small_check and special_check and nums_check and big_check:
        all = [*small, *big, *special, *nums, *big]
        for i in range(length):
            pw += random.choice(all)

    # 3 options
    if small_check and special_check and big_check and not nums_check:
        all = [*small, *special, *big]
        for i in range(length):
            pw += random.choice(all)

    if small_check and nums_check and big_check and not special_check:
        all = [*small, *nums, *big]
        for i in range(length):
            pw += random.choice(all)

    if small_check and special_check and nums_check and not big_check:
        all = [*small, *special, *nums]
        for i in range(length):
            pw += random.choice(all)

    if big_check and special_check and nums_check and not small_check:
        all = [*small, *special, *nums]
        for i in range(length):
            pw += random.choice(all)

    # 2 options
    if small_check and big_check and not nums_check and not special_check:
        all = [*small, *big]
        for i in range(length):
            pw += random.choice(all)

    if small_check and special_check and not nums_check and not big_check:
        all = [*small, *special]
        for i in range(length):
            pw += random.choice(all)

    if small_check and nums_check and not big_check and not special_check:
        all = [*small, *nums]
        for i in range(length):
            pw += random.choice(all)

    if big_check and nums_check and not small_check and not special_check:
        all = [*nums, *big]
        for i in range(length):
            pw += random.choice(all)

    if big_check and special_check and not small_check and not nums_check:
        all = [*special, *big]
        for i in range(length):
            pw += random.choice(all)

    if nums_check and special_check and not small_check and not big_check:
        all = [*nums, *special]
        for i in range(length):
            pw += random.choice(all)

    if small_check and not big_check and not special_check and not nums_check:
        all = [*small]
        for i in range(length):
            pw += random.choice(all)

    if big_check and not small_check and not special_check and not nums_check:
        all = [*big]
        for i in range(length):
            pw += random.choice(all)

    if nums_check and not big_check and not special_check and not small_check:
        all = [*nums]
        for i in range(length):
            pw += random.choice(all)

    if special_check and not big_check and not small_check and not nums_check:
        all = [*special]
        for i in range(length):
            pw += random.choice(all)

    label.delete(0, "end")
    label.insert(0, pw)
