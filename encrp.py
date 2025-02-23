import cv2
import os

# Load the image
img = cv2.imread("pic.jpg")  # Use a high-quality image

# Get the secret message and password from the user
msg = input("Enter secret message: ") + chr(255)  # Add an end marker
password = input("Enter a passcode: ")

# Creating a dictionary to convert letters to numbers
d = {chr(i): i for i in range(256)}

# Variables to track pixel position
m, n, z = 0, 0, 0

# Hiding the message inside the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3  # Switch between R, G, and B

# Save as PNG instead of JPG (PNG keeps pixel values exact)
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Opens the image on Windows

# Save the password
with open("password.txt", "w") as f:
    f.write(password)

print("Encryption complete! Your message is hidden inside encryptedImage.png.")
