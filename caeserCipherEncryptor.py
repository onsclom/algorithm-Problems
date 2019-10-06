def caesarCipherEncryptor(string, key):
	new=[]
	for x in list(string):
		curAscii = ord(x)
		curAscii -= ord('a')
		curAscii += key
		#26 letters... so %26 to get 0-25
		curAscii = curAscii%26
		curAscii += ord('a')
		
		new.append(chr(curAscii))
		
	return "".join(new)
	
