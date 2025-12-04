math=int(input("Enter the Mathematics Subjecct Marks:"))
sci=int(input("Enter the Science Subject Marks:"))
eng=int(input("Enter the English Subject Marks:"))
sen=int(input("Entet the Software Engineering Subject Marks:"))
java=int(input("Entet the Java Programming Subject Marks:"))

total=math+sci+eng+sen+java
print("The Total Marks of all Subject:",total)
print("The Average is:",total/5)
print("The Percentage is:",total/500*100,"%")
