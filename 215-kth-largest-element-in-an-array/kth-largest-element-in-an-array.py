class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # the approaches to use minimum heap and by doing so what we do is keep the largest element at the top and at any point if the length of the array goes greater then K, we just remove it so always we will have the Kth element on the top. We only push elements in the heap when its length is less than K.
        #TC - O(nlogK)
        #SC - O(logK)
        # heap=[]

        # for num in nums:
        #     if len(heap)<k:
        #         heapq.heappush(heap, num)
        #     else:
        #         heapq.heappushpop(heap, num)
        # return heap[0]

        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            print(pivot)
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)
