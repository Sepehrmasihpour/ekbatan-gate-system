from pin_utils.core import generate_encrypted_pin
import time

# Example: generate a PIN valid for 5 days across 3 blocks
expiry = int(time.time()) + 5 * 86400
secret = "MY_SECRET_KEY_2025_06"
blocks = ["B1", "B2", "MARKET"]

pin = generate_encrypted_pin(blocks, expiry, secret)
print("Generated PIN:", pin)
