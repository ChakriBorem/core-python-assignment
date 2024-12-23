class Student:
    def avg_cal(self,stu):
        avg_stu={}
        for name,marks in stu.items():
            avg=0
            avg = sum(marks)/len(marks)
            avg_stu[name]=avg
        avg_stu1={name:f"{avg:.2f}" for name,avg in avg_stu.items()}
        print(f"Average Marks: {avg_stu1}")
        topper = max(avg_stu,key=avg_stu.get)
        print(f'Top Performer: "{topper}"')

obj=Student()
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
obj.avg_cal(students)
