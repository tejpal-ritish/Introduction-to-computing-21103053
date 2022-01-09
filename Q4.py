#Ques 3. wap to store marks of 5 students and sort them

marks=[]

for i in range(5):
    print('Enter the marks of student',i+1,' -> ')
    item=int(input())
    marks.append(item)

marks.sort()
print(marks)
