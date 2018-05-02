
w=input('Enter the weight in KG: ')

h=input('Enter the height in CM: ')
h=int(h)/100
bmi = int(w)/(h*h)
print ('bmi is: ' +str(bmi))


if bmi<25:
      print ('you are underweight')
elif bmi>25 and bmi <30:
      print('perfect weight....maintain')
else:
      print ('You seem to be overweight')
