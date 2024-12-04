# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     answer = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] != nums[j] and nums[i] + nums[j] == target:
#                 answer.append(i)
#                 answer.append(j)
#                 print(answer)
#                 break
#         if len(answer) > 0:
#             break

# twoSum([2,7,11,15], 9)

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    def len_linked_list(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def listToInt(list):
        num = ""
        for i in range(len_linked_list(list)):
            num += str(list[len(list) - (i + 1)])
        return int(num)
    
    def intToList(interger):
        intString = str(interger)
        returnList = []
        for i in range(len_linked_list(intString)):
            returnList.append(int(intString[len(intString) - (i + 1)]))
        return returnList

    num1, num2 = listToInt(l1), listToInt(l2)
    sumOfNums = num1 + num2

    return intToList(sumOfNums)
    
    

addTwoNumbers([2,4,3], [5,6,4])