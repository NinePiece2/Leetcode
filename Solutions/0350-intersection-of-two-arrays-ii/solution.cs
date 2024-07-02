public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        Dictionary<int, int> elementCounts = new Dictionary<int, int>();

        // Count occurrences of each element in nums1
        foreach (int num in nums1)
        {
            if (elementCounts.ContainsKey(num))
            {
                elementCounts[num]++;
            }
            else
            {
                elementCounts.Add(num, 1);
            }
        }

        List<int> commonElements = new List<int>();

        // Find common elements in nums2
        foreach (int num in nums2)
        {
            if (elementCounts.ContainsKey(num) && elementCounts[num] > 0)
            {
                commonElements.Add(num);
                elementCounts[num]--; // Decrement the count
            }
        }

        return commonElements.ToArray();
    }


    
}
