def losa(x):
   for i in range(2,int(x+1)):
      if x % i == 0:
         print(i,end=',')
         losa(x/i) 
         break 
if __name__ == "__main__":
   user_inp = int(input("Number : "))
   print(user_inp,"Losagu",end=" : ")
   losa(user_inp)
   print('\n')