'''

"""
************
*          *
*          *
*          *
*          *
************



"""


def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('"Symbol" needs to a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"Width" and "Height" must be greater or equal to 2.')
    
    print(symbol * width)

    for i in range(height -2):
        print(symbol + (' ' * (width -2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)
'''

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key]= 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

    switchLights(market_2nd)

