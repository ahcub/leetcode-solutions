class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        n = 2 * n + 1
        lps_lengths = [0] * n
        lps_lengths[0] = 0
        lps_lengths[1] = 1
        center = 1
        right = 2
        max_lps_length = 1
        max_lps_center_position = 1

        for i in range(2,n):
            i_mirror = 2*center-i
            lps_lengths[i] = 0
            diff = right - i
            if diff > 0:
                lps_lengths[i] = min(lps_lengths[i_mirror], diff)

            try:
                while ((i+lps_lengths[i]) < n and (i-lps_lengths[i]) > 0) and \
                        (((i+lps_lengths[i]+1) % 2 == 0) or (s[(i+lps_lengths[i]+1)//2] == s[(i-lps_lengths[i]-1)//2])):
                    lps_lengths[i] += 1
            except:
                pass

            if lps_lengths[i] > max_lps_length:
                max_lps_length = lps_lengths[i]
                max_lps_center_position = i

            if i + lps_lengths[i] > right:
                center = i
                right = i + lps_lengths[i]

        start = (max_lps_center_position - max_lps_length) // 2
        end = start + max_lps_length - 1
        return s[start:end+1]

print(Solution().longestPalindrome("a"))
