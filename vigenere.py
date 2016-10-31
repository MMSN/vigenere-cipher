alphabet = [",","-",".","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e",
            "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
            "w","x","y","z"]

alphabet2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
            "R","S","T","U","V","W","X","Y","Z"]


def generatingNewKey(s, n, string):
    out = string
    subsecret =  string[::-1]
    aux = string
    secret = subsecret
    totalSize = n-1
    begin = 0
    gate = 0;
    #//cout << s << n << endl;
    while (totalSize < s-1):
        #print secret[begin]
        if (begin == n-1):
            gate = 1
        if (secret[begin] >= 'A' and secret[begin] <= 'Z'):
            out += secret[begin]
        else:
             if(secret[begin] >= 'a' and secret[begin] <= 'z'):
                 out += secret[begin]
        if (gate == 1):
            begin = -1
            subsecret =  secret[::-1]
            aux = secret
            secret = subsecret
            gate = 0
        begin+= 1

        totalSize +=1
    return out

# def asciiEncrpytion(msg, newSecret):
#     saida = ""
#     for i in range(len(msg)):
#         print i
#         h = (ord(msg[i]) - 65) + (ord(newSecret[i]) - 65)
#         h = h % 26
#         print("%c", h + 65)
#         char = h + 65
#         saida = saida + chr(char)
#     print saida

def alphabetEncryption(msg, newSecret):
    out = ""
    for i in range(len(msg)):
        #print msg,msg[i],newSecret,newSecret[i]
        h = alphabet.index(msg[i]) + alphabet.index(newSecret[i])
        h = h % 55;
        result = alphabet[h]
        out = out + result
    #print out
    return out

def alphabetDecryption(msg, newSecret):
    out = ""
    for i in range(len(msg)):
        #print msg,msg[i],newSecret,newSecret[i]
        h = alphabet.index(msg[i]) - alphabet.index(newSecret[i])
        h = h % 55;
        result = alphabet[h]
        out = out + result
    #print out
    return out


if __name__ == '__main__':
    secret = "Florida"
    msg = str(raw_input("Please enter the message you would like to encrypt? "))

    if len(msg) > len(secret):
        newSecret = generatingNewKey(len(msg), len(secret), secret)
    else:
        newSecret = secret

    #print newSecret
    #print msg
    encrypted = alphabetEncryption(msg, newSecret)
    decrypted = alphabetDecryption(encrypted, newSecret)

    print "This is our Key:",newSecret
    print "Ciphertext: ",encrypted
    print "Plain Text: ",decrypted
