import binascii

def file_to_bits():
    path1 = "/home/strat0m/Python/Test.txt"
    file1=open(path1,"rb")
    number=list(file1.read())
    print (number)
    file1.close()
#    bin_data = open(path, 'rb').read()
    bits = bin(int(binascii.hexlify(number), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

print(file_to_bits())


path2 = "/home/strat0m/Python/Testing.txt"

file2=open(path2,"wb")
# num=[2,4,6,8,10]
array=bytearray(number)
file2.write(array)
file2.close()



