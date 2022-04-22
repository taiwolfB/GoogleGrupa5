cnp = input()

S = cnp[0]
AA = cnp[1:3]
LL = cnp[3:5]
ZZ = cnp[5:7]
JJ = cnp[7:9]
NNN = cnp[9:12]
C = cnp[12]

validation = '279146358279'


def calculateValid():
    result = 0
    for i in range(12):
        result += int(cnp[i]) * int(validation[i])
    if result % 11 == 10:
        return 1
    return result % 11


def isValidCnp(cnp):
    if len(cnp) != 13:
        return False
    elif S == '0':
        return False
    elif NNN == '000':
        return False
    elif int(C) != calculateValid():
        return False
    return True


print(isValidCnp(cnp))