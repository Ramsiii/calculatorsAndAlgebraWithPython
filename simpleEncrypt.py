def encrypt_string(text):
    encrypted = []
    for c in text:
#  Checks if `c` is a letter different from 'z' and 'Z'. 
# If so, converts it to asci, increments it by 1, converts it back, and appends it to encrypted.
        if c.isalpha() and c not in 'zZ':
            charFromOrdPlus1 = ((ord(c)) + 1)
            encrypted.append(chr(charFromOrdPlus1))
        # If 'c' is 'z', changes it to 'a'. If 'c' is 'Z', change it to 'A'. Appends each one to encrypted
        elif c == 'z':
            encrypted.append('a')
        elif c == 'Z':
            encrypted.append('A')
        else:
            encrypted.append(c)
            
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
    return ''.join(encrypted)


if __name__ == '__main__':
    # Encrypt the string "Hello, Python!"
    encrypted_text = encrypt_string("Hello, Python!")
    print("The encrypted text is:", encrypted_text) # Should print out "Ifmmp, Qzuipo!" 