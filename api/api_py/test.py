





def maximumProduct(nums):
    maxlist = nums[:3]
    minlist = nums[:2]
    
    maxlist.sort()
    minlist.sort()

    for num in nums[3:]:
      if num >= maxlist[2]:
        maxlist[0] =  maxlist[1]
        maxlist[1] =  maxlist[2]
        maxlist[2] = num
      elif num >= maxlist[1]:
        maxlist[0] = maxlist[1]
        maxlist[1] = num
      elif num >= maxlist[0]:
        maxlist[0] = num
    
    for num in nums[2:]:
      if num <= minlist[0]:
        minlist[1] = minlist[0]
        minlist[0] = num
      elif num <= minlist[1]:
        minlist[1] = num

    print(maxlist)
    print(minlist)

    maxRes = 1
    minRes = 1
    for num in maxlist:
        maxRes *= num

    for num in minlist:
        minRes *= num
  
    return max(maxRes, minRes * maxlist[2]);

print(maximumProduct([1,1,1,1,2,2,2,3,3,3]))