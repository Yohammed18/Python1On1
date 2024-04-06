# Given an interger, return an integer that is reverse ordering numbers

def reverse_int(num):
    reversed_str = str(num)[::-1] if num >= 0 else str(num)[1:][::-1]
    
    reverse_num = int(reversed_str) if num >= 0 else -int(reversed_str)
    
    return reverse_num







if __name__ == '__main__':
    print('ex_reverse_int.py\n')
    print(reverse_int(-9))
    