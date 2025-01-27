#!/usr/bin/env python3

import os

def create_file_with_zeros(size_in_kb, file_format):
    # Convert KB to bytes
    size_in_bytes = size_in_kb * 1024
    
    # Create a file with all zeros
    with open(f"all_zeros.{file_format}", "wb") as file:
        # Write magic numbers and format based on the file format
        if file_format == "png":
            file.write(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A')  # PNG magic numbers
        elif file_format == "jpg":
            file.write(b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01')  # JPEG magic numbers
        elif file_format == "mp3":
            file.write(b'\xFF\xFB')  # MP3 magic numbers
        elif file_format == "wav":
            file.write(b'\x52\x49\x46\x46\x00\x00\x00\x00\x57\x41\x56\x45\x66\x6D\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00\x44\xAC\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00\x64\x61\x74\x61')  # WAV magic numbers
        elif file_format == "docx":
            file.write(b'\x50\x4B\x03\x04')  # DOCX magic numbers
        elif file_format == "xlsx":
            file.write(b'\x50\x4B\x03\x04')  # XLSX magic numbers
        elif file_format == "pptx":
            file.write(b'\x50\x4B\x03\x04')  # PPTX magic numbers
        elif file_format == "zip":
            file.write(b'\x50\x4B\x03\x04')  # ZIP magic numbers
        elif file_format == "7z":
            file.write(b'\x37\x7A\xBC\xAF\x27\x1C')  # 7z magic numbers
        elif file_format == "rar":
            file.write(b'\x52\x61\x72\x21\x1A\x07\x00')  # RAR magic numbers
        elif file_format == "txt":
            file.write(b'')  # TXT has no magic numbers
        elif file_format == "csv":
            file.write(b'')  # CSV has no magic numbers
        elif file_format == "exe":
            file.write(b'\x4D\x5A')  # EXE magic numbers
        elif file_format == "elf":
            file.write(b'\x7F\x45\x4C\x46')  # ELF magic numbers
        elif file_format == "pdf":
            file.write(b'\x25\x50\x44\x46')  # PDF magic numbers
        elif file_format == "iso":
            file.write(b'\x43\x44\x30\x30\x31')  # ISO magic numbers
        elif file_format == "img":
            file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')  # IMG magic numbers
        else:
            print("Unsupported file format. Creating file with zeros only.")
        
        # Write the zeros for the data
        file.write(b'\x00' * (size_in_bytes - file.tell()))

# Ask the user for the desired size in KB
size_in_kb = int(input("Enter the desired size of the file in KB: "))

# Ask the user for the file format
file_format = input("Enter the desired file format (png, jpg, mp3, wav, docx, xlsx, pptx, zip, 7z, rar, txt, csv, exe, elf, pdf, iso, img): ").lower()

# Create the file with all zeros and magic numbers
create_file_with_zeros(size_in_kb, file_format)

print(f"File 'all_zeros' created with {size_in_kb} KB of zeros and {file_format} format.")
