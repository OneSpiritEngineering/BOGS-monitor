
from gpiozero import MCP3208
import time
import csv

csvfile = 'MCP3208.csv'
adc = [0, 1, 2, 3, 4, 5, 6, 7]
vref = 3.3

while True:

    with MCP3208(channel=0) as reading:
        adc0 = reading.value * vref
        adc0temp = ('{:.1f}'.format(adc0))

    with MCP3208(channel=1) as reading:
        adc1 = reading.value * vref
        adc1temp = ('{:.1f}'.format(adc1))

    with MCP3208(channel=2) as reading:
        adc2 = reading.value * vref
        adc2light = ('{:.1f}'.format(adc2))

    with MCP3208(channel=3) as reading:
        adc3 = reading.value * vref
        adc3light = ('{:.1f}'.format(adc3))

    with MCP3208(channel=4) as reading:
        adc4 = reading.value * vref
        adc4levelt = ('{:.1f}'.format(adc4))

    with MCP3208(channel=5) as reading:
        adc5 = reading.value * vref
        adc5levelb = ('{:.1f}'.format(adc5))

    with MCP3208(channel=6) as reading:
        adc6 = reading.value * vref
        adc6press = ('{:.1f}'.format(adc6))

    with MCP3208(channel=7) as reading:
        adc7 = reading.value * vref
        adc7x = ('{:.1f}'.format(adc7))

    timex = time.strftime('%H') + ':' + time.strftime('%M') + ':' + time.strftime('%S')
    data = [adc0temp, adc1temp, adc2light, adc3light,
            adc4levelt, adc5levelb, adc6press, adc7x, timex]

    with open(csvfile, 'a') as output:
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        writer.writerow(data)

    time.sleep(2)