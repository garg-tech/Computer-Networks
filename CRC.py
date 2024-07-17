from math import log2
from random import randrange

def Sender(dataword: int, key: int) -> int:
    n = int(log2(dataword)) + 1
    k = int(log2(key)) + 1
    codeword = dataword << (k-1)
    temp = key << (n-1)
    remainder = codeword ^ temp
    n -= 1
    while(n>0):
        temp = key << (n-1)
        if(remainder & (1<<(n+k-2))):
            remainder = remainder ^ temp
        else:
            remainder = remainder ^ 0
        n -= 1
    
    codeword = codeword + remainder
    return codeword

def Receiver1(codeword: int, key: int) -> bool:
    flipbits = int(input("How many bits to flip? "))
    n = int(log2(codeword)) + 1
    k = int(log2(key)) + 1
    flip = 0
    tmp = n
    while(flipbits>0):
        pos = randrange(n)
        while(pos==tmp):
            pos = randrange(n)
        tmp = pos
        flip = flip | (1 << pos)
        flipbits -= 1
        print(f"Bit flipped at position: {pos+1}")
    
    codeword = codeword ^ flip
    t = int(log2(codeword)) + 1
    add = ""
    if(t < n):
        add = "0" * (n-t)
    
    print(f"Receiver received Codeword = {add}{bin(codeword)[2:]}")
    temp = key << (n-k)
    remainder = codeword ^ temp
    n -= 1
    while(n>=k):
        temp = key << (n-k)
        if(remainder & (1<<(n-1))):
            remainder = remainder ^ temp
        else:
            remainder = remainder ^ 0
        n -= 1
    
    return (remainder != 0)

def Receiver2(codeword: int, key: int) -> bool:
    chances = int(input("How many times to flip? "))
    n = int(log2(codeword)) + 1
    k = int(log2(key)) + 1
    i = 0
    while( 2*i < (n-1) and chances > 0):
        codeword = codeword ^ ((1 << i) | (1 << (n-i-1)))
        i += 1
        chances -= 1

    t = int(log2(codeword)) + 1
    add = ""
    if(t < n):
        add = "0" * (n-t)
    
    print(f"Receiver received Codeword = {add}{bin(codeword)[2:]}")
    temp = key << (n-k)
    remainder = codeword ^ temp
    n -= 1
    while(n>=k):
        temp = key << (n-k)
        if(remainder & (1<<(n-1))):
            remainder = remainder ^ temp
        else:
            remainder = remainder ^ 0
        n -= 1
    
    return (remainder != 0)

def Receiver3(codeword: int, key: int) -> bool:
    distance = int(input("Enter distance to flip the bits: "))
    n = int(log2(codeword)) + 1
    k = int(log2(key)) + 1
    t = n - 1
    while(t >= 0):
        codeword = codeword ^ (1 << t)
        t -= distance
    
    t = int(log2(codeword)) + 1
    add = ""
    if(t < n):
        add = "0" * (n-t)
    
    print(f"Receiver received Codeword = {add}{bin(codeword)[2:]}")
    temp = key << (n-k)
    remainder = codeword ^ temp
    n -= 1
    while(n>=k):
        temp = key << (n-k)
        if(remainder & (1<<(n-1))):
            remainder = remainder ^ temp
        else:
            remainder = remainder ^ 0
        n -= 1
    
    return (remainder != 0)

if __name__ == '__main__':
    data = int(input("Enter the dataword: "), 2)
    key = int(input("Enter the generator key: "), 2)
    code = Sender(data, key)
    print(f"Sender generated Codeword = {bin(code)[2:]}")

    choice = int(input("Select one:\n1. Flip one or more random bits.\n2. Flip two extreme bits\n3. Flip two bits with given distance.\n"))

    error = True
    if(choice == 1):
        error = Receiver1(code, key)
    elif(choice == 2):
        error = Receiver2(code, key)
    elif(choice == 3):
        error = Receiver3(code, key)

    if(error):
        print("Error was detected")
    else:
        print("No error was detected!")
