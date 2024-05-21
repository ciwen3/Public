

alphabet = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
newmsg = ''

startmsg = int(input('Do you want to Encrypt or Decrypt? \n 1 for Encrypt \n 2 for Decrypt \n 3 to Close the Program \n'))

if startmsg == 1:
	posoffset = int(input('choose cipher offset: '))
	enmsg = input('Please enter a message to encrypt: ')
	for character in enmsg:
		if character in alphabet:
			position = alphabet.find(character)
			newposition = (position + posoffset) % 26
			newcharacter = alphabet[newposition]
			newmsg += newcharacter
		elif character in caps:
			position = caps.find(character)
			newposition = (position + posoffset) % 26
			newcharacter = caps[newposition]
			newmsg += newcharacter
		else:
			newmsg += character
	print('the encrypted message is: ', newmsg)
	input('Press Enter to Close Window')
elif startmsg == 2:
	negoffset = - int(input('choose cipher offset: '))
	demsg = input('Please enter a message to decrypt: ')
	for character in demsg:
		if character in alphabet:
			position = alphabet.find(character)
			newposition = (position + negoffset) % 26
			newcharacter = alphabet[newposition]
			newmsg += newcharacter
		elif character in caps:
			position = caps.find(character)
			newposition = (position + negoffset) % 26
			newcharacter = caps[newposition]
			newmsg += newcharacter
		else:
			newmsg += character
	print('the encrypted message is: ', newmsg)
	input('Press Enter to Close Window')
else:
	raise SystemExit


#hi there
#kl wkhuh







