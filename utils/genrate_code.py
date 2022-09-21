import random



def generate_code():
    lenth = 8
    numper = '0123456789'
    code = ''.join(random.choice(numper) for x in range(lenth))
    return code