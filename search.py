def search_linear(alist, item):
    
    for i in range(len(alist)):
        if item == alist[i]:
            return (i)
    return -1

def find_unknown_words(vocab, wds):
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

def load_words_from_file(filename):
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

def text_to_words(the_text):
    my_substitutions = the_text.maketrans(
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      "abcdefghijklmnopqrstuvwxyz                                          ")
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


book_words = get_words_in_book("AliceInWonderland.txt")
vocab = get_words_in_book("vocab.txt")

unknown_words=find_unknown_words(vocab,book_words)
print('there are',len(unknown_words),'unknown_words','they are:',unknown_words)


book_words = get_words_in_book("AliceInWonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))



import time

t0 = time.clock()
missing_words = find_unknown_words(vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))