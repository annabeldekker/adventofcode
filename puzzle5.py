import sys
import string

def main(filename):
    opened = open(filename, 'r')
    polymer = opened.readlines()[0].strip()

    dict = {}
    for char in string.ascii_lowercase:
        stop = False
        count = 0
        newpolymer = polymer.replace(char, '')

        newpolymer = newpolymer.replace(char.upper(), '')
        while stop != True:

            if newpolymer[count] == newpolymer[count+1]:
                count += 1
            elif newpolymer[count].lower() == newpolymer[count+1].lower():
                newpolymer = newpolymer[:count] + newpolymer[count + 2:]
                if count != 0:
                    count = count - 1
            else:
                count += 1

            if len(newpolymer) == count+1:
                stop = True
        dict[char] = len(newpolymer)

    print(dict)
    min = len(polymer)
    bestchar = ''
    for char in dict:
        if dict[char] < min:
            min = dict[char]
            bestchar = char
    print('bestchar: ' + str(min))
if __name__ == '__main__':
    main(sys.argv[1])
