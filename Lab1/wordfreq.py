

def tokenize(lines):

    words = []

    for line in lines:
        i = line.strip('\n')
        start = 0

        while start < len(i):
            ch = line[start]

            if ch.isspace():
                start = start + 1

            elif ch.isalpha():
                end = start + 1

                while end < len(i):
                    if i[end].isalpha():
                        end = end + 1
                    else:
                        break

                word = i[start:end].lower()
                words.append(word)
                start = end

            elif ch.isdigit():

                end = start + 1

                while end < len(i):
                    if i[end].isdigit():
                        end = end + 1
                    else:
                        break

                word = i[start:end]
                words.append(word)
                # print(word)
                start = end

            else:
                # print(ch + " is a symbol")

                end = start + 1
                word = i[start:end]
                words.append(word)
                # print(word)
                start = end

    return words


def countWords(words, stopWords):
    counted = {}

    for word in words:
        if word in stopWords:
            continue

        if word not in counted:
            counted[word] = 1
        else:
            counted[word] += 1

    return counted


def printTopMost(frequencies, n):

    wordsTuple = [(k, v) for k, v in frequencies.items()]
    newList = sorted(wordsTuple, key=lambda x: -x[1])
    i = 0
    theString = ""

    if n < len(newList):
        while i < n:
            # print(newList[i][0].ljust(20), str(newList[i][1]).rjust(5))
            theString = theString + newList[i][0].ljust(20) + str(newList[i][1]).rjust(5) + "\n"
            i += 1

    elif n == 0 or n > len(newList):
        return ""

    return theString


def main():
    pass


main()
