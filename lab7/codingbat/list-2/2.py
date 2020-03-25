def big_diff(nums):
  minn = 999999
  maxx = -99999
  for i in range( len(nums)):
    maxx = max(nums[i], maxx)
    minn = min(nums[i], minn)
  return maxx - minn
