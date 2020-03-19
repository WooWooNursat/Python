def close_far(a, b, c):
  return abs(a - b) <= 2 and abs(a-c) + abs(b-c) >= 4 or abs(a-c) <= 2 and abs(a-b) + abs(b-c) >= 4
