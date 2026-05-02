from typing import List

def read_integers() -> List[int]:
    list_integers = input()
    string_list = list_integers.split(",")
        
    return [int(x) for x in string_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
