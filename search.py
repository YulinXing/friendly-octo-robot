def search(alist, item):
    
    for i in range(len(alist)):
        if item == alist[i]:
            return (i)
    return -1

def unknownWords(vocab, wds):
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

def loadWords(filename):
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

def getBookWord(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


book_words = getBookWord("AliceInWonderland.txt")
vocab = getBookWord("vocab.txt")

unknown_words=unknownWords(vocab,book_words)
print('there are',len(unknown_words),'unknown_words','they are:',unknown_words)


book_words = getBookWord("AliceInWonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))

missing_words = unknownWords(vocab, book_words)
print("There are {0} unknown words.".format(len(missing_words)))
