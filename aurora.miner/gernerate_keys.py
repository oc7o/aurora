import binascii
import json

from nacl.signing import SigningKey

address_private = SigningKey.generate()
address_public = address_private.verify_key
address_public_string = binascii.hexlify(address_public.encode()).decode()
address_private_string = binascii.hexlify(address_private.encode()).decode()
print("Public:", address_public_string)
print("Private:", address_private_string)

