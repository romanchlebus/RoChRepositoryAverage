
marks = ()
print("podaj 5 liczb")
for n in range(5):
 numbers = int(input())
 marks = marks + (numbers,)

def  average(m):
 sum = 0
 for i in range (len(m)):
  sum = sum + m[i]
    #end loop
 return print(sum/len(m))
print("\n srednia to:")
average(marks)
