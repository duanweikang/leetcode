### since this doesn't allow us to use extra space, therefore, we can't just convert it to string.
### we can just iterate from two sides, and check two sides digits one by one, if they are same, we keep going
### if they are not same, we return false
### after the iteration, if false is not returned, which indiates that it is a palindrome
### the trick is in each step, how to get rid of the leftmost digits and rightmost digits
### we keep a number called div and use this to get the leftmost digit by doing x/div
### after the check in each step, we can use x%div to get rid of leftmost digit, and then (x%div)/10 to get rid of the right most digit

def isPalindrome(self,x):
	if x < 0:
		return False
	# get the div
	div = 1
	while x/div >= 10:
		div = div*10
	# div equals to the 10*number of digits of x, e.g. if x = 131, then div = 100

	# iterate over the whole number, and in each step, compare leftmost and rightmost digit
	while x:
		left = x/div
		right = x%10

        # if not then not a palindrome
		if left != right:
			return False
        
        # get rid of rightmost digit and leftmost digit
        x = (x%div)/10
        # since we kicked out rightmost digit and leftmost digit, we lost two digit, 
        # we thus need to shrink div by two digits
        div = div/100

    return True


