def answer(heights):
    N = len(heights)
    # Scan for left highest
    lhigh = -1
    lindex = -1
    larray = [0] * N
    for i in range(N):
        vi = heights[i]
        if vi < lhigh:
            larray[i] = lindex
        else:
            larray[i] = i
            lhigh = vi
            lindex = i
    # scan for right highest
    rhigh = -1
    rindex = -1
    rarray = [0] * N
    for i in range(N-1, -1, -1):
        vi = heights[i]
        if vi < rhigh:
            rarray[i] = rindex
        else:
            rarray[i] = i
            rhigh = vi
            rindex = i

    # print (larray)
    # print ([heights[i] for i in larray])
    # print (rarray)
    # print ([heights[i] for i in rarray])

    # build total height
    total = 0
    for i in range(N):
        lindex = larray[i]
        rindex = rarray[i]
        if i - lindex > 0 and rindex - i > 0:
            v = min(heights[lindex], heights[rindex]) - heights[i]
            total += v
            # print ("Height of cell {} is {}".format(i, v))
    # print("Total is {}".format(total))
    return total


heights = [1, 4, 2, 5, 1, 2, 3]
heights = [1, 2, 3, 2, 1]
answer(heights)
[0, 1, 1, 3, 3, 3, 3]
[3, 3, 3, 3, 6, 6, 6]
