import re
import pprint

cat = {}
idx = 0

with open('input') as fp:
    for line in fp:
        #print(line.strip())
        if re.search(r"^seeds:", line):
            data = line.strip().split(':')
            cat[idx] = data[1].split()

        elif re.search(r"(.*)\ map:$", line.strip()):
            m = str(re.search(r"(.*)\ map:$", line).groups())
            #print(m)
        elif line.strip() == '':
            print("index " + str(idx) + " is done!")
            idx = idx + 1
        else:
            data = line.strip().split()
            if not idx in cat:
                cat[idx] = {}
            for x in range(int(data[2])):
                cat[idx][int(data[1])+x] = int(data[0]) + x



pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(cat)

ans = []

for seed in cat[0]:
    newseed = int(seed)
    for z in range(1, len(cat)):
        if newseed in cat[z]:
            temp = newseed
            newseed = cat[z][(temp)]
    ans.append(newseed)

ans.sort()    
print("part1: " + str(ans[0]))