year = input()
copy = int(year)
while True:
  copy += 1
  year = str(copy)
  if len(set(list(year))) == 4:
    print(year)
    break