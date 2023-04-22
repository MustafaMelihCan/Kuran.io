

def sureler(string):
    string = string.split('<option value=')
    listofsureler = []
    for sure in string:
        first_ind = sure.rfind(' ')
        last_ind = sure.rfind('(')
        sure = sure[first_ind+1:last_ind].lower()
        listofsureler.append(sure)
    return listofsureler

def characterfixer(L):
    wrongL = ['â','û','ü',"'",'î','i̇',"’"]
    correct = ['a','u','u','','i','i','']
    L1 = []
    for sure in L:
        for char in sure:
            if char in wrongL:
                ind = wrongL.index(char)
                sure = sure.replace(char,correct[ind])
        if 'i̇' in sure:
            sure = sure.replace('i̇','i')
        L1.append(sure)
    return L1
