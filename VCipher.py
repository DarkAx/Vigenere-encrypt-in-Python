#!/usr/bin/env python3
def VCipher(Text, Key, encrypt=False):  
	'''Encrypting & Decrypting Vigenere cipher
	
			Usage : VCipher("Text", "Key")
	
	   To decrypt just pass True argument to the function call 
				such as
				
			VCipher("EncryptMe", "Test123", True)'''


	
	NewText= ""; symbol=0; Key = Key.lower(); alpha=[chr(i) for i in range(97,123)] # Declaring..
	
	if len(Key) != len(Text):
		for i in range(len(Text)-len(Key)): 
			Key+=Key[i]
	
	for i in range(len(Text)):
		Process=Text.lower() # Making the Text temporary lower to make it easy to deal with it. 
		
		if Process[i].isalpha():
			KeyIndex=alpha.index(Key[i-symbol]) # If there was a symbol in the Text it will be substracted
			TextIndex=alpha.index(Process[i]) # from the Key as the function only deals with alphabet.
		

			if encrypt:
				NewText+=alpha[(TextIndex + KeyIndex) % 26]
			
			else:
			
				NewText+=alpha[(TextIndex - KeyIndex)% 26]
		else:
			NewText+=Process[i]
			symbol+=1

	else: # If the for function has succeeded without any errors or break it will do the next.

		Process=""
		for char in range(len(Text)):
				if Text[char].isupper() and NewText[char].islower(): # Here we are converting back 
						Process+=NewText[char].upper()               # any lower character to its 
																	 # original upper one.
				else:   
					Process+=NewText[char]
	
	if encrypt: return "Encrypted text is : "+Process
	
	else: return "Decrypted text is : "+Process
	
