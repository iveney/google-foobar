import random

memoization = {}

def opt(minions, remain):
    '''
    Returns the best time using the remain minions, also the sequence
    '''
    if remain.count(1) == 0:
        # if empty, just return zero-time and empty list
        return 0, []

    if repr(remain) in memoization:
        return memoization[repr(remain)]

    N = len(minions)
    best = 100000
    for i in range(N):
        # Find a minion that is not yet used
        if remain[i] == 0:
            continue
        ith = minions[i]
        Ti, Ni, Di = ith
        Pi = 1.0 * Ni / Di
        remain[i] = 0
        time_remain, seq_remain = opt(minions, remain)
        time = Pi * Ti + (1 - Pi) * (Ti + time_remain)
        if time < best:
            best = time
            best_seq = [i] + seq_remain
        remain[i] = 1

    memoization[repr(remain)] = (best, best_seq)
    return best, best_seq

def answer(minions):
    N = len(minions)
    remain = [1] * N

    T, seq = opt(minions, remain)
    print (T, seq)
    return seq

minions = [[5, 1, 5], [10, 1, 2]]
minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]

def get_random_input(N):
    l = []
    for i in range(N):
        numerator = random.randint(1, 1023)
        denominator = random.randint(numerator + 1, 1024)
        l.append([random.randint(1, 1024), numerator, denominator])
    return l

# minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
minions = get_random_input(4)
for m in minions:
    print ("Prob = {}, Time = {}, E = {}".format(1.0 * m[1] / m[2], m[0], 1.0 * m[0] * m[1] / m[2]))
    # print 1.0 * m[0] * m[1] / m[2]
print(minions)
answer(minions)
print(memoization)
