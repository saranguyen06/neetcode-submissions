class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #frequency map
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #list of groups, freq[i] stores all nums appearing i times
        freq = [[] for i in range(len(nums) + 1)]
        for n, cnt in count.items():
            freq[cnt].append(n)

        results = []
        #loop from largest freq (end of freq) to 1
        for i in range(len(freq) -1, 0, -1): 
            for n in freq[i]:
                results.append(n)
                if len(results) == k:
                    return results
        