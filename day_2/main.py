from typing import List

with open("in.txt") as infile:
    content = infile.read()
    content_list = content.split("\n")

safe: int= 0

def safety_check(levels_list: List[int])-> bool:
    print("-----------------")
    max_difference_in_levels = 3
    for i in range(len(levels_list)-1):
        if abs(levels_list[i+1] - levels_list[i]) > max_difference_in_levels:
            print("TOO HIGH DIFFERENCE")
            return False

    # inc check
    if levels_list[0]>levels_list[1]:
        print("LIST DECREASING")
        inc = False
    else:
        print("LIST INCREASING")
        inc = True

    for i in range(len(levels_list)-1):
        if levels_list[i] == levels_list[i+1]:
            print("SAME LEVELS")
            return False
        if inc:
            if levels_list[i+1] < levels_list[i]:
                print("LIST SHOULD BE INCEASING")
                return False
        else:
            if levels_list[i+1] > levels_list[i]:
                print("LIST SHOULD BE DECREASING")
                return False
    print("SAFE")
    return True

def brute_safety_check(levels_list: List[int])-> bool:
    safe_results = 0
    possible_lists: List[List[int]] = []
    for i in range(len(levels_list)):
        possible_lists.append(levels_list[:i] + levels_list[i+1:])
    print(possible_lists)
    for possible_list in possible_lists:
        if safety_check(possible_list):
            safe_results = safe_results + 1
    if safe_results > 0:
        return True


for line in content_list:
    if line:
        levels: List[int] = [int(x) for x in line.split()]
        if safety_check(levels):
            safe = safe + 1
        elif brute_safety_check(levels):
            safe = safe + 1
print(safe)
