def sum13(nums):
  s = 0
  if nums == []:
    return 0
  for i in range(len(nums)):
    if nums[i] == 13 or i!=0 and nums[i-1] == 13:
      continue
    else:
      s = s + nums[i]
  return s