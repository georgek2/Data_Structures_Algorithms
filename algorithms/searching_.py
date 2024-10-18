
nums = [2, 4, 1, 6, 34, 7, 8, 34, 9]


# Linear Search
num = 5

def linear_search(num):
    found = False
    for ind, i in enumerate(nums):
        if i == num:
            found = True
            print(f'number found: ind - {ind}')
        else:
            continue

    if found == False:
        print('number not found')


# linear_search(100)
'''
    It has a BigO(n) time complexity: the worst case scenario is that we go through 
    a list with n items before we find the num we are searching
'''

# Binary Search

sorted_list = sorted(nums)
def binary_search(num, nums):
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    print('Starting....')
    if nums[mid] > num:
        for i in right:
            if i == num:
                print('number found')
                # binary_search(right)
    elif nums[mid] < num:
        for i in left:
            if i == num:
                print('number found')
                # binary_search(left)
    else:
        print('number found')
        
binary_search(44, sorted_list)










