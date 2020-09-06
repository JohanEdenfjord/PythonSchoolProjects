def transpose(m):
    result = []
    if m == result:
        return m
    else:
        for i in range(len(m[0])):
            r2 = []
            for j in range(len(m)):
                val = m[j][i]
                r2.append(val)
            result.append(r2)

    return result


def powers(m, p1, p2):
    result = []

    if m == result:
        return m
    else:
        for i in range(len(m)):
            r2 = []
            for j in range(p1, p2 + 1):
                val = m[i] ** j
                r2.append(val)

            result.append(r2)

    return result


def matmul(m1, m2):
    result = []
    if m1 == [] or m2 == []:
        return []
    else:
        for i in range(0, len(m1)):
            row = []
            for j in range(0, len(m2[0])):
                val = 0
                for k in range(0, len(m1[0])):
                    val += m1[i][k] * m2[k][j]
                row.append(val)
            result.append(row)
    return result


def invert(m1):
    det = (m1[0][0] * m1[1][1]) - (m1[0][1] * m1[1][0])
    rowA = [m1[1][1] / det, -m1[0][1] / det]
    rowB = [-m1[1][0] / det, m1[0][0] / det]
    return [rowA, rowB]


def loadtxt(thefile):
    data = open(thefile, "r")
    theData = data.readlines()
    data.close()

    rows = []
    finalData = []

    for lines in theData:
        rows.append(lines)

    for i in rows:
        s = i.split()
        for j in range(len(s)):
            s[j] = float(s[j])
        finalData.append(s)

    return finalData
