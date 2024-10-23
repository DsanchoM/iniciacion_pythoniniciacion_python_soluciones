def computepay (hours, rate):
  print(f'TOTAL{(min(hours, 40)*rate)+(max((hours-40), 0)*(rate*1.5))}')
computepay (50,10)
computepay (45,10)
