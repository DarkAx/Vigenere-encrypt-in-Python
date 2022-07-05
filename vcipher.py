#!/usr/bin/env python3
def encrypt(text,key):
	import string
	key = key.lower(); final=""; cipher=""; symbol=0; al=[chr(i) for i in range(97,123)]
	
	if not key.isalpha():
		return "Key must consist of letters"

	if len(key) != len(text):
		for i in range(len(text)-len(key)):
			key+=key[i]
	i=0
	while i < len(text):
		process=text.lower()
		if text[i].isalpha():
			cipher+=al[(al.index(process[i])+al.index(key[i-symbol])) % 26]
		else:
			cipher+=process[i]
			symbol+=1
		i+=1

	for counter in range(len(text)):
			if text[counter].isupper() and cipher[counter].islower():
					final+=cipher[counter].upper()

			else:
					final+=cipher[counter]
	return "Encrypted text is : "+final
