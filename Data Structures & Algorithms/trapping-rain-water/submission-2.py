class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        l_max=height[left]
        r_max=height[right]
        m_area=0
        while left < right:
            if l_max < r_max:
                area=l_max-height[left]
                left+=1
                l_max=max(l_max, height[left])
            else:
                area=r_max-height[right]
                right-=1
                r_max=max(r_max, height[right])

            if area>0:
                m_area+=area

        return m_area

            

        