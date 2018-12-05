import sys

def main(file):
    openedfile = open(file, 'r')
    count_2 = 0
    count_3 = 0
    id_list = []

    for line in openedfile:
        id = line.strip()
        id_list.append(id)
        checked_2 = False
        checked_3 = False
        for char in id:
            if (id.count(char) == 2) and (checked_2 == False):
                count_2 += 1
                checked_2 = True

            elif (id.count(char) == 3) and (checked_3 == False):
                count_3 += 1
                checked_3 = True
            else: pass
    print('Checksum: ' + str(count_2 * count_3))

    count = 0
    print(len(id_list))
    for id_1 in id_list:
        for id_2 in id_list[0:count] + id_list[count+1:len(id_list)]:
            for i in range(0, len(id_1)+1):
                sub_id_1 = id_1[0:i] + id_1[i+1:len(id_1)]
                sub_id_2 = id_2[0:i] + id_2[i+1:len(id_2)]
                if sub_id_1 == sub_id_2:
                    correct1 = id_1
                    correct2 = id_2
                    print(sub_id_1)
        count += 1
    print(correct1, correct2)

if __name__ == '__main__':
    main(sys.argv[1])
