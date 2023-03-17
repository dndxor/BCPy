
step = 30

for r in range(0, 256, step) :
    for g in range(0, 256, step) :
        for b in range(0, 256, step) :
            cstr = str(r) + ';' + str(g) +';' + str(b)
            print("0x%02x:%02x:%02x" % (r, g, b))
            print('\033[48;2;' + cstr + 'm' + '          ' + '\033[0m')
