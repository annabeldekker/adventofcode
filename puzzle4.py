import sys
from collections import Counter

# find guard that sleeps most and find minute it has slept on most
def main(filename):
    opened = open(filename, 'r')
    events = opened.readlines()
    sortedevents = []

# Sorting the input
    for event in events:
        month = event[6:8]
        day = event[9:11]
        min = event[15:17]
        time_id = month+day+min
        sortedevents.append([time_id, event.strip()[19:]])
    sortedevents = sorted(sortedevents)


    guardtrack = {}
    guards = []
    for event in sortedevents:
        if event[1][0] == 'G':
            guard = event[1].split()[1]
            if guard not in guards:
                guards.append(guard)
                guardtrack[guard] = []
        elif event[1][0] == 'f':
            start = event[0][4:6]
            if start[0] == 0:
                start = start[1:]
        elif event[1][0] == 'w':
            stop = event[0][4:6]
            if stop[0] == 0:
                stop = stop[1:]
            slept = []
            for i in range(int(start), int(stop)):
                slept.append(i)
            guardtrack[guard] += slept
        else:
            print('idontunderstand')

# Answer puzzle A
    maxsleep = 0
    dumbo = ''
    for guard in guardtrack:
        sleep = len(guardtrack[guard])
        if sleep > maxsleep:
            dumbo = guard
            maxsleep = sleep
        else:
            pass
    print('massive sleeper is guard: '+dumbo)
    minute, freq = Counter(guardtrack[dumbo]).most_common(1)[0]
    print('He sleeps most at: '+str(minute))
    print(int(dumbo[1:])*minute)

# Answer puzzle B
    guardfreq = {}
    for guard in guardtrack:
        if guardtrack[guard]:
            minfreq = Counter(guardtrack[guard]).most_common(1)[0]
            guardfreq[guard] = minfreq

    count = 0
    maxfreq = 0
    bestguard = ''
    print(guardfreq)
    for track in guardfreq:
        moment, freq = guardfreq[track]
        if freq > maxfreq:
            maxfreq = freq
            bestmin = moment
            bestguard = track

    print(bestguard, maxfreq, bestmin)
    print('Here: ' + str(int(bestguard[1:]) * bestmin ))

if __name__ == '__main__':
    main(sys.argv[1])
