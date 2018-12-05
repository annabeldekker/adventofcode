import sys


def main(filename):
    opened = open(filename, 'r')
    dict = {}

    for line in opened:
        d_list = line.split()[2].strip(':').split(',')
        width = int(line.strip().split()[3].split('x')[0])
        length = int(line.strip().split()[3].split('x')[1])

        index_list = []
        for i in range(int(d_list[0]), int(d_list[0]) + width):
            for n in range(int(d_list[1]), int(d_list[1]) + length):
                inch = str(i) + ',' + str(n)
                if inch not in list(dict.keys()):
                    dict[inch] = 1
                else:
                    dict[inch] += 1

    count = 0
    for inch in dict:
        if dict[inch] > 1:
            count += 1

    print(count)

if __name__ == '__main__':
    main(sys.argv[1])
