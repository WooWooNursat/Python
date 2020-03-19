def count_code(str):
  k = 0
  for i in range (3, len(str)):
    if str[i] + str[i-2] + str[i-3] == 'eoc':
      k = k + 1
  return k
