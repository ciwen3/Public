#!/usr/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ceasar( offset ):
	newmsg = ''
	msg = input('Please enter a message to encrypt: ').lower()
	for character in msg:
		if character in alphabet:
			position = alphabet.find(character)
			newposition = (position + offset) % 26
			newcharacter = alphabet[newposition]
			newmsg += newcharacter
		else:
			newmsg += character
	print('the encrypted message is: ', newmsg)
	input('Press Enter to Close Window')

startmsg = int(input('Do you want to Encrypt or Decrypt? \n 1 for Encrypt \n 2 for Decrypt \n 3 to Close the Program \n'))

if startmsg == 1:
	offset = int(input('choose cipher offset: '))
	ceasar(offset)
elif startmsg == 2:
	offset = - int(input('choose cipher offset: '))
	ceasar(offset)
else:
	raise SystemExit