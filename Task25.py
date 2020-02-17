text = input()
print(text)
words = text.split()
longest = 0

for i in range(1,len(words)):
   if len(words[longest]) < len(words[i]):
        longest = i

print(words[longest])