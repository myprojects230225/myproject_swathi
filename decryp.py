import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")  # Load PNG (no compression loss)

# Read the stored password
with open("password.txt", "r") as f:
    saved_password = f.read().strip()

# Ask user for the passcode
pas = input("Enter passcode for Decryption: ")

# Dictionary to convert numbers back to letters
c = {i: chr(i) for i in range(256)}

# If the password is correct, extract the hidden message
if pas == saved_password:
    message = ""
    n = 0
    m = 0
    z = 0

    for _ in range(len(img) * len(img[0])):  # Loop through enough pixels
        pixel_value = int(img[n, m, z])  # Convert NumPy value to integer
        if pixel_value == 255:  # Stop at end marker
            break
        message += c[pixel_value]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through R, G, B

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
