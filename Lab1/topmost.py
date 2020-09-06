import wordfreq
import sys
import urllib.request


def main():

    inp_stop = open(sys.argv[1], encoding='utf8')

    if str(sys.argv[2])[:4].lower() == "http" or str(sys.argv[2])[:3].lower() == "www":
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
    else:
        response = open(sys.argv[2], encoding='utf8')
        lines = response

    numberofwords = int(sys.argv[3])
    stopwords = inp_stop.read().strip()
    # print(stopwords)

    words = wordfreq.tokenize(lines)
    countedWords = wordfreq.countWords(words, stopwords)
    topmost = wordfreq.printTopMost(countedWords, numberofwords)

    print(topmost)

    response.close()
    inp_stop.close()


main()
