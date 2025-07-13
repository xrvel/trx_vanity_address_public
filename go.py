import ecdsa
import hashlib
import base58
import argparse
import secrets
import time
from eth_hash.auto import keccak  # pip install eth-hash

def generate_private_key():
    return secrets.token_bytes(32)

def private_key_to_uncompressed_pubkey_bytes(private_key):
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return vk.to_string()  # X + Y (64 bytes)

def public_key_to_tron_address(pubkey_bytes):
    keccak_digest = keccak(pubkey_bytes)
    last20 = keccak_digest[-20:]
    address = b'\x41' + last20
    checksum = hashlib.sha256(hashlib.sha256(address).digest()).digest()[:4]
    address_with_checksum = address + checksum
    return base58.b58encode(address_with_checksum).decode()

def match_address(address, prefix, suffix, case_sensitive):
    addr_to_check = address
    if not case_sensitive:
        addr_to_check = addr_to_check.lower()
        if prefix:
            prefix = prefix.lower()
        if suffix:
            suffix = suffix.lower()

    prefix_match = True
    suffix_match = True

    if prefix:
        prefix_match = addr_to_check[1:].startswith(prefix)
    if suffix:
        suffix_match = addr_to_check.endswith(suffix)

    return prefix_match and suffix_match

def main(prefix, suffix, case_sensitive):
    attempts = 0
    start_time = time.time()

    while True:
        private_key = generate_private_key()
        pubkey_bytes = private_key_to_uncompressed_pubkey_bytes(private_key)
        address = public_key_to_tron_address(pubkey_bytes)
        attempts += 1

        if match_address(address, prefix, suffix, case_sensitive):
            total_time = time.time() - start_time
            speed = attempts / total_time if total_time > 0 else 0
            print(f"\n✅ Found after {attempts} attempts!")
            print(f"Address: {address}")
            print(f"Private Key (hex): {private_key.hex()}")
            print(f"⏱ Time spent: {total_time:.2f} seconds")
            print(f"⚡ Speed: {speed:.2f} attempts/sec")

            # Save result to file
            with open("vanity_result.txt", "a") as f:
                f.write(f"Address: {address}\n")
                f.write(f"Private Key: {private_key.hex()}\n")
                f.write(f"Attempts: {attempts}\n")
                f.write(f"Time spent: {total_time:.2f} sec\n")
                f.write(f"Speed: {speed:.2f} attempts/sec\n")
                f.write("-----\n")
            break

        if attempts % 1000 == 0:
            elapsed = time.time() - start_time
            speed = attempts / elapsed if elapsed > 0 else 0
            print(
                f"Attempts: {attempts:,}, latest: {address}, "
                f"elapsed: {elapsed:,.2f} sec, "
                f"prefix: {prefix or '-'}, suffix: {suffix or '-'}, case_sensitive: {case_sensitive}"
            )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TRON Vanity Address Generator (enhanced with stats)")
    parser.add_argument('--prefix', type=str, help='Desired prefix (starts after the T)')
    parser.add_argument('--suffix', type=str, help='Desired suffix')
    parser.add_argument('--case-sensitive', action='store_true', help='Enable case-sensitive matching')
    args = parser.parse_args()

    if not args.prefix and not args.suffix:
        print("❌ Please provide at least a prefix or a suffix using --prefix PREFIX or --suffix SUFFIX (e.g. --prefix ai).")
    else:
        main(args.prefix, args.suffix, args.case_sensitive)
