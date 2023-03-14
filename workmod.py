
"""
Created on Mon Feb 13 00:29:56 2023

@author: Alexey Ovsyannikov

Модуль включающий в себя функции для использования в основном WorkApp

"""

# Функция расчета длинны материала в рулоне
# Исходная формула L=pi(D^2-d^2)/4t 
def linerlen(D:float, d:float, t:float=1.5):
    """Функция возвращает длину материала в рулоне по формуле
        L=pi(D^2-d^2)/4t где
        D - внешний диаметр рулона в мм
        d - внутренний диаметр рулона в мм
        t - толщина материала в мм
    """
    from math import pi
    L=pi*(D**2-d**2)/(4000*t)
    return round(L, 2)

def linerlen_release():
    " Рассчет длинны материала в рулоне"
    D = float(input("Ведите внешний диаметр D рулона в мм: "))
    d = float(input("Ведите внутренний диаметр d рулона в мм: "))
    t = float(input("Ведите толщину материала t в мм: "))
    print("D = ", D,"мм d = ", d, "мм t = ", t, "мм")
    print ("Длина материала в рулоне L = ", linerlen(D, d, t) , "м")


# Функция расчета материалов для сборки опалубки
def formwork_materials(P):
    """ Функция расчитывает необходимые материалы для подготовки
        комплекта опалубочных конструкций. Расчет только от периметра.
        На выходе массив данных result = [
            0 - профильная труба 40х20мм п.м.,
            1 - контрфорсы(подпорки) компл.,
            2 - болты М8х35 шт./кг,
            3 - гайки M10 шт./кг,
            4 - шайбы M10 шт./кг,
            5 - кровельные саморезы M6х16 шт.,]
    """

    metalprofile = int(P * 2.1 + 6)//6 * 6
    contrforses = int(P//1.5)
    bolt_quantity = nut_quantity = int(P * 4 * 3)
    bolt_weight = round(bolt_quantity * 0.0191, 2)
    nut_weight = round(nut_quantity * 0.011, 2)
    washer_quantity = int(bolt_quantity * 2)
    washer_weight = round(washer_quantity * 0.016, 2)
    bolt = [bolt_quantity, bolt_weight] 
    nut = [nut_quantity, nut_weight] 
    washer = [washer_quantity, washer_weight]
    roofing_screws = int(P * 4 * 4 * 1.1)
    result = [metalprofile, contrforses, bolt, nut, washer, roofing_screws]
    
    return result

def formwork_materials_release(P):
    " Расчет материалов для подготовки комплекта опалубки"
    # P = float(input("Ведите периметр бассейна в п.м. (Пример: 24.5): "))
    M = formwork_materials(P)
    print('Металлический профиль 40х20х1.5мм :',M[0],'п.м.')
    print('Контрфорсы :',M[1],'комплектов')
    print('Болты М8х35 :',M[2][0],'шт./', M[2][1],'кг.') 
    print('Гайки М10 :',M[3][0],'шт./', M[3][1],'кг.')
    print('Шайбы М8 :',M[4][0],'шт./', M[4][1],'кг.')
    print('Кровельные саморезы М6х16 :',M[5],'шт.')
 
# Функция расчета местных строительных материалов    
def local_materials(length, width):
    """ Функция расчитывает необходимые местные материалы для изготовления
        чаши бассейна с применением комплекта полипропиленовой опалубки. 
        Расчет от внутренних размеров чаши.
        На выходе массив данных result = [
            0 - бетон М350.,
            1 - арматура 8мм и 10мм.,
            2 - щебень для подсыпки фр.5-20,
            3 - песок для обратной засыпки,
            4 - блоки 400х200х200мм,
            5 - штукатурная смесь по 25кг,
            6 - шпатлевка по 20 кг,
            7 - клей плиточный по 25кг,]
    """
    p = 2 * length + 2 * width
    concrete = int(p*0.15*1.5+p*0.25*0.25+(length+0.8)*(width+0.8)*0.2 + 1)
    if length >= 12:
        steel8 = int(p*4*2 + 4 * (length + 1.5)*(width + 1.5) / 0.15)
    else:
        steel8 = int(p*4*2 + 2 * (length + 1.5)*(width + 1.5) / 0.15) 
    steel10 = int((p + 4) * 5 if length >=12 else (p + 4) * 3)
    stone = int((length + 0.8)*(width + 0.8)*0.15)
    sand = int(p * 1 * 1.2)
    block = int(p//1.5 + 10)
    plaster = int((length + 0.3)*(width + 0.3)*0.2)
    putty = int((length + 0.3)*(width + 0.3) / 10)
    glue = int(p/8)
    result = [concrete, steel8, steel10, stone, sand,
              block, plaster, putty, glue]
    return result

if __name__ == "__main__":
    l = float(input("Введите длинну бассейна: "))
    w = float(input("Введите ширину бассейна: "))
    print(local_materials(l, w))
    p = 2*(l+w)
    formwork_materials_release(p)
