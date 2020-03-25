def round_sum(a, b, c):
  s = 0
  arr = [a, b, c]
  def round10(n):
    if n%10>=5:
      return (int(n/10) + 1) * 10
    return int(n/10) * 10
  for i in range (0,3,1):
    s = s + round10(arr[i])
  return s
