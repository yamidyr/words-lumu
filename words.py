numberOfChars = 0
numberOfWords = 0
words = {}
orderedWords = []

def addWord(word):
  if word in words:
    newFrequenceWord = words[word] + 1
    i = 0
    while True:
      if i == numberOfWords:
        orderedWords.remove((word,words[word]))
        orderedWords.append((word, newFrequenceWord))
        break
      if orderedWords[i][1] < newFrequenceWord:
        orderedWords.remove((word,words[word]))
        orderedWords.insert(i, (word, newFrequenceWord))
        break
      i += 1
    words[word] += 1

  else:
    words[word] = 1
    orderedWords.append((word,1))

with open("texto.txt", "r") as file:
  text = file.read()
  word = ""
  for char in text:
    numberOfChars += 1
    if char.isspace():
      if word != "":
        addWord(word)
        numberOfWords += 1
      word = ""
    else:
      word += char
  if word != "":
    addWord(word)
    numberOfWords += 1

print("{:<15} {:<5}".format(numberOfChars,"characters"))
print("{:<15} {:<5}".format(numberOfWords,"words") + "\n")

for word in orderedWords:
  print("{:<15} {:<5}".format(word[0],word[1]))