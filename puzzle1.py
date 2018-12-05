import sys
def main(freq_file):
    result = 0
    freq_opened = open(freq_file, 'r')
    freq_list = [0]

    found = False
    while found == False:
        freq_opened = open(freq_file, 'r')
        for line in freq_opened:
            if line[0] == '+':
                result = result + int(line[1:])
                if result in freq_list:
                    print('The first twice is: ' + str(result))
                    found = True
                else:
                    freq_list.append(result)
            elif line[0] == '-':
                result = result - int(line[1:])
                if result in freq_list:
                    print('The first twice is: ' + str(result))
                    found = True
                else:
                    freq_list.append(result)
        print(len(freq_list))
        freq_opened.close()

    print(len(set(freq_list)))
    print(result)

if __name__ == '__main__':
    main(sys.argv[1])
