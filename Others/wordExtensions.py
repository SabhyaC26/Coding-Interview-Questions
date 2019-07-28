def wordExtend(word):
    wordMap = {}
    chars = []
    indices = []
    unique = ''.join(set(word))
    for c in unique:
        wordMap[c] = 0
    for c in word:
        wordMap[c] += 1
        if (wordMap[c] == 3):
            chars.append(c)
    for c in chars:
        start = word.find(c)
        stop = start + wordMap[c] - 1
        indices.append([start, stop])
    return indices

def main():
    print(wordExtend("whaaaaatttsup"))

if __name__ == "__main__":
    main()
