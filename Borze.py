code = input()
#word = False
count = 0
while True:
  if count == 0 and code[count] == '.':
    print(0,end='')
    count += 1
  if count < len(code):
    if code[count] == '.':
      print(0,end='')
      count += 1
      if count > len(code)-1:
        break
      if count > len(code)-1:
        break
    if code[count] == '-':
      if code[count+1] == '.':
        print(1, end='')
        count += 2
        if count > len(code)-1:
          break
        
      elif code[count+1] == '-':
        print(2,end='')
        count += 2
  if count > len(code)-1:
    break