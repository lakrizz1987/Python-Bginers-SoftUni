number_of_students = int(input())
marks_2_to_299 = 0
marks_3_to_399 = 0
marks_4_to_499 = 0
marks_5_and_more = 0
all_marks = 0

for x in range(number_of_students):
    mark = float(input())
    all_marks += mark
    if 2 <= mark <= 2.99:
        marks_2_to_299 += 1
    elif 3 <= mark <= 3.99:
        marks_3_to_399 += 1
    elif 4 <= mark <= 4.99:
        marks_4_to_499 += 1
    else:
        marks_5_and_more += 1

top_students_percent = marks_5_and_more / number_of_students * 100
between_4_and_499_percent = marks_4_to_499 / number_of_students * 100
between_3_and_399_percent = marks_3_to_399 / number_of_students * 100
fail_percent = marks_2_to_299 / number_of_students * 100
average_marks = all_marks / number_of_students

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_499_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_399_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_marks:.2f}")

