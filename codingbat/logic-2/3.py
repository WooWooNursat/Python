def lucky_sum(a, b, c):
  arr = [a, b, c]
  s = 0
  for i in range(0, 3, 1):
    if arr[i] == 13:
      break
    s = s + arr[i]
  return s
