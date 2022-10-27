

#С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
#"Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"
# Рассчёт стоимости путешествия на арендованной машине или на своей или на поезде или на бензине

# #Аренда 1500 Газ - 4431 в одну сторону аренда жилья - 6000 2х местный

# обернуть все инпуты в фунцию def GetData():

# Добавить стоимость мотеля в дороге и стоимость еды и алко

def benz(mark, ras, rsd, AI92, AI95, GAZ):
    if mark == '92':
        stm = int(AI92 * kolvo) # стоимость бензина
        stm_v2 = int(stm * (2))
        print('Стоимость бензина в одну сторону : ', stm, 'Рублей')
        print('Стоимость бензина в 2 стороны: ', stm_v2, 'Рублей')
        if mark != '92':
            print('Такой марки нет')


    elif mark == 'газ':
        mark
        stm = int((GAZ * kolvo))
        stm_v2 = int((kolvo * 2))
        print('Стоимость газа: ', stm, 'Рублей')
        print('Стоимость бензина в 2 стороны: ', stm_v2, 'Рублей')

    elif mark == '95':
        stm = int((AI95 * kolvo))
        stm_v2 = int((stm * 2))
        print('Стоимость бензина в одну сторону : ', stm, 'Рублей')
        print('Стоимость бензина в 2 стороны: ', stm_v2, 'Рублей')

    return stm_v2


    while True:
            if mark == 92 or mark == 95:
                break
            if mark == ('газ'):
                break
            else:
                print('Попробуйте ещё раз')


GetInput(mark)

ras = float(input('Введите расстояние: '))
rsd = float(input('Введите расход бензина на 100км : '))  # расход бензина на 100км
AI92 = 45.85  # 92 бенз #4431
AI95 = 49.85  # 95 бенз
GAZ = 20
rsd1 = float(rsd / 100)
kolvo = float(ras * rsd1)






car = input('Поедете на своей машине? ')


while car != 'нет':
    Mistake(car)
    break


else:                                                                      #print('Неправильный ввод, попробуйте с маленькой буквы')

    arenda = int(input('Введите стоимость аренды машины: '))
    kolvo_dney = int(input('Введите количество дней аренды авто: '))
    stm_avto = arenda * kolvo_dney  # стоимость аренды авто на n дней
    print('Стоимость арендованного автомобиля: ', stm_avto)





motel = input('Будете ли вы по дороге останавливаться? ')
if motel == 'да':
    hotel = int(input('Введите стоимость мотеля: '))
    kolvo_hotel = int(input('Введите дни в мотеле: '))
    stm_hotel = hotel * kolvo_hotel  # Стоимость мотеля
    print('Стоимость мотеля: ', stm_hotel)



hata = int(input('Введите стоимость квартиры или дома за сутки: '))
kolvo_dney_hata = int(input('Введите количество дней аренды жилья: '))
kolvo_chel = int(input('Введите количество человек: '))

stm_hata = hata * kolvo_dney_hata #Стоимость аренды квартиры на n дней


stm_fuel = benz(mark, ras, rsd, AI92, AI95, GAZ) #Стоимость бензина или газа

poezdka = stm_avto + stm_fuel # стоимость машины туда и обратно



print('___________\n' + ' Стоимость машины на ' + str(kolvo_dney) + ' дней ' + 'на ', kolvo_chel, ' человек: ', stm_avto, 'Рублей')
print('___________\n' + ' Стоимость жилья на ' + str(kolvo_dney_hata) + ' дней ' + 'на', kolvo_chel, 'человек: ', stm_hata, 'Рублей')
print('___________\n' + ' Стоимость мотеля на ' + str(kolvo_hotel) + ' дней ' + 'на', kolvo_chel, 'человек: ', stm_hotel, 'Рублей')

#stm_avto_na_1 = stm_avto/kolvo_chel
#print(stm_avto_na_1, ' Стоимость на 1 человека')



auto = poezdka / kolvo_chel # стоимость машины туда и обратно на одного человека
hata_сhel = stm_hata / kolvo_chel # стоимость квартиры на человека
hotel_chel = stm_hotel / kolvo_chel # стоимость мотеля на человека
stm_poezdki = stm_avto + stm_fuel + stm_hata + stm_hotel  # стоимость поездки на всех
stm_poezdki_na_chel = stm_poezdki / kolvo_chel # стоимость поездки на человека
print('Стоимость поездки(авто): ', poezdka)
print('Стоимость поездки  человека на авто: ', auto)
print('Стоимость аренды жилья на человека: ', hata_сhel)                        #25184
print('Стоимость поездки: ', stm_poezdki)
print('Стоимость поездки на человека: ', stm_poezdki_na_chel)


input('Press ENTER to exit')






















