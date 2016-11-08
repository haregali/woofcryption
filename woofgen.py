from random import randint

listWoof = ['wOOf', 'WOoF', 'wOOF', 'Woof', 'wOof', 'WoOf', 'wooF', 'woOF', 'WooF', 'woOf', 'woof', 'WOOf', 'WOOF', 'WOof', 'wOoF', 'WoOF']
listChar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','=']
dictHash = dict()
ranInt1 = 0
ranInt2 = 0
woofString = ''

k = 0
while k < len(listChar):
    woofString = listWoof[randint(0,15)]
    while len(woofString) != 8:
        woofStr = listWoof[randint(0,15)]
        if woofStr not in woofString:
            woofString = woofString + woofStr
    if woofString not in dictHash.values():
        dictHash[listChar[k]] = woofString
        k = k+1
    else:
        k = k-1
reverse = dict((v,k) for k, v in dictHash.iteritems())
print("Original: " + str(dictHash) + "\n")
print("Reverse(for decoding): " + str(reverse))