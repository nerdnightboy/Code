# Function for hexadecimal to binary
# value = "AB12"

def hexadecimalToBinary(value):
    # Initializing a dictionary
    dic = {'0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111"
    }
    # Initilizing an empty string
    binaryVal=""
    for i in range(len(value)):
        binaryVal = binaryVal + dic[value[i]]
    return binaryVal

# print(hexadecimalToBinary(value))

# value = "00001111"
# Function for Binary to Hexadecimal
def binaryToHexadecimal(value):
    dic={"0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1110": 'E',
        "1111": 'F'
    }
    hexadecimal=""
    for i in range(0, len(value), 4):
        binary = "" 
        binary = binary + value[i] # grouping four binary digits
        binary = binary + value[i+1]
        binary = binary + value[i+2]
        binary = binary + value[i+3]
        hexadecimal = hexadecimal + dic[binary]
    return hexadecimal

# print(binaryToHexadecimal(value))

# val = 101
# Function for Binary to Decimal
def binaryToDecimal(binaryValue):
    decimalVal = 0
    i = 0
    
    while(binaryValue != 0):
        rem = binaryValue % 10  # fetching last digit
        decimalVal = decimalVal + rem * pow(2, i)  # adding decimalVal values according to bit position
        binaryValue = binaryValue // 10
        i += 1
    return decimalVal

# print(binaryToDecimal(val))

# Decimal to binary conversion
# val = 4
def decimalToBinary(decimalValue):
    binary = bin(decimalValue).replace("0b", "") # convert decimal number to binary string and the remove prefix
    if(len(binary) % 4 != 0): #check if length of the binary number is not divisible by 4 
        div = decimalValue / 4 #calculate integer division
        div = int(div) #calculate result to integer
        counter = (4 * (div + 1)) - len(binary) #calculate number of zeros need to make it an binary number divisible by 4
        for i in range (0, counter): #adding number of zeros needed
            binary = '0' + binary
    return binary
# print(decimalToBinary(val))

# Function for permutation
def permute(k, arr, n):
    permutation=""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1] #Takes the character at index arr[i] - 1 from the string k and appends it to the permutation string
    return permutation

# Function to left shift bits by n steps
def leftShift(k, nshift):
    shifted = ""
    for i in range(nshift):
        for j in range (1, len(k)):
            shifted = shifted + k[j]
        shifted = shifted + k[0]
        k = shifted
        shifted = ""
    return k

#  Function to calculate XOR of two string values
def xor(a, b):
    xorRes = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            xorRes = xorRes + "0"
        else:
            xorRes = xorRes + "1"
    return xorRes


# Table of Position of 64 bits at initial level: Initial Permutation Table, This permutation to be used for initital permutation to be used in plain text
initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7
                ]

# Expansion box Table
expansion_box = [32, 1, 2, 3, 4, 5, 4, 5,
        6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27,
        28, 29, 28, 29, 30, 31, 32, 1
        ]
# Straight Permutation Table
permutation_table = [16,  7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25
        ]
# S-box Table
substitutionbox = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],

        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],

        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],

        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],

        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],

        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],

        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],

        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

# Final Permutation Table
final_permutation = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]


plaintext = "123456ABCD132536" #This is our plain text 64 bit
key = "AABB09182736CCDD" #This is our 64bit key 

#---------------------KEY GENERATION-----------------------------
# Convert Hexadecimal key to Binary
binarykkey = hexadecimalToBinary(key)
# print(binaryKey)

# parity bit drop table so m
dropparitykeytable = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# permute the 64bit initial key into 56 bit key where 64bits divided into 8*8 groups and 8th bit dropped from each group
permutedchoice1key = permute(binarykkey, dropparitykeytable, 56)

# split the 56bit permutedkey into two parts each 28bits
left = permutedchoice1key[0:28]
right = permutedchoice1key[28:56]

roundkeybinary = [] #initilizing an array to store each round key in binary
roundkeyhexadecimal = [] #initilizing an array to store each round key in hexadecimal

# bit shift table for each round out of 16 where only in 1,2,9,16th round 1bit left shift else 2bit left shift
shifttable = [1,1,2,2,
            2,2,2,2,
            1,2,2,2,
            2,2,2,1]

# Key- Compression Table : Compression of key from 56 bits to 48 bits
keycompressiontable = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

# key generating part in which we divide our 56 bit key into two and then left shift and send it to for another permutation
for i in range (0, 16): #Generating key for all the 16 rounds and store them into roundkey arrays
    left = leftShift(left, shifttable[i]) #Shifting our key's left and right part of each 28 bit accourding to the shift table
    right = leftShift(right, shifttable[i])

    # Combining left and right bits after performing shift operation
    combinekeybits = left +right
    # Compress the key size from 56 to 48 by using permutation and key compression table
    roundkey = permute(combinekeybits, keycompressiontable, 48) #permute 2

    # adding each round key to our arrays which will store 16 round keys
    roundkeybinary.append(roundkey)
    roundkeyhexadecimal.append(binaryToHexadecimal(roundkey)) #convert binary key to hexadecimal and append

# -------------------------------ENCRYPTION FUNCTION----------------------------------------------------------
# there a part of process called fiestel round
def encryption(plaintext, roundkeybinary, roundkeyhexadecimal):


    plaintext = hexadecimalToBinary(plaintext) #convert plaintext into binary

    plaintext = permute(plaintext, initial_permutation, 64)

    print("Plain Text after Initial Permutation", binaryToHexadecimal(plaintext))

    # Split the block cipher into two each 32 bit
    left = plaintext[0:32]
    right = plaintext[32:64]

    for i in range(0, 16): #right half of the black ciper will go into expansion box so that 32bit can be expanded to 48 bit
        rightexpand = permute(right, expansion_box, 48) #expanding 32 bit into 48 bit with the help of expansion_box table
        xorwithkey = xor(rightexpand, roundkeybinary[i]) #performing xor operation with the help of xor function with permuted choice 2 result

        # Substitution Box work
        # Substitution the value from s-box table by calculating row and column
        substitutionboxstring = ""  #initializing blank string
        for j in range (0, 8):
            row = binaryToDecimal(int(xorwithkey[j*6] + xorwithkey[j*6+5])) #fethcing 1st and last bit of 6 bit output then converting to decimal for finding the column accourding to that decimal number from substitution box table
            col = binaryToDecimal(int(xorwithkey[j * 6 + 1] + xorwithkey[j * 5 + 2] + xorwithkey[j * 5 + 3])) #fethcing 2nd, 3rd and 5th bit output then converting to decimal for finding the row accourding to that decimal number from substitution box table
            value = substitutionbox[j][row][col]
            substitutionboxstring = substitutionboxstring + decimalToBinary(value)

        # to rearrange bits after substitution we again permute with the straight permutation table
        substitutionboxstring = permute(substitutionboxstring, permutation_table, 32)

        # we again xor the substitutionboxstring 32bit and left bits of plain text  32bits
        result = xor(left, substitutionboxstring)
        left = result

        # in next step we use swapping here so that our left 32bits will be right and right 32bits will be left 32bits for the nex round and here our ########fiestel round ends
        if(i != 15):
            left, right = right, left
        

        print("Round ", i+1, "32 Left bits: ", binaryToHexadecimal(left), "32 right bits: ", binaryToHexadecimal(right), "Round ", i+1, " key:", roundkeyhexadecimal[i])

    combinebits = left + right

    # Using final permutation table we again rearrange the bits to get cipher text because we permuted our bits inittially so we need to finally inverse that initial permutation
    encryptedciphertext = permute(combinebits, final_permutation, 64)
        
    return encryptedciphertext
# ----------------------------------------END ENCRYPTION--------------------------------------------

print("Encryption Running")
ciphertext = binaryToHexadecimal(encryption(plaintext, roundkeybinary, roundkeyhexadecimal))

print("Cipher Text: ", ciphertext)

# -------------------------------------DECRYPTION--------------------------------------------------
print("Decryption Running")
roundkeybinaryreverse = roundkeybinary[::-1] #reversing roundkeybinary
roundkeyhexadecimalreverse = roundkeyhexadecimal[::-1] #reverse of the key
# instead of writing decryption we just inversed our key of 48bit and call the encryption function so we get our plain text by our reverse process
decrypttex = binaryToHexadecimal(encryption(ciphertext, roundkeybinaryreverse, roundkeyhexadecimalreverse))

print("Plain Text: ", decrypttex)

# ------------------------------------DECRYPTION END--------------------------------------------------------------