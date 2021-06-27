import pprint

message = input("Type in a message: ")
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pp(count)

