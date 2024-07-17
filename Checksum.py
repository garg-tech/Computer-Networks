from math import log2

def Sender(dataword: int) -> int:
    n = int(log2(dataword)) + 1
    words = []
    for i in range(0,n,4):
        words.append((dataword >> i) & 15)
    words.reverse()
    
    sum = words[0]
    for i in range(1,len(words)):
        sum = sum + words[i]
        carry = sum >> 4
        sum = sum & 15
        sum = sum + carry

    checksum = sum ^ 15
    codeword = (dataword << 4) + checksum

    if(checksum!=0): k = int(log2(checksum)) + 1
    else: k = 1
    add = "0" * (4-k)
    print(f"Sender generated:\nChecksum = {add}{bin(checksum)[2:]}")

    return codeword

def Receiver(codeword: int) -> bool:
    
    print("Receiver:\nReceived Codeword = ", bin(code)[2:])

    n = int(log2(codeword)) + 1
    words = []
    for i in range(0,n,4):
        words.append((codeword >> i) & 15)
    words.reverse()
    
    sum = words[0]
    for i in range(1,len(words)):
        sum = sum + words[i]
        carry = sum >> 4
        sum = sum & 15
        sum = sum + carry
    
    checksum = sum ^ 15
    if(checksum!=0): k = int(log2(checksum)) + 1
    else: k = 1
    add = "0" * (4-k)

    print(f"Generated Checksum = {add}{bin(checksum)[2:]}")

    return (sum == 15)

if __name__ == '__main__':
    data = int(input("Enter the dataword: "), 2)
    codeword = Sender(data)
    code = codeword
    print(f"Codeword = {bin(codeword)[2:]}\n")

    choice = input("Do you want to change the codeword before transmission?\ny/n? ")

    if(choice.capitalize() == 'Y'):
        error_code = int(input("Enter the codeword you wish to transmit: "), 2)
        code = error_code

    print("")

    if(Receiver(code)):
        print("No error in transmission")
    else:
        print("Error in transmission")