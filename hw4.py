def rep_char(a,b):
    print(a * b)

def welcome_message(prompt):
    msg1 = 'Hello ' + prompt + ','
    msg2 = 'Welcome to Seoul.'
    if (len(msg1) > len(msg2)):
        nstr = len(msg1)
    else:
        nstr = len(msg2)
    rep_char('-', nstr + 2)
    print(f' {msg1}')
    print(f' {msg2}')
    rep_char('-', nstr + 2)

name = input('Input his/her name: ')
result = welcome_message(name)
