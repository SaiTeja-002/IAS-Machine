#VARIABLES#
memory = [[0 for i in range(40)] for j in range(1000)]

PC  = [0 for i in range(12)]
MBR = [0 for i in range(40)]
IR  = [0 for i in range(8)]
MAR = [0 for i in range(12)]
IBR = [0 for i in range(20)]
AC  = [0 for i in range(40)]
MQ  = [0 for i in range(40)]

k = 1
run = True
####################

#SOME PREREQUISITES#

def binary_int(lst):
    result = int("".join(str(x) for x in lst), 2)
    return result

def empty(lst):
    for i in range(len(lst)):
        if(lst[i] != 0): return False
    return True

def Increment(lst):
    lst = list(lst)
    k = len(lst)
    for i in range(k-1,-1,-1):
        if(lst[i]):
            lst[i] = 0
        else:
            lst[i] = 1
            break
    return lst

def list_string(lst):
    string = ""
    for i in lst:
        string += str(i)
    return string

def take_data(adress,data):
    global memory
    if(data>=0):
        memory[adress] = bin(data)[2:].zfill(40)
    else:
        memory[adress] = bin(data)[3:].zfill(40)
        memory[adress] = list(map(int,list(memory[adress])))    #doubt
        memory[adress][0] = 1

def bin_adress(adress):
    return bin(adress)[2:].zfill(12)

####################
####################

#FUNCTIONS#

def load():
    global MBR,MAR,AC
    MBR = memory[binary_int(MAR)]
    AC  = MBR
    return

def load_mq():
    global AC,MQ
    AC = MQ
    return

def load_mq_mx():
    global MBR,MAR,MQ
    MBR = memory[binary_int(MAR)]
    MQ = MBR
    return

def stor():
    global MBR,AC,MAR
    MBR = AC
    memory[binary_int(MAR)] = MBR
    return

def add():
    global MBR,MAR,AC
    MBR = memory[binary_int(MAR)]
    num = binary_int(MBR)
    AC = list(map(int,list(AC)))    #doubt
    for i in range(num):
        AC = Increment(AC)
    return

def sub():
    global MBR,MAR,AC,k
    MBR = memory[binary_int(MAR)]
    num1 = binary_int(AC)
    num2 = binary_int(MBR)
    if(num1-num2) >= 0: lst = bin(num1-num2)[2:].zfill(40)
    else:
        lst = bin(num1-num2)[3:].zfill(80)
        k = 0
    AC = list(map(int,list(lst)))
    if(k==0): AC[0] = 1
    return

def mul():
    global MBR,MAR,MQ,AC
    MBR = memory[binary_int(MAR)]
    num1 = binary_int(MQ)
    num2 = binary_int(MBR)
    lst = bin(num1*num2)[2:].zfill(80)
    AC  = list(map(int,list(lst[0:40])))
    MQ  = list(map(int,list(lst[40:80])))
    return

def div():
    global MBR,MAR,AC,MQ
    MBR = memory[binary_int(MAR)]
    num1 = binary_int(AC)
    num2 = binary_int(MBR)
    lst1 = bin(int(num1/num2))[2:].zfill(40)
    lst2 = bin(int(num1%num2))[2:].zfill(40)
    MQ = list(map(int,list(lst1)))
    AC = list(map(int,list(lst2)))
    return

def jump_left():    #doubt
    global MBR,MAR,AC,PC,MQ,IBR,IR
    if(AC[0] == 0):
        PC = MAR
        print(list_string(MAR))
    return

####################

####################

#FETCH & EXECUTE#

def fetch():
    global PC,IBR,MAR,IR,MBR,run
    if(empty(memory[binary_int(PC)])): run = False
    else:
        if(empty(IBR)):
            MAR = PC
            MBR = memory[binary_int(MAR)]
            if(empty(MBR[0:8])):
                IR  = MBR[20:28]
                MAR = MBR[28:40]
                PC = Increment(PC)
            else:
                IR  = MBR[0:8]
                MAR = MBR[8:20]
                IBR = MBR[20:40]
        else:    
            IR  = IBR[0:8]
            MAR = IBR[8:20]
            IBR = [0 for i in range(20)]
            PC = Increment(PC)
    return 

def execute():
    global IR, run

    opcode = list_string(IR)

    if(opcode == '00000001'):
        load()
        print('loaded into AC')
    elif(opcode == '00001010'):
        load_mq()
        print('MQ loaded into AC')
    elif(opcode == '00001001'):
        load_mq_mx()
        print('M(X) loaded to MQ')
    elif(opcode == '00100001'):
        stor()
        print('Contents of AC are stored in M(X)')
    elif(opcode == '00000101'):
        add()
        print('Added successfully')
    elif(opcode == '00001011'):
        mul()
        print('Multiplied sucessfully')
    elif(opcode == '00000110'):
        sub()
        print('Subtracted successfully')
    elif(opcode == '00001111'):
        jump_left()
        print('Jumped left successfully')
    elif(opcode == '00001100'):
        div()
        print('Divided successfully')
    else:
        print(opcode)
        print("Error: Opcode Not Found")
        run = False
        return

###################
###################
def Addition(a,b):     
    #MEMORY:
    #   Adress 241 a(10)
    #          242 b(5)
    #          900 c(to be stored)
    #
    #ASSEMBLY CODE:
    #   LOAD(M(241)) ADD(M(242))
    #   STOR(M(900))

    take_data(241,a)
    take_data(242,b)
    
    seg = '00000001' + bin_adress(241) + '00000101' + bin_adress(242)
    memory[0] = list(map(int,list(seg)))

    seg = '00000000' + bin_adress(0) + '00100001' + bin_adress(900)
    memory[1] = list(map(int,list(seg)))

def Subtraction(a,b):
    #MEMORY
    #   Adress 105 a(10)
    #          106 b(5)
    #          900 c(to be stored)
    #
    #ASSEBLY CODE:
    #   LOAD M(105) SUB M(106)
    #   STOR M(900)

    take_data(105,a)
    take_data(106,b)

    seg = '00000001' + bin_adress(105) + '00000110' + bin_adress(106)
    memory[0] = list(map(int,list(seg)))

    seg = '00000000' + bin_adress(0) + '00100001' + bin_adress(900)
    memory[1] = list(map(int,list(seg)))

def Multiply(a,b):
    #MEMORY:
    #   Adress: 301 a
    #           302 b
    #           900 c(to be stored)
    #
    #ASSEMBLY CODE:
    #   LOAD MQ,M(301)  MUL M(302)
    #   LOAD MQ         STOR M(900)

    take_data(301,a)
    take_data(302,b)

    seg = '00001001' + bin_adress(301) + '00001011' + bin_adress(302)
    memory[0] = list(map(int,list(seg)))

    seg = '00001010' + bin_adress(0) + '00100001' + bin_adress(900)
    memory[1] = list(map(int,list(seg)))

def Divide(a,b):
    #MEMORY:
    #   Adress: 421 a
    #           422 b
    #           900 quotient of a and b
    #
    #ASSEMBLY CODE:
    #   LOAD M(421) DIV M(422)
    #   LOAD MQ     STOR M(900)

    take_data(421,a)
    take_data(422,b)

    seg = '00000001' + bin_adress(421) + '00001100' + bin_adress(422)
    memory[0] = list(map(int,list(seg)))

    seg = '00001010' + bin_adress(0)   + '00100001' + bin_adress(900)
    memory[1] = list(map(int,list(seg)))

def Factorial(n):
    #MEMORY:
    #   Adress: 289 n
    #           290 1(temperory)
    #           900 stores  answer
    #
    #ASSEMBLY CODE:
    #   LOAD MQ,M(290) LOAD M(289)
    #   ADD(M(290)) MUL M(289)
    #   LOAD M(289) SUB M(290)
    #   STOR M(289) SUB M(290)
    #   JUMP+M(1,left) 
    #   LOAD MQ     STOR M(900)

    take_data(289,n)
    take_data(290,1)

    seg = '00001001' + bin_adress(290) + '00000001' + bin_adress(289)
    memory[0] = list(map(int,list(seg)))

    seg = '00000101' + bin_adress(290) + '00001011' + bin_adress(289)
    memory[1] = list(map(int,list(seg)))

    seg = '00000001' + bin_adress(289) + '00000110' + bin_adress(290)
    memory[2] = list(map(int,list(seg)))

    seg = '00100001' + bin_adress(289) + '00000110' + bin_adress(290)
    memory[3] = list(map(int,list(seg)))

    seg = '00000000' + bin_adress(0)   + '00001111' + bin_adress(1)
    memory[4] = list(map(int,list(seg)))

    seg = '00001010' + bin_adress(0)   + '00100001' + bin_adress(900)
    memory[5] = list(map(int,list(seg)))


###################

###################
def start(key):
    global run

    if(key == '+'):
        print('Opted Addition of two numbers')
        print('Input Numbers')
        x = int(input())
        y = int(input())
        Addition(x,y)
    
    elif(key == '-'):
        print('Opted Subtraction of two numbers')
        print('Input Bigger Number')
        x = int(input())
        print('Input Smaller Number')
        y = int(input())
        Subtraction(x,y)

    elif(key == 'x'):
        print('Opted for multiplication of two numbers')
        print('Input Numbers')
        x = int(input())
        y = int(input())
        Multiply(x,y)

    elif(key == '/'):
        print('Opted for division of two numbers')
        print('Input Numerator')
        x = int(input())
        print('Input Denominator')
        y = int(input())
        Divide(x,y)

    elif(key == '!'):
        print('Opted for factorial of number')
        print('Input Number')
        x = int(input())
        Factorial(x)

    else:
        print('Invalid Option')
        run = False

    while(run):
        print('Fetching...')
        fetch()
        print('Fetching Completed')
        if(run):
            execute()
            print('Completed Execution')
            print('\n')
    
    if(run==False):
        print('Execution ended')
        print('\nAnswer in M(900) is ' + str(binary_int(memory[900])))
        print("Program Terminated")

    print("Thank you")
    return
###################
########MENU#######

print("Please enter only non-negative integers")
print('***MENU***\n')
print('PRESS : ! to perform factorial of a number')
print('PRESS : + to perform sum of two numbers')
print('PRESS : - to perforn subtraction of two numbers')
print('PRESS : x to perform multiplication of two numbers')
print('PRESS : / to perform integral division of two numbers')


key = str(input())
start(key)

