num=raw_input("Enter number please to exit -1")
num=int( num )


while num != -1:

   if num%10==num/10000:
      num=num/10
      if num%10==(num/100)%10:
         print "Palindrome"
 
   else:
 
      print "Not palindrome"


   num=raw_input("Enter number please to exit -1")
   num=int( num )


   
print "END"  

   
   
