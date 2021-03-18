numberOfTests= int(input())

for i in range (numberOfTests):
  makeList = []
  newList = []
  roadName = input()
  amountOfAddress,nameOfAddresses = input().split()

  while (len(makeList))<int(amountOfAddress):
    singleAddress = input()
    
    if singleAddress.isdigit():
      makeList.append(int(singleAddress))

    else: 
      a, b, c, d = map(str, singleAddress.split())
      b = int(b)
      c = int(c)
      d = int(d)

      while b <= c:
        makeList.append(b)
        b+=d

  for i in range(len(makeList)):
    num = str(makeList[i])
    for i in range (len(num)):
      newList.append(num[i])
    

  print(roadName)
  print(amountOfAddress, nameOfAddresses)
  count0 = newList.count('0')
  print('Make', count0, 'digit 0')
  count1 = newList.count('1')
  print('Make', count1, 'digit 1')
  count2 = newList.count('2')
  print('Make', count2, 'digit 2')
  count3 = newList.count('3')
  print('Make', count3, 'digit 3')
  count4 = newList.count('4')
  print('Make', count4, 'digit 4')
  count5 = newList.count('5')
  print('Make', count5, 'digit 5')
  count6 = newList.count('6')
  print('Make', count6, 'digit 6')
  count7 = newList.count('7')
  print('Make', count7, 'digit 7')
  count8 = newList.count('8')
  print('Make', count8, 'digit 8')
  count9 = newList.count('9')
  print('Make', count9, 'digit 9')
  totalDigits = count0 + count1+ count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9
  

  if totalDigits <= 1:
    print('In total', totalDigits, 'digit')
  else:
    print('In total', totalDigits, 'digits')
