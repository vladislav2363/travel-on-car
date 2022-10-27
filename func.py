def getKolvo():

    dis = float(input('Введите расстояние: '))
    consum = float(input('Введите расход на 100км : '))  # расход бензина на 100км
    dis_one_km = float(consum / 100)
    kolvo = float(dis * dis_one_km)
    return kolvo


def benz(mark2, kolvo, AI92, AI95):
    if mark2 == 92:
        stm = int(AI92 * kolvo)  # стоимость бензина
        stm_v2 = int(stm * (2))
        print('Стоимость бензина в одну сторону : ', stm, 'Рублей')
        print('Стоимость бензина в 2 стороны: ', stm_v2, 'Рублей')

    elif mark2 == 95:
        stm = int((AI95 * kolvo))
        stm_v2 = int((stm * 2))
        print('Стоимость бензина в одну сторону : ', stm, 'Рублей')
        print('Стоимость бензина в 2 стороны: ', stm_v2, 'Рублей')

    return stm_v2


def gas(mark, kolvo,GAZ):

    if mark == 'газ':
        stm = int((GAZ * kolvo))
        stm_v2 = int((stm * (2)))
        print('Стоимость газа: ', stm, 'Рублей')
        print('Стоимость бензина в 2 стороны: ', stm_v2, 'Рублей')
        print("Вычисления газа")

        return stm_v2