# Your Name Here: Rikart Yeimo
# UWYO COSC 1010
# Submission Date: 11/21/2024
# Lab XX
# Lab Section: 10
# Sources, people worked with, help given to: 
# your
# comments
# here

#import modules you will need 





# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

from hashlib import sha256 
from pathlib import Path
def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()
def crack_password():
    try:
        with open("hash", "r") as hash_file:
            stored_hash = hash_file.read().strip()
    except FileNotFoundError:
        print("It's error: the file hash cannot be found.")
        return
    except Exception as e:
        print(f"unexpectted error reading 'hash': {e}")
        return

    try:
        with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as password_file:
            password_list = password_file.readlines()
    except FileNotFoundError:
        print("It's Error: The file 'rockyou.txt' cannot be found.")
        return
    except Exception as e:
        print(f"error found from 'rockyou.txt': {e}")
        return
    else:
        print("passsword is succesfully found in'rockyou.txt'.")

    for password in password_list:
        password = password.strip() 
        hashed_password = get_hash(password)

        if hashed_password == stored_hash:
            print(f"Password found: {password}")
            break
    else:
        print("The password is not matching with the 'rocktext you'")
    
if __name__ == "__main__":
    crack_password()
        

       
