
import cv2
import string

# Load the encrypted image
#img = cv2.imread("encryptedImage.jpg")  # Make sure to use the correct path

# Retrieve the passcode from the user
pas = input("Enter passcode for Decryption: ")

# Read the password from the file
with open('password.txt', 'r') as f:
    saved_password = f.read()

# Check if the passcode matches
if saved_password == pas:
    # Initialize variables
    m = 0
    n = 0
    z = 0
    message = ""

    # Decrypt the message from the image
    for i in range(len(msg)):  # Ensure the length of 'msg' is correct
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
