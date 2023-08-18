FIO="Test Testing Tester"

print (f"FIO: {str(FIO+', hello!')}")

width = 4

print (f"{2:0{width}b}")

listofvalues=['1','2','three','four','five','six','7']

one,two,_,_,five,six,seven = listofvalues

print (f'{five:5}{seven:7}{two:2}')

one,two,_,*others = listofvalues

print(others)
