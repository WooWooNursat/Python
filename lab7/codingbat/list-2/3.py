def centered_average(nums):
  maxx = -999999
  minn = 999999
  s = 0
  for i in range(len(nums)):
    maxx = max(maxx, nums[i])
    minn = min(minn, nums[i])
    s = s + nums[i]
  return (s - maxx - minn)/(len(nums)-2)
