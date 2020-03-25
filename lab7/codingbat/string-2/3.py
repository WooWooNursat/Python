def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(2, len(str)):
    if str[i-2] + str[i-1] + str[i] == 'cat':
      cat = cat + 1
    elif str[i-2] + str[i-1] + str[i] == 'dog':
      dog = dog + 1
  return cat == dog
