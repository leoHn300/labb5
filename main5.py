defmedians(num1, num2):
  amend_nums = num1 + num2
  amend_nums = sorted(amend_nums)
    length = int(len(amend_nums))
    if len(amend_nums) % 2 == 1:
        median = amend_nums[length/2-0,5]
    else:
        median = (amend_nums[int(length/2)]+amend_nums[int(length/2)])/2
    return "%.5f" % median