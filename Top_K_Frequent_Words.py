class Solution(object):
  def topKFrequent(self, combo, k):
    """
    input: string[] combo, int k
    return: string[]
    """
    # write your solution here
    freq = {}
    for item in combo:
      if item in freq:
        freq[item] += 1
      else:
        freq[item] = 1
    # one way
    #return sorted(freq.keys(), key = lambda x: freq[x], reverse = True)[:k]
    # the other way
    sorted_tuple = sorted(freq.items(), key = lambda x: -x[1])
    return [x[0] for x in sorted_tuple][:k]
