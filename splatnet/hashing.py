import hashlib
import os

# Data to hash
password = "my_secure_password"

# Generate a random salt
salt = os.urandom(16)  # 16-byte salt

# Combine password and salt
data = password.encode() + salt

# Hash the combined data
hash_object = hashlib.sha256()
hash_object.update(data)

# Get the hashed password with salt
hashed_password = hash_object.hexdigest()

print(f"Salt: {salt.hex()}")
print(f"Hashed Password with Salt: {hashed_password}")