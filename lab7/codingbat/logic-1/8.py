def in1to10(n, outside_mode):
  if n>=1 and n<=10 and outside_mode == False:
    return True
  if n<=1 and outside_mode == True or n>=10 and outside_mode == True:
    return True
  return False
