def concatenate(s1: str, s2: str) -> str:
    length = s1 + s2

    if len(length) > 10:
        return "Too long!"
    else:
        return length




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
