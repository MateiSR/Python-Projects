sentence = 'Lorem ipsum placerat in egestas erat imperdiet sed euismod est'
words = sentence.split()
print('The last 3 words are: ' + words[7] + '; ' + words[8] + '; ' + words[9])

sentence_new = sentence.replace(' sed euismod est', '') 
print('The sentence without those last 3 words is: ' + sentence_new)