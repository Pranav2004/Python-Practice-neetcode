def add_two_numbers() -> int:
    integers = input().split(',')
    addition = 0
    i, j = map(int, integers)
    addition = i + j
        
    return addition



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())