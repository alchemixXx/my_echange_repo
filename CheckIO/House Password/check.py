#!/usr/bin/env python
def lenght(password):
    if len(password) >= 10:
        return True

def upper(password):
    for i in password:
        if ord(i) in range(65, 91):
            return True

def digit(password):
    for i in password:
        if ord(i) in range(48, 58):
            return True

def checkio(password):
    if lenght(password) and upper(password) and digit(password):
        return True
    else:
        return False


print(checkio('QwErTy911poqqqq'))



# checkio('A1213pokl') == False
# checkio('bAse730onE') == True
# checkio('asasasasasasasaas') == False
# checkio('QWERTYqwerty') == False
# checkio('123456123456') == False
# checkio('QwErTy911poqqqq') == True