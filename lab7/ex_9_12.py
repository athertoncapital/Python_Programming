def countsam(data):
    k = 0
    s="sam"
    for j in data:
        k += 1
        if j == s:
            break
    return k
print(countsam(["kkkk","dsaf","fdklsamkk"]))
