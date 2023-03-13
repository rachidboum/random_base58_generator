import random
import itertools
import os

# Define the allowed characters for the password
allowed_chars = "123456789ABCDEFGHJKMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

# Define the desired length of the password
desired_length = int(input("Enter desired password length: "))

# Define the maximum file size in bytes
max_file_size = 50 * 1024 * 1024  # 50 MB in bytes

# Initialize the current file size and file counter
current_file_size = 0
file_counter = 1

# Open the first file for writing
output_file = open(f"possible_keys_{file_counter}.txt", "w")

# Generate keys and write to file
for key in itertools.product(allowed_chars, repeat=desired_length):
    key_str = ''.join(key) + '\n'
    
    # Check if writing the key to the current file would exceed the maximum file size
    if current_file_size + len(key_str) > max_file_size:
        # Close the current file and open a new one
        output_file.close()
        file_counter += 1
        output_file = open(f"possible_keys_{file_counter}.txt", "w")
        current_file_size = 0
    
    # Write the key to the current file
    output_file.write(key_str)
    current_file_size += len(key_str)

# Close the output file
output_file.close()

# Print a message to indicate that key generation is complete
print("Key generation complete.")
