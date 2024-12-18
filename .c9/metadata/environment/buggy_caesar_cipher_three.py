{"filter":false,"title":"buggy_caesar_cipher_three.py","tooltip":"/buggy_caesar_cipher_three.py","undoManager":{"mark":30,"position":30,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, cipherKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":36,"column":36},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "],"id":3},{"start":{"row":36,"column":36},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["#"],"id":4}],[{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":[" "],"id":5}],[{"start":{"row":37,"column":57},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["t"]},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":["h"]},{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"remove","lines":["e"],"id":7},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"remove","lines":["h"]},{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"remove","lines":["t"]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["#"],"id":8}],[{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":[" "],"id":9},{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["t"]},{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["h"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":[" "],"id":10},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["b"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["u"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["g"]}],[{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":[" "],"id":11},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["i"]},{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":[" "],"id":12},{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":["w"]},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":[" "],"id":13},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["a"]},{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":["r"]},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"insert","lines":[" "],"id":14},{"start":{"row":38,"column":24},"end":{"row":38,"column":25},"action":"insert","lines":["n"]},{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"insert","lines":["o"]},{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":[" "],"id":15},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["c"]},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"insert","lines":["a"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"insert","lines":["l"]},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"insert","lines":["l"]},{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"insert","lines":["i"]},{"start":{"row":38,"column":33},"end":{"row":38,"column":34},"action":"insert","lines":["n"]},{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["g"]}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":[" "],"id":16},{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["d"]},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["e"]},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["c"]},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"remove","lines":["r"],"id":17},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"remove","lines":["c"]},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"remove","lines":["e"]},{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"remove","lines":["d"]}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["e"],"id":18},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["n"]},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["c"]},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"insert","lines":["r"]},{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"insert","lines":["y"]},{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"insert","lines":["p"]}],[{"start":{"row":38,"column":42},"end":{"row":38,"column":43},"action":"insert","lines":[" "],"id":19},{"start":{"row":38,"column":43},"end":{"row":38,"column":44},"action":"insert","lines":["f"]},{"start":{"row":38,"column":44},"end":{"row":38,"column":45},"action":"insert","lines":["u"]},{"start":{"row":38,"column":45},"end":{"row":38,"column":46},"action":"insert","lines":["n"]},{"start":{"row":38,"column":46},"end":{"row":38,"column":47},"action":"insert","lines":["c"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"insert","lines":["t"]},{"start":{"row":38,"column":48},"end":{"row":38,"column":49},"action":"insert","lines":["i"]},{"start":{"row":38,"column":49},"end":{"row":38,"column":50},"action":"insert","lines":["o"]},{"start":{"row":38,"column":50},"end":{"row":38,"column":51},"action":"insert","lines":["n"]}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":[" "],"id":20},{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["r"]},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["e"]},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["v"]},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"insert","lines":["e"]},{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"insert","lines":["r"]},{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"insert","lines":["s"]},{"start":{"row":38,"column":42},"end":{"row":38,"column":43},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":59},"end":{"row":38,"column":60},"action":"insert","lines":[" "],"id":21},{"start":{"row":38,"column":60},"end":{"row":38,"column":61},"action":"insert","lines":["w"]},{"start":{"row":38,"column":61},"end":{"row":38,"column":62},"action":"insert","lines":["i"]},{"start":{"row":38,"column":62},"end":{"row":38,"column":63},"action":"insert","lines":["t"]},{"start":{"row":38,"column":63},"end":{"row":38,"column":64},"action":"insert","lines":["h"]}],[{"start":{"row":38,"column":64},"end":{"row":38,"column":65},"action":"insert","lines":[" "],"id":22},{"start":{"row":38,"column":65},"end":{"row":38,"column":66},"action":"insert","lines":["t"]},{"start":{"row":38,"column":66},"end":{"row":38,"column":67},"action":"insert","lines":["h"]},{"start":{"row":38,"column":67},"end":{"row":38,"column":68},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":68},"end":{"row":38,"column":69},"action":"insert","lines":[" "],"id":23}],[{"start":{"row":38,"column":69},"end":{"row":38,"column":70},"action":"insert","lines":["d"],"id":24},{"start":{"row":38,"column":70},"end":{"row":38,"column":71},"action":"insert","lines":["e"]},{"start":{"row":38,"column":71},"end":{"row":38,"column":72},"action":"insert","lines":["c"]},{"start":{"row":38,"column":72},"end":{"row":38,"column":73},"action":"insert","lines":["r"]},{"start":{"row":38,"column":73},"end":{"row":38,"column":74},"action":"insert","lines":["y"]},{"start":{"row":38,"column":74},"end":{"row":38,"column":75},"action":"insert","lines":["p"]},{"start":{"row":38,"column":75},"end":{"row":38,"column":76},"action":"insert","lines":["k"]},{"start":{"row":38,"column":76},"end":{"row":38,"column":77},"action":"insert","lines":["e"]},{"start":{"row":38,"column":77},"end":{"row":38,"column":78},"action":"insert","lines":["y"]}],[{"start":{"row":38,"column":77},"end":{"row":38,"column":78},"action":"remove","lines":["y"],"id":25},{"start":{"row":38,"column":76},"end":{"row":38,"column":77},"action":"remove","lines":["e"]},{"start":{"row":38,"column":75},"end":{"row":38,"column":76},"action":"remove","lines":["k"]}],[{"start":{"row":38,"column":75},"end":{"row":38,"column":76},"action":"insert","lines":["K"],"id":26},{"start":{"row":38,"column":76},"end":{"row":38,"column":77},"action":"insert","lines":["e"]},{"start":{"row":38,"column":77},"end":{"row":38,"column":78},"action":"insert","lines":["y"]}],[{"start":{"row":38,"column":78},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":57},"action":"insert","lines":["# return encryptMessage(message, cipherKey, alphabet)"],"id":28}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":[" "],"id":29},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":["#"]}],[{"start":{"row":39,"column":35},"end":{"row":39,"column":44},"action":"remove","lines":["cipherKey"],"id":30},{"start":{"row":39,"column":35},"end":{"row":39,"column":36},"action":"insert","lines":["d"]},{"start":{"row":39,"column":36},"end":{"row":39,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":35},"end":{"row":39,"column":37},"action":"remove","lines":["de"],"id":31},{"start":{"row":39,"column":35},"end":{"row":39,"column":45},"action":"insert","lines":["decryptKey"]}]]},"ace":{"folds":[],"scrolltop":370.00000762939453,"scrollleft":0,"selection":{"start":{"row":36,"column":36},"end":{"row":36,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":36,"state":"start","mode":"ace/mode/python"}},"timestamp":1734531450043,"hash":"5c7ab00c2088b5212e3669e4054c9055d7bb02e2"}