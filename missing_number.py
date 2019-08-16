# why set, it's fast
class Solution(object):
  def missing(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    
    array = set(array)
    N = len(array) + 1
    for num in range(1, N + 1, 1):
      if num not in array:
        return num
    return -1
