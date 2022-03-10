def tigaAtaulima(x):
    if(x % 3 == 0 and x % 5 == 0):
        print('Bilangan ini kelipatan 3 dan 5')
    elif x % 3 == 0:
        print('Bilangan ini adlaah kelipatan 3')
    elif x % 5 == 0:
        print('Bilangan ini adlaah kelipatan 5')
    else:
        print('Bilangan ini bukan kelipatan 3 maupun 5')


print(tigaAtaulima(11))
