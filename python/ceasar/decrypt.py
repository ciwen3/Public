

alphabet = 'abcdefghijklmnopqrstuvwxyz12345'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ67890'
msg = 'jyvzzpunaolybipjvunfzpthre'
for offset in range(1,26):
    newmsg = ''
    for character in msg:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position + offset) % 31
            newcharacter = alphabet[newposition]
            newmsg += newcharacter
        elif character in caps:
            position = caps.find(character)
            newposition = (position + offset) % 31
            newcharacter = caps[newposition]
            newmsg += newcharacter
        else:
            newmsg += character
    print('the decrypted message is: ', newmsg)
    print("")

        

