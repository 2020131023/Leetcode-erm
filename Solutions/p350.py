class Solution(object):
  def intersect(self, nums1, nums2):
    ans = []
    nums1.sort()
    nums2.sort()
    i = j = 0
    while i < len(nums1) and j < len(nums2):
      if nums1[i] < nums2[j]:
        i += 1
      elif nums1[i] > nums2[j]:
        j += 1
      else:
        ans.append(nums1[i])
        i += 1
        j += 1

    return ans