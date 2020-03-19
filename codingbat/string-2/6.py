def xyz_there(str):
  for i in range(2, len(str)):
    if str[i] + str[i-1] + str[i-2] == 'zyx' and str[i-3] != '.':
      return True
  return False
