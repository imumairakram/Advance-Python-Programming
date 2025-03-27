
def calculate_percentage(obtained_marks, total_marks):
    per = obtained_marks / total_marks * (100)
    print(f"Your Percentage is : {per}")
    return per

obtained_marks = float(input("Enter Your Marks: "))
total_marks = int(input("Enter Total Marks: "))

calculate_percentage(obtained_marks, total_marks)
