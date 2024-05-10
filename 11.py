import hashlib
import random

def md5(s):
    return hashlib.md5(s).hexdigest()

def generate_coupon(member_id, md5_hash):
    char_set = ["S", "e", "y", "o", "n", "g", "-", "K", "i", "m"]
    
    # Generate random time part
    time_part = ''.join(random.choice(char_set) for _ in range(4))
    
    # Calculate coupon middle
    asciisum = 810 + sum(ord(char) for char in member_id)
    couponmiddle = ''.join(char_set[int(char)] for char in str(asciisum).zfill(4))
    
    # Construct coupon number
    prefix = "Eqst"
    coupon_number = prefix + time_part + couponmiddle + md5_hash
    
    return coupon_number

# Given member ID and MD5 hash
member_id = b"test9"  # Use bytes instead of string
md5_hash = b"d7"       # Use bytes instead of string

# Generate and print valid coupon number
valid_coupon_number = generate_coupon(member_id, md5_hash)
print("Valid Coupon Number:", valid_coupon_number)