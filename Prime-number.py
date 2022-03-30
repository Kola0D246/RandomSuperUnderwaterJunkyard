#RandomSuperUnderwaterJankyard
#Prime Numbers
Def= {'prime number':'For any number x, if x is only divisible by +-1 and +-x such that qoutient is also an int',
     }

def primernot(num):
  if num<0:num= -num
  if num==0:return 0
  elif num==1:return 1
  else:
    R=num^(1/2) #check storage of file with R and num^(1/2)
    for x in range(1,R+1):
      Q=num/x #check storage of file with Q and num/x
      if Q==num or Q==1:continue
      if type(Q)== int:return False
      if x==int(R):return True
    return True

def primebtw(num1, num2, pr='P'):
  if pr!='P' and pr!='C' and pr!='Z' and pr!='O':raise ValueError(pr,'is invalid')
  primelst=conslst=zerolst=onelst=[]
  for num in range(num1, num2+1)
    prime= primernot(num)
    if prime==True: primelst.add(num)
    if prime==False: conslst.add(num)
    if prime==0: zerolst.add(num)
    if prime==1: onelst.add(num)
  if pr=='P':return primelst
  elif pr=='C':return conslst
  elif pr=='Z':return zerolst
  elif pr=='O':return onelst

#rename onelst with original name
