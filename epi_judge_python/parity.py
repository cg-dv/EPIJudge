from test_framework import generic_test


def parity(x: int) -> int:
    # Assuming word size is 64 bits, successively XOR x with x >> 2^(lg(n)-1) 
    # return parity of last bit, the result 
    x ^= x >> 32
    x ^= x >> 16 
    x ^= x >> 8 
    x ^= x >> 4 
    x ^= x >> 2 
    x ^= x >> 1 
    return x & 1 


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
