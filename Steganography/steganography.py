# Image-based Steganography using Least Significant Bit (LSB) method

from PIL import Image
import stepic

example_image_path = "example_image.png"
message = "This is a secret message!"

example_image = Image.open(example_image_path).convert("RGBA")
message_bytes = message.encode()

steganography = stepic.encode(example_image, message_bytes)

steganographic_image_path = "steganographic_image.png"

steganography.save(steganographic_image_path)

steganographic_image = Image.open(steganographic_image_path)
decoded_message = stepic.decode(steganographic_image)

print ("Decoded message: ", decoded_message)