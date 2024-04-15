emptyMap = []

with open('E:\Egyetem Drive\OneDrive - Eotvos Lorand Tudomanyegyetem\Egyetem\\7.félév\EVA\Bead\Labyrinth game\Labyrinth game\Labyrinth game\Assets\Maps\map10.txt', 'r') as f:
    map = f.read().splitlines()

    for i in range(len(map)):
        map[i] = map[i].split(' ')
        for j in range(len(map[i])):
            map[i][j] = int(map[i][j])

    for i in range(len(map)):
        print(map[i])

    for i in range(len(map)):
        line = []
        for j in range(len(map[i])):
            line.append(map[j][i])
        emptyMap.append(line)


    for i in range(len(emptyMap)):
        print(emptyMap[i])
    f.close()

with open('E:\Egyetem Drive\OneDrive - Eotvos Lorand Tudomanyegyetem\Egyetem\\7.félév\EVA\Bead\Labyrinth game\Labyrinth game\Labyrinth game\Assets\Maps\map10C.txt', 'w') as f:
    for i in range(len(emptyMap)):
        for j in range(len(emptyMap[i])):
            f.write(str(emptyMap[i][j]))
            f.write(' ')
        f.write('\n')
    f.close()