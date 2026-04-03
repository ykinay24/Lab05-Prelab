def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """

    def _expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""

    for i in range(len(s)):
        odd_pal = _expand_around_center(i, i)
        even_pal = _expand_around_center(i, i + 1)

        if len(odd_pal) > len(longest):
            longest = odd_pal
        if len(even_pal) > len(longest):
            longest = even_pal

    if len(longest) <= 1:
        return ""

    return longest
