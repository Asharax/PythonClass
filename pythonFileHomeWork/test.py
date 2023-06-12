# Furkan AYTAN E225043161

import random
def do_test():
    continue_read = 'h'
    numbers = [random.randint(-15, 25) for i in range(10)]
    return calculate_and_print_sums(continue_read, numbers)


def calculate_and_print_sums(continue_read='e', numbers=[]):
    while continue_read != 'h':
        number = int(input('Bir sayı gir: '))
        numbers.append(number)
        if len(numbers) >= 5:
            continue_read = input('Devam etmek istiyor musunuz? (E/H) ').lower()
            if continue_read != 'e' and continue_read != 'h':
                print('Lütfen E veya H giriniz')
                continue_read = 'e'

    print(f'Sayılar: {numbers}')
    positive_numbers = [number for number in numbers if number > 0]
    print(f'Girilen sayılarda bu kadarı pozitif: {len(positive_numbers)}, toplamları: {sum(positive_numbers)}')

    negative_numbers = [number for number in numbers if number < 0]

    print(f'Girilen sayılarda bu kadarı negatif: {len(negative_numbers)}, toplamları: {sum(negative_numbers)}')

    zero_numbers = [number for number in numbers if number == 0]
    print(f'Girilen sayılarda bu kadarı sıfır: {len(zero_numbers)}')

    print(f'Girilen tüm sayıların toplamı: {sum([number for number in numbers])}')

    return numbers


test_mode = input('Minimum 5 sayı girmeniz istenecek, hazır verilerle devam etmek ister misiniz? (E/H) ').lower()
if(test_mode == 'e'):
    list1 = do_test()
elif(test_mode == 'h'):
    list1 = calculate_and_print_sums()
else:
    print('Geçerli bir giriş yapmadığınız için veriler sizden istenecek')
    list1 = calculate_and_print_sums()

list2 = list1.copy()

avarage = sum(list2) / len(list2)

list2 = [number for number in list2 if number >= avarage]
print(f'Liste1 in ortalaması: {avarage},'
      f' ortalamadan küçük {len(list1) - len(list2)} sayı çıkarıldı ve Liste 2 oluşturuldu.')


print(f'Liste1: {list1}')
print(f'Liste2: {list2}')