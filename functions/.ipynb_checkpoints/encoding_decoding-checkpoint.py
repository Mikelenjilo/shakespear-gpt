# encoding of character to integer.
def encode(chars, string):
    encode_dict = { ch:i for i, ch in enumerate(chars) }
    return [encode_dict[c] for c in string]


# decoding of integer to character.
def decode(chars, list_int):
    decode_dict = { i:ch for i, ch in enumerate(chars) } 
    return ''.join([decode_dict[n] for n in list_int])