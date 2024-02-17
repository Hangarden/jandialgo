# 5 0
# -7 -3 -2 5 8


n, target = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False]* n
count = 0
# def back(N,start, lst, nums):
#     global count
#     if N == n:
#         print(lst)
#         count += 1
#         return
#
#     for i in range(n):

def back(start, path, nums):
    global count
    # Add current path to the result
    if path:  # Ensure the path is not empty
        if target == sum(path):
            count += 1
    # Generate combinations by exploring further elements
    for i in range(start, len(nums)):
        # Include arr[i] in the combination
        path.append(nums[i])
        # Move to the next element
        back(i + 1, path, nums)
        # Exclude arr[i] from the combination, backtrack
        path.pop()

back(0, [], nums)
print(count)