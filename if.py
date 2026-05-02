def ask_ok(prompt, retries=4, reminder= 'please try later'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
Result = ask_ok("Do you want to continue: ")
print("Result: ", Result)


        

