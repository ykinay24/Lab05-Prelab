def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a_val = a[2:]
    b_val = b[2:]
    
    i = len(a_val) - 1
    j = len(b_val) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        bit_a = ord(a_val[i]) - ord('0') if i >= 0 else 0
        bit_b = ord(b_val[j]) - ord('0') if j >= 0 else 0
        
        total = bit_a + bit_b + carry
        carry = total // 2
        
        result.append(chr((total % 2) + ord('0')))
        
        i -= 1
        j -= 1
        
    res_str = "".join(result[::-1]).lstrip('0')
    
    return "0b" + (res_str if res_str else "0")
