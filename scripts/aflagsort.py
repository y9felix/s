c = input("Enter character: ")
with open("all.txt") as f:
    lines = f.readlines()

keep, move = [], []
for l in lines:
    (move if c in l else keep).append(l)

with open("all.txt", "w") as f:
    f.writelines(keep)
with open("yo.txt", "a") as g:
    g.writelines(move)