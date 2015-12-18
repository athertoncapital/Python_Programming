prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p!="O" and p!="Q":
        print(p + suffix)
    else:
        print(p+"u"+suffix)


