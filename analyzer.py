from nltk.corpus import inaugural
from nltk.text import Text

speech = Text(inaugural.words("2009-Obama.txt"))
    
total_len = len(speech)
unique_types = len(set(speech))
num_letters = [len(w) for w in speech]
avg_word_len = sum(num_letters) / total_len 

print("2009-Obama")
print("words total: ", total_len)
print("unique words: ", unique_types)
print("lexical diversity: ", total_len / unique_types)
print("average word lenght: ", avg_word_len)

#print("2001-Bush")
#print("words total: ", total_len)
#print("unique words: ", unique_types)
#print("lexical diversity: ", total_len / unique_types)
#print("average word lenght: ", avg_word_len)

#print("1969-Nixon")
#print("words total: ", total_len)
#print("unique words: ", unique_types)
#print("lexical diversity: ", total_len / unique_types)
#print("average word lenght: ", avg_word_len)

#print("1789-Washington")
#print("words total: ", total_len)
#print("unique words: ", unique_types)
#print("lexical diversity: ", total_len / unique_types)
#print("average word lenght: ", avg_word_len)
