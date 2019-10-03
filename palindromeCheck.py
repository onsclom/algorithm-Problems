def isPalindrome(string):
    for x in range(len(string)//2):
    	if string[x]!=string[len(string)-1-x]:
    		return False    
    return True
