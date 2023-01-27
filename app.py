
def parallel(*resistors):
    result = 0
    sum = 0
    for resistor in resistors:
        sum+= 1/resistor
        result = 1/sum
    return result 

print (parallel(330, 1000, 2200))
