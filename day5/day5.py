import re

cat = {}
idx = 0

with open('sample') as fp:
    for line in fp:
        #print(line.strip())
        if re.search(r"^seeds:", line):
            data = line.strip().split(':')
            cat[idx] = data[1].split()

        elif re.search(r"(.*)\ map:$", line.strip()):
            m = str(re.search(r"(.*)\ map:$", line).groups())
            #print(m)
        elif line.strip() == '':
            print("empty line")
            idx = idx + 1
        else:
            data = line.strip().split()
            if idx in cat:
                print("present")
            else:
                cat[idx] = None
        
print(cat)