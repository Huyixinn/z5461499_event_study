def freqword(filepath):
    with open(filepath) as file:
        counts = dict()
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word,0) + 1
        maxword = None
        maxcount = None
        for word, count in counts.items():
            if maxcount is None or count > maxcount:
                maxcount = count
                maxword = word
        return f"The most frequent word is: {maxword}, and the frequency is: {maxcount}"
result = freqword(r"D:\网页下载\week5_data (2)\iso.txt")
print(result)

