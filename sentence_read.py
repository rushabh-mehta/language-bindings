sentences = []

with open('readme.txt') as f:
    lines = f.readlines()

for sentence in lines:
    temp = sentence.strip()
    if temp != '':
        sentences.append(temp)    

print(sentences)

