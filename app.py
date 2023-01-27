#Jada Campbell 620141014 ECSE3038 Lab1
def parallel(*resistors):
    result = 0
    sum = 0
    for resistor in resistors:
        sum+= 1/resistor
        result = 1/sum
    return result 

print (parallel(330, 1000, 2200), "ohms")
print("\n")


def potential_divider(voltage, resistor2s=[]):
    ans = 0
    sum2 = 0
    for x in resistor2s:
        sum2+= x

    for x in resistor2s:
        ans = (x/sum2)*voltage
        print(ans, "volts")

values=[3000, 1000,]
potential_divider(9, values)


def temperature_check(temp, unit):
    print("\n")
    if (unit == "C"):
        if temp > 38:
            print("the patient is hyperthermic")
        elif temp < 35:
            print("The patient is hypothermic")
        else:
            print("The patient is normal")
    
    if (unit == "F"):
        if temp > 100:
            print("the patient is hyperthermic")
        elif temp < 95:
            print("The patient is hypothermic")
        else:
            print("The patient is normal")

temperature_check(200, "F")
