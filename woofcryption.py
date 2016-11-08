from Crypto import Random
from Crypto.Cipher import AES
import base64
import md5

#hashmaps/dictionaries that contain the corresponding woofwoof, each one is unique
#has ascii and woof dict and woof and ascii dict
translateDict = {'+': 'WoofWOOF', '/': 'WooFWoOF', '1': 'wooFWoof', '0': 'WOOFwOOf', '3': 'WOOfWoof', '2': 'wOofWoOF', '5': 'wooFWOoF', '4': 'WOofWOoF', '7': 'WoOfWOOF', '6': 'WOOfwoof', '9': 'WOoFwoof', '8': 'wOoFwOOF', '=': 'wooFwOoF', 'A': 'WoOfwoOF', 'C': 'wOOFwOOf', 'B': 'WooFWOoF', 'E': 'WoofwoOf', 'D': 'woofWOOf', 'G': 'WOoFwOOF', 'F': 'woofwoOf', 'I': 'woOFWoOF', 'H': 'WOofwoOF', 'K': 'WOoFWoOF', 'J': 'wOOfWOof', 'M': 'WOOfWOoF', 'L': 'WoofWooF', 'O': 'wOofwOOf', 'N': 'WOOfWoOf', 'Q': 'woOFwOOf', 'P': 'wOOFWoof', 'S': 'wooFwoof', 'R': 'woofWoof', 'U': 'woOFWoof', 'T': 'wOOfWOOF', 'W': 'WOOFwoOF', 'V': 'WOOFWOOf', 'Y': 'woOfwOoF', 'X': 'wOoFWoOF', 'Z': 'WOoFWoOf', 'a': 'wOofwoOF', 'c': 'woofwOof', 'b': 'wOOfWOoF', 'e': 'WoOfWoOF', 'd': 'wOofWOoF', 'g': 'wooFWoOf', 'f': 'WOoFwOoF', 'i': 'wOOfwoOF', 'h': 'Woofwoof', 'k': 'woOFWOOf', 'j': 'wOoFwoOF', 'm': 'WOoFWoof', 'l': 'wOoFwoof', 'o': 'WoofwOoF', 'n': 'wOOfwOof', 'q': 'WoofWOoF', 'p': 'woofWooF', 's': 'WOOfWoOF', 'r': 'woOFwOoF', 'u': 'wooFWOof', 't': 'wOOfwoOf', 'w': 'wOoFWOOF', 'v': 'woOfWoOF', 'y': 'woofwOOF', 'x': 'woOfWOOF', 'z': 'WoOFwooF'}
reverseTranslate = {'WoofwoOf': 'E', 'wOofwoOF': 'a', 'wooFWOof': 'u', 'wooFWoOf': 'g', 'wOOfwoOf': 't', 'woOFWOOf': 'k', 'wOoFWoOF': 'X', 'woofwOof': 'c', 'woofWOOf': 'D', 'woOfWOOF': 'x', 'WoOfwoOF': 'A', 'wOoFwOOF': '8', 'WOOFWOOf': 'V', 'wooFWOoF': '5', 'WooFWOoF': 'B', 'WOoFWoOF': 'K', 'woofWooF': 'p', 'woOfwOoF': 'Y', 'wooFWoof': '1', 'woOFWoOF': 'I', 'wooFwOoF': '=', 'WOOfwoof': '6', 'wOoFwoof': 'l', 'WOoFwoof': '9', 'WOoFwOOF': 'G', 'wOOFWoof': 'P', 'wooFwoof': 'S', 'woofwoOf': 'F', 'WOoFwOoF': 'f', 'wOofWoOF': '2', 'wOOfWOOF': 'T', 'wOoFwoOF': 'j', 'WoOFwooF': 'z', 'woofwOOF': 'y', 'WOOFwoOF': 'W', 'wOOfwoOF': 'i', 'WOOfWoOF': 's', 'wOOfWOof': 'J', 'wOoFWOOF': 'w', 'wOOfwOof': 'n', 'WoOfWOOF': '7', 'WOOfWoof': '3', 'WOOFwOOf': '0', 'WOOfWoOf': 'N', 'WOoFWoof': 'm', 'woOFWoof': 'U', 'WOoFWoOf': 'Z', 'woofWoof': 'R', 'WOofWOoF': '4', 'wOofWOoF': 'd', 'WoofWOOF': '+', 'WoofWOoF': 'q', 'WOofwoOF': 'H', 'WOOfWOoF': 'M', 'wOofwOOf': 'O', 'wOOFwOOf': 'C', 'woOFwOoF': 'r', 'WoofWooF': 'L', 'WoofwOoF': 'o', 'wOOfWOoF': 'b', 'WooFWoOF': '/', 'WoOfWoOF': 'e','woOfWoOF': 'v', 'woOFwOOf': 'Q', 'Woofwoof': 'h'}

#creates md5 hash based on key used b/c of AES
def trans(key):
    return md5.new(key).digest()

inp = raw_input("encrypt or decrypt?")
key = trans("quack")


#conditionals to check whether user wants to encrypt or decrypt
if inp=="encrypt":
    
    #reads plaintext input and generates a random block of mem to set aside

    x = raw_input("please enter the string you want to encrypt")
    IV = Random.new().read(16)
    
    #AES encrypts text but the return contains special characters so it is converted
    #to base64 for readibility and hashtables, the hashtable/dictionary can 
    #be expanded up to 256
    aes = AES.new(key, AES.MODE_CFB, IV)
    string = base64.b64encode(IV +aes.encrypt(x))
    print(string)
    
    #here is where the magic happens, it checks the hashmaps above then creates
    #a string with only woofwoof and each unique character has it's own woofwoof
    trueString = ''
    for s in string:
        trueString = trueString + translateDict[s] + ' '

    print trueString




elif inp == "decrypt":
    
    #reads user input and splits it based on spaces between woofs
    x=raw_input("enter string to decode")
    temp = x.split(' ')
    translatedString = ''
    
    #converts the string back to base64 then back to AES
    for i in temp:
        translatedString = translatedString + reverseTranslate[i]
    encrypted = base64.b64decode(translatedString)

    #Same process as above but AES decrypts it this time
    IV = encrypted[:AES.block_size]
    aes = AES.new(key, AES.MODE_CFB, IV)
    print(aes.decrypt(encrypted[AES.block_size:]))