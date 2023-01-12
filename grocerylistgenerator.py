import time
list = []

def listprint():
    print()
    time.sleep(1.5)
    print('Writing your list, please hold...')
    waiting = '...'
    for dots in waiting:
        print(dots,end='')
        time.sleep(0.5)
    print('\nHere is your grocery list:')
    time.sleep(0.5)
    for index in range(len(list)):
        if index != (len(list)-1):
            print(list[index], end=', ')
        else:
            print('and', list[-1])
    time.sleep(1.5)
    print('\nThanks for using our services!')
        

titleScreen = '‿︵‿︵‿︵‿ GROCERY LIST GENERATOR ‿︵‿︵‿︵‿ \n\n\n'
for squiggly in titleScreen:
    print(squiggly, end='')
    time.sleep(0.05)

print("(^０^)ノ Hello! I'll be your helper in creating your custom grocery list!")
time.sleep(1.0)

while True:
    time.sleep(0.7)
    print("So, let's begin.")
    time.sleep(1)
    print('How many items you want your list to have? Please type it below!')
    try:
        size = int(input()) - 1
        print('Please insert the items for your list: (',size + 1,' items)',sep='')
        while True:
            grocery = input()
            if grocery != '' and len(list) < size:
                list = list + [grocery]
                print('!', grocery, ' has been added to the list!')
            elif len(list) == size:
                list = list + [grocery]
                print('!', grocery, ' has been added to the list!')
                time.sleep(0.5)
                print('Your list is full!')
                listprint()
                break
            else:
                print('There are still items left to insert!')
                continue
        break
    except ValueError:
        print('Please enter a valid number! (╯°益°)╯彡┻━┻')
        time.sleep(0.5)
        continue