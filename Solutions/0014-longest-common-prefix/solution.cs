public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string firstStr = strs[0];

        for (int i = 0; i < firstStr.Length; i++) {
            char c = firstStr[i];
            for (int j = 1; j < strs.Length; j++) {
                if (i >= strs[j].Length || strs[j][i] != c) {
                    return firstStr.Substring(0, i);
                }
            }
        }

        return firstStr;
    }
}
