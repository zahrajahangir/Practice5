# Note "pip install ipfsapi Pillow"
import ipfsapi
from PIL import Image

# Connect to the local IPFS node.
api = ipfsapi.connect('127.0.0.1', 5001)

# Add the photo to IPFS and obtain its hash.
def add_photo_to_ipfs(photo_path):
    with open(photo_path, 'rb') as photo_file:
        photo_data = photo_file.read()
    result = api.add_bytes(photo_data)
    return result

# Get the photo from IPFS using the hash and display it.
def get_and_display_photo_from_ipfs(photo_hash):
    photo_data = api.cat(photo_hash)
    with open('temp_photo.jpeg', 'wb') as temp_file:
        temp_file.write(photo_data)
    image = Image.open('temp_photo.jpeg')
    image.show()

# Use the functions to add and display the photo.
photo_path = 'flower.jpeg'
photo_hash = add_photo_to_ipfs(photo_path)
print(f"The photo hash is: {photo_hash}")
get_and_display_photo_from_ipfs(photo_hash)
