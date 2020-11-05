from collections import Counter

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

word_count = Counter(words)
top_three = word_count.most_common(3)

print(top_three)

print(word_count['not'])

morewords = ['why','are','you','not','looking','in','my','eyes']

for w in morewords:
    # It can be used as a dictionary:
    word_count[w] += 1

# The .update(...) method 
