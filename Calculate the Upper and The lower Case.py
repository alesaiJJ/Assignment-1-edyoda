x = 'The quick Brow Fox'
def ascii(uppercase = 0,lowercase = 0):
    for i in x:
        if ord(i) in range(65,90):
            uppercase += 1
        elif ord(i) in range(97,122):
            lowercase += 1
    return uppercase, lowercase
print(ascii())
