# Problem 9
#
# Write a function to find all common elements between two lists.
#
# def common_elements(nums1, nums2):
#


#comparing two lists
#need the two lists
#need to loop through each element of list one and loop + compare to list two
#then keep track of comparisons

# IF element IN list,dictionary,string
# put like elements in new list




def common_elements(nums1, nums2):

    in_common = []
    for nums in nums1:
        if nums in nums2:
            in_common.append(nums)
    print(in_common)

common_elements([1,2,4,3,45], [1,4,45,6])
