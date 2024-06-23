S = input()
output = ""
is_spoiler = True

for s in S:
    if s == "|":
        is_spoiler = not bool(is_spoiler)
    else:
        if is_spoiler:
            output += s
        
print(output)