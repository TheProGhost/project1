# validating the bitcoin address

def validation(bit_add):
    if bit_add[:2] == "0x":
        bit_add = bit_add[2:]
    else:
        pass

    if (bit_add[0] == "1" or bit_add[0] == "3") and (26 <= len(bit_add) <= 34):
        return True

    elif bit_add[:3] == "bc1" and (42 <= len(bit_add) <= 62):
        return True

    else:
        return False