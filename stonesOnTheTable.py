num = int(input())
word = list(input())
count = -1
move = 0
while count < len(word)-2:
  count += 1
  if word[count] == word[count + 1]:
    move += 1
    word.pop(count)
    count = -1

print(move)