#RSA,Method

alf = {'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ё':7,'ж':8,'з':9,'и':10,'й':11,'к':12,'л':13,'м':14,'н':15,'о':16,'п':17,'р':18,'с':19,'т':20,'у':21,'ф':22,'х':23,'ц':24,'ч':25,'ш':26,'щ':27,'ъ':28,'ы':29,'ь':30,'э':31,'ю':32,'я':33}
key = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,47,53,59,61,67,71,73,79,83,97,101,103,107,109,113,127,131,137,149,151,157,163,167,173,179,181,191,197,199,211,223,227,229,233,239,241,257,263,269,271,277,281,283,293,307,313,317,331,337,347,349,353,359,367,379,383,389,397,401,409,419,421,431,439,443,449,457,461,463,467,479,487,499,503,509,521,523,541,547,557,563,571,577,587,593,599]
alf_sym = []
alf_num = []
message_mas = []
p = 0
k = 0
mod = 0
fi = 0
e = 0
d = 0

massive = []
clear_massive = []
p_true = False
q_true = False


while True:
    p = int(input('Введите число p (*простое число от 1 до 599*): '))
    q = int(input('Введите число q (*простое число от 1 до 599*): '))
    if(p != q):
        for i in key:
            if(p == i):
                print('    └─>Число p соответсвует требованиям')
                p_true = True
                break
        if(p_true == True):
            for i in key:
                if(q == i):
                    print('    └─>Число q соответсвует требованиям')
                    q_true = True
                    break
    if(p_true != True):
         print('    └─>Число p НЕ соответсвует требованиям')
    if(q_true != True):
         print('    └─>Число q НЕ соответсвует требованиям')
    if(q_true == True and p_true == True):
        break

mod = p*q
fi = (p-1)*(q-1)
print('Первое число публичного и секретного ключа: ',mod)
print('Значение ф-ции Эйлера: ',fi)
for i in key:
    if(i<fi):
        massive.append(i)
#print('    └─>Массив чисел меньших ',fi,' -> ',massive,' кол-во числел -> ',len(massive))

for j in range(0,len(massive)): 
    if(fi % massive[j] != 0 ):
       clear_massive.append(massive[j])

#print('    └─>Массив чисел на которых ',fi,' не делится: ',clear_massive)


for i in clear_massive:
    if(len(str(i)) == len(str(mod))):
        e = i
        break
print('Второе число публичного ключа: ',e)

for i in key:
    if((i*e)%fi == 1 and i != e):
        d = i
        break
print('Второе число секретного ключа: ',d)

alf_sym = list(alf.keys())
alf_num = list(alf.values())
####################################################################
def Code():
    message = list(input('Введите сообщение: '))
    for i in range(len(message)):
        for sym in range(len(alf_sym)):
            if(message[i] == alf_sym[sym]):
                message_mas.append(alf_num[sym])

    for i in range(len(message_mas)):
        message_mas[i] = message_mas[i]**e % mod
        print(message_mas[i],end = ' ')
###########################################################
def Decode():
    message = input('Введите сообщение: ').split(' ')
    for i in range(len(message)):
        message[i] = int(message[i])
    print(message)

    for i in range(len(message)):
        message_mas.append(message[i]**d % mod)
    print(message_mas)
    for i in range(len(message_mas)):
        for sym in range(len(alf_num)):
            if(int(message_mas[i]) == alf_num[sym]):
                print(alf_sym[sym],end = '')



change = input('Кодировать / Декодировать: ')
if(change == 'К'):
    Code()
if(change == 'Д'):
    Decode()














