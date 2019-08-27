# by using hash-table
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
  
  # by using heap method 
  class Solution(object):
  def topKFrequent(self, combo, k):
    """
    input: string[] combo, int k
    return: string[]
    """
    # write your solution here
    # by using heap
    import heapq
    freq = {}
    for num in combo:
      if num in freq:
        freq[num] += 1
      else:
        freq[num] = 1
    heap = [(-freqrent, word) for word, freqrent in freq.items()]
    heapq.heapify(heap)

    return [item[1] for item in heap][:k]
