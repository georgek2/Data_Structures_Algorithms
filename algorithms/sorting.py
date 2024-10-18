

nums = [2, 4, 1, 6, 34]
print(nums)

def merge_sort(nums):

    for i in range(len(nums)):
        print('-----------------------------------')
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                print(f'swap: {nums}')
            else:
                print(f'no swap: {nums}')
                continue


merge_sort(nums)
# print(nums)

'''
    Has a time complexity BigO(n^2)
'''

def another_sort(nums):

    pass

another_sort(nums)













