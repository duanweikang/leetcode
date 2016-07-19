#3. longest substring without repeating characters

# so we keep three numbers, start, result, end, we iterate each substring element use for loop
# with each step, we add 1 to end, thus use end as the index to store we are now.
# we use a dictionary to store the count of each element, if the element count is larger than 1
# then we have one substring, we need to move start index to the right of first occurence and delete the count 
# of each iterated element since we are going to loop some elements from the start index and these elements are 
# going to be iterated again. then once we catch a substring, we calculate length and then update to the largest 
# number that we can have.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initiate
        result, start, end = 0,0,0
        count = {}
        for i in s:
            end += 1
            # add 1 after each iterate
            count[i] = count.get(i,0)+1
            # if certain element appears two times
            while count[i] > 1:
                # clear every interation to 0 besides the same string element
                count[s[start]] -= 1
                # move start to the right of first occurence so that we can count from the count from that position next time.
                start += 1
            result = max(result, end-start)
        return result
            