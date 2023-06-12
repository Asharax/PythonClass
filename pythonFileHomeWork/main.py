#Create file name months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#New file
new_file = open('months.txt', 'w')
#with open ('months.txt', 'w') as new_file:

#Write months to file
for month in months:
    new_file.write(month + "\n")

#Close file
new_file.close()

f  = open("months.txt", "r")

veri = f.readlines()
SS = len(veri)


print('SS')
print(SS)
print('veri')
print(veri)


#which line to read
#line = int(input('Dosyada{} satır var. Hangi satırı okumak istersiniz? '.format(SS)))

#read line
#print(veri[line-1])

#close file
f.close()


#########################

def func():
    while True:
        line=int(input('Dosyada{} satır var. Hangi satırı okumak istersiniz? '.format(SS)))
        #check if line smallwer than 0 opr bigger than SS
        if line <= 0 or line > SS:
            print('Lütfen 1 ile {} arasında bir sayı giriniz'.format(SS))
            continue
        else:
            print(veri[line-1])

        continueRead = input('Devam etmek istiyor musunuz? (E/H) ')
        if continueRead == 'E' or continueRead == 'e': # upper or lower
            continue
        else:
            print('Programdan çıkılıyor...')
            break


def arttır(x):
    return x + 1


a=3
print(arttır(a))

print(a)
def new_user(ad='Girilmedi', soyad='Girilmedi', yas=0, meslek='Girilmedi'):
    with open('users.txt', 'a') as file:
        file.write(f'{ad} {soyad} {yas} {meslek}\n')
### çalışmadı???

new_user('Ayşe', 'Yılmaz', 25, 'Öğrenci')
new_user(ad='Hüsam', yas=15)



alphabeth = 'abcçdefgğhıijklmnoöprsştuüvyz'
key = 'xwqazsdcfrvgtbhyujnıolpökmşü'

def encrypt(message):
    encrypted = ''
    for char in message:
        if char in alphabeth:
            encrypted += key[alphabeth.index(char)],
            #print(key[alphabeth.index(char)],end='')
        else:
            encrypted += char
    return encrypted

print('test')


for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            if x**2 + y**2 == z**2:
                print(x,y,z)
