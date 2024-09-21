# Komalpreet Kuar

# Part 1
import time
from PIL import Image
print("Part 1:")

# Step 1: Generate the number (n)
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print("Generated Number (n):", generated_number)

# Step 2: Open the image and check its mode
input_image = Image.open(r'C:/Users/hp/Downloads/Chapter1.png')  # Load the input image

# Convert the image to RGB if it's not in RGB mode
if input_image.mode != 'RGB':
    input_image = input_image.convert('RGB')

pixels = input_image.load()  # Get pixel data of the image
width, height = input_image.size

# Create a new image to store the modified pixels
output_image = Image.new('RGB', (width, height))

red_pixel_sum = 0  # Initialize the sum of red pixel values

# Loop through each pixel, modify, and calculate the sum of red values
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]  # Unpack the pixel values (r, g, b)
        # Modify the pixel values by adding the generated number (n)
        new_r = min(r + generated_number, 255)  # Ensure pixel values don't exceed 255
        new_g = min(g + generated_number, 255)
        new_b = min(b + generated_number, 255)
        
        # Update the red pixel sum
        red_pixel_sum += new_r
        
        # Set the new pixel values in the output image
        output_image.putpixel((x, y), (new_r, new_g, new_b))

# Step 3: Save the modified image
output_image.save('chapter1out.png')
print("Modified image saved as 'chapter1out.png'.")

# Step 4: Output the sum of red pixel values
print("Sum of red pixel values in the new image:", red_pixel_sum)

#part 2
print("Part 2:")

def separate_and_convert(input_string):
    # Separate numbers and letters
    number_string = ''.join([char for char in input_string if char.isdigit()])
    letter_string = ''.join([char for char in input_string if char.isalpha()])

    # Extract even numbers and convert to ASCII
    even_numbers = [char for char in number_string if int(char) % 2 == 0]
    even_numbers_ascii = [ord(char) for char in even_numbers]
    
    # Extract uppercase letters and convert to ASCII
    uppercase_letters = [char for char in letter_string if char.isupper()]
    uppercase_letters_ascii = [ord(char) for char in uppercase_letters]

    # Print the results
    print(f"Number string: {number_string}")
    print(f"Letter string: {letter_string}")
    print(f"Even numbers: {even_numbers}")
    print(f"ASCII codes for even numbers: {even_numbers_ascii}")
    print(f"Uppercase letters: {uppercase_letters}")
    print(f"ASCII codes for uppercase letters: {uppercase_letters_ascii}")

# Example scenario
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0*'
separate_and_convert(input_string)

def decrypt_caesar_cipher(ciphered_text, shift_key):
    decrypted_text = ''
    
    for char in ciphered_text:
        # Process only alphabetic characters
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character back by the shift_key
            decrypted_char = chr((ord(char) - ascii_offset - shift_key) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            # Keep non-alphabetic characters as they are
            decrypted_text += char

    return decrypted_text

# Example usage of the Caesar cipher decryption:
ciphered_quote = 'VZ FRYSVFU VZNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY'
shift_key = 1  # Start with a shift key, and you can try different values until you find the correct one

decrypted_quote = decrypt_caesar_cipher(ciphered_quote, shift_key)
print(f"Decrypted text with shift key {shift_key}: {decrypted_quote}")

