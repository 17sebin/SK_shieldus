import hashlib
import time

def md5(string):
    return hashlib.md5(string.encode()).hexdigest()[:2]

def generate_coupon(member_id, md5_hash):
    char_set = ["S", "e", "y", "o", "n", "g", "-", "K", "i", "m"]
    prefix = "Eqst"
    
    # Generate couponfront
    time_part = '1009'
    couponfront = ''.join(char_set[int(digit)] for digit in time_part)
    
    # Generate couponmiddle
    asciisum = 810 + sum(ord(char) for char in member_id)
    asciisum = str(asciisum).zfill(4)
    couponmiddle = ''.join(char_set[int(digit)] for digit in asciisum)
    
    # Generate MD5 hash of the first 13 characters of the coupon number
    for i in range(128):  # Iterate through all possible characters
        md5_partial = chr(i)
        coupon_number = prefix + couponfront + couponmiddle + md5_partial
        input_md5 = hashlib.md5(coupon_number.encode()).hexdigest()[:2]
        if input_md5 == md5_hash:
            return coupon_number + md5_hash
        else:
            print("no")
    
    return None

# Example usage
member_id = "test9"
md5_hash = "17"
valid_coupon_number = generate_coupon(member_id, md5_hash)
if valid_coupon_number:
    print("Valid Coupon Number:", valid_coupon_number)
else:
    print("Unable to generate a valid coupon number.")