total = 0
total2 = 0

cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open('input') as fp:
    for line in fp:
        over = False
        red_max = 0
        green_max = 0
        blue_max = 0

        data = line.strip().split(':')
        games = data[1].split(';')
        for round in games:
            raw = round.split(',')
            #print(raw)
            for info in raw:
                cr = info.strip().split(' ')
                if cubes[cr[1]] < int(cr[0]):
                    over = True
                if cr[1] == 'red' and red_max < int(cr[0]):
                    red_max = int(cr[0])
                if cr[1] == 'green' and green_max < int(cr[0]):
                    green_max = int(cr[0])
                if cr[1] == 'blue' and blue_max < int(cr[0]):
                    blue_max = int(cr[0])
                
        if not over:
            tally = data[0].split(' ')
            total = total + int(tally[1])

        total2 = total2 + int(red_max) * int(green_max) * int(blue_max)

    print("part 1: " + str(total))
    print("part 2: " + str(total2))