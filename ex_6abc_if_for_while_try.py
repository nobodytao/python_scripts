
#Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
#состоит из 4 чисел (а не букв или других символов)
#числа разделенны точкой
#каждое число в диапазоне от 0 до 255
#Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес». 
#-------------------------------------------------------------------------
#Указать принадлежность адреса:
#«unicast» - если первый байт в диапазоне 1-223
#«multicast» - если первый байт в диапазоне 224-239
#«local broadcast» - если IP-адрес равен 255.255.255.255
#«unassigned» - если IP-адрес равен 0.0.0.0
#«unused» - во всех остальных случаях

# Решение: перебирать символы до тех пор, пока будет не число, 
# а любой другой знак

isOk=False
isOctetsOk=False
ip = input('Введите IP-адрес в формате 10.10.0.1: ') 

while (isOk==False) or (isOctetsOk == False):

    prev_lett=''
    prev_dots_count=1
    isOk=True
    isOctetsOk=True

    for lett in ip:
        if lett.isdigit():
            prev_dots_count = 1
            #print (lett)
        elif lett != '.': 
            print ('Ошибка: IP-адрес содержит иные символы кроме цифр и точки')
            isOk=False 
        elif ((lett == '.') and (prev_lett =='.')):
            prev_dots_count += 1
            print ('Ошибка: {} точек подряд'.format(prev_dots_count))
            isOk=False
        prev_lett=lett

    if (ip.startswith(".")):
        print('Ошибка: IP-адрес начинается с точки, не введен первый октет')
        isOk=False

    if (ip.endswith(".")):
        print('Ошибка: IP-адрес заканчивается точкой, не введен последний октет')
        isOk=False
       
    if isOk:
        IPlist=ip.split('.')

        if (len(IPlist) != 4):
            isOctetsOk=False
            print ("Ошибка: Недостаточное количество октетов, разделенных точкой = {}".format(len(IPlist)))
 
        for octet in IPlist:
            if not(int(octet) in range (0,256)): 
                isOctetsOk=False
                print('Октет {} не находится в диапазоне от 0 до 255'.format(octet))
        if isOctetsOk:
            if int(IPlist[0]) in range(1,223): 
                print(ip,' «unicast»')
            elif int(IPlist[0]) in range(224,239):
                print(ip,' «multicast»')
            elif ip=='255.255.255.255':
                print(ip,'«local broadcast»')
            elif ip=='0.0.0.0':
                print(ip,'«unassigned»')
            else:
                print(ip,'«unused»')
    if isOk == False or isOctetsOk == False:
        print ('Неправильный IP-адрес!')
        ip=input('Введите IP-адрес еще раз: ')