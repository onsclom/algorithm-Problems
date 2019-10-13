def balancedBrackets(string):
    brackets = list()
	
    for char in string:
    	if char == ')':
    		if len(brackets) == 0 or brackets.pop(len(brackets)-1) != '(':
    			return False
    	elif char == ']':
    		if len(brackets) == 0 or brackets.pop(len(brackets)-1) != '[':
    			return False
    	elif char == '}':
    		if len(brackets) == 0 or brackets.pop(len(brackets)-1) != '{':
    			return False
    	else:
    		brackets.append(char)
		
    return len(brackets) == 0
