# List comprehensions and readability
# lists a mutable containers
# List comprehensions build lists from sequences or any other iterable type by filtering and transforming items

def doStuff():
    symbols = '$¢£¥€¤'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

def doStuffListComp():
    symbols = '$¢£¥€¤'
    codes = [ord(symbol) for symbol in symbols]
    print(codes)


def doStuffListComp2():
    nums = '12345'
    numms = [num for num in nums]
    print(numms)
    print(type(numms))


def cartesianStuff():
    colours = ['blue', 'green', 'red']
    sizes = ['small', 'medium', 'large']
    tshirts = [(colour, size) for colour in colours for size in sizes]
    print(tshirts)
    print(type(tshirts))

if __name__ == '__main__':
    #doStuff()
    #doStuffListComp2()#
    cartesianStuff()