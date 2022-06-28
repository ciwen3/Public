import binascii


path = "/home/strat0m/Python/Test.txt"

def file_to_bits():
    bin_data = open(path, 'rb').read()
    bits = bin(int(binascii.hexlify(bin_data), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

print(file_to_bits())

