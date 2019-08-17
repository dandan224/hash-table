class Solution(object):
  def countAndSay(self, n):
    """
    input: int n
    return: string
    """
    # write your solution here
    if n == 1:
      return '1'
    if n == 2:
      return '11'
    # we generate the item base on the previous item
    s = '11'
    for i in range(3, n+1):
      s += '$'
      l = len(s) 
      temp = ''
      count = 1
      prev = s[0]
      for j in range(1, l):
        if s[j] == prev:
          count += 1
        else:
          temp += str(count)
          temp += prev
          count = 1
          prev = s[j]
      s = temp
    return s
