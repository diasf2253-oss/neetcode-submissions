class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for number in nums:
            if number in hashmap:
                hashmap[number] += 1
            else: 
                hashmap[number] = 1
        result = []
        for i in range(k):
            top = max(hashmap, key=hashmap.get)
            result.append(top)
            del hashmap[top]
        return result