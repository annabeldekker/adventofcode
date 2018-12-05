import sys


def main(filename):
    opened = open(filename, 'r')
    dict = {}

    id = 0
    for line in opened:
        d_list = line.split()[2].strip(':').split(',')
        width = int(line.strip().split()[3].split('x')[0])
        length = int(line.strip().split()[3].split('x')[1])

        index_list = []
        for i in range(int(d_list[0]), int(d_list[0]) + width):
            for n in range(int(d_list[1]), int(d_list[1]) + length):
                inch = str(i) + ',' + str(n)
                if inch not in list(dict.keys()):
                    dict[inch] = [line.split()[0][1:]]
                else:
                    dict[inch].append(line.split()[0][1:])

# Answer puzzle A
    count = 0
    unique = []
    non_unique = []
    for inch in dict:
        if len(dict[inch]) > 1:
            count += 1
            non_unique += dict[inch]
        elif len(dict[inch]) == 1:
            unique.append(dict[inch][0])

    print('amount overlapping inches: ' + count)

# Answer puzzle B
    for id in set(unique):
        if id not in set(non_unique):
            print(id)





if __name__ == '__main__':
    main(sys.argv[1])
