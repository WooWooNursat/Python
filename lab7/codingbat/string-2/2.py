def count_hi(str):
  k = 0
  for i in range(1,len(str)):
    if str[i-1] + str[i] == 'hi':
      k = k + 1
  return k
