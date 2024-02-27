
def total_salary(path):
    total = 0
    num_developers = 0

    try:
        with open(path, 'r') as file:
            for line in file:
                name, salary_str = line.split(',')
                salary = int(salary_str)
                total += salary
                num_developers += 1
            
        average_sum = total / num_developers   
        average_sum = int(average_sum)
        return total,average_sum

    except FileNotFoundError:
        print("File is not found")

    except ValueError:
        print("Invalid file format")
    if num_developers == 0:
            print("File is Empty")

total, average_sum = total_salary("D:/Python/HW_4/HW_4.1.txt")
if total is not 0 and average_sum is not 0:
    print("Total amount of salaries:", total)
    print("Average salary:", int(average_sum))