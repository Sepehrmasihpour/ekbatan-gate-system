from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import time


def generate_encrypted_pin(
    block_ids: list[str], expiry_ts: int, secret_key: str, pin_length=10
) -> str:
    block_string = "-".join(block_ids)  # e.g., "B1-B2-B5"
    data = f"{block_string}|{expiry_ts}"

    key = secret_key.encode("utf-8")[:32].ljust(32, b"\0")
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(data.encode("utf-8"), 16)
    encrypted = cipher.encrypt(padded)
    encoded = base64.b32encode(encrypted).decode("utf-8")

    return encoded[:pin_length]


def validate_encrypted_pin(
    pin: str, secret_key: str, block_id: str, current_time: int = None
) -> bool:
    if current_time is None:
        current_time = int(time.time())

    key = secret_key.encode("utf-8")[:32].ljust(32, b"\0")

    try:
        # Decode + decrypt
        # Because we truncated the PIN, this part only works if you save full PINs or use longer versions
        # So for now: expect full base32 input for actual use
        raise NotImplementedError(
            "Short PINs cannot be decrypted unless you store the full encrypted blob"
        )

    except Exception as e:
        print("PIN validation failed:", e)
        return False
