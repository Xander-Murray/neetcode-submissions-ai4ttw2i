class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # initialize count dict
        freq = [[] for i in range(len(nums) + 1)] # make a list of lists size of length nums + 1

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            #simple frequency dict
        for num, cnt in count.items():
            freq[cnt].append(num)
            # append num to frequeny list nested count list

        res = [] # what we are returninng
        # hos is freq sorted so that when we iterate backwards its in order 
        #iterate backwards since it will be in order now and append ot result
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # checkf if len is == to k means we added the k elements of highest frequency
                if len(res) == k:
                    return res