import re

with open("in.txt") as infile:
    content = infile.read()

def find_muls(content):
    matches = re.findall("mul\(\d+,\d+\)", content)

    sum = 0
    for m in matches:
        [a,b] = re.search("\d{1,3},\d{1,3}", m).group(0).split(",")
        sum += int(a) * int(b)
    return sum
print("Ex1: ",find_muls(content))

def find_do_muls(content):
    content  = content.replace("\n","") # would have loced to have used
    stripped = re.sub("((don't\(\)).*?do\(\))|don't.*(don't)", "", content)
    return find_muls(stripped)

print("Ex2: ", find_do_muls(content))
