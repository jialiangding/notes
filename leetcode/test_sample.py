# def inc(x):
#     return x + 1
# def test_answer():
#     assert inc(3) == 5

#给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c
# 使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# def threeSum(self, nums: List[int]) -> List[List[int]]:
          
#         pass

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
def sum(nums,target):
     list = []   
     for i in nums:
         if i>=target:
             continue
         y=target-i
         if y in nums:
             z=nums.index(y)
         x=nums.index(i)
         if x==z:
             continue
         list.append(x)
         list.append(z)
         return list
print(sum([1,2,3,4],4))

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

def lengthOfLongestSubstring(ss):
   n=ss[0]
   b=True
   for i in ss:
       if i==n:
           continue
       b=False
   if  b==True:
       return 1
   for i in ss:
       
  
   

print(lengthOfLongestSubstring("aava"))
      

      


      
    
    
    
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。



    



