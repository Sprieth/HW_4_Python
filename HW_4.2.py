
def get_cats_info(path):
    cat_list = []
    try:
        with open(path, "r") as file:
            for cat in file:
                cat_id, cat_name, cat_age = cat.strip().split(',')
                cat_dict = {"id": cat_id, "name": cat_name, "age": cat_age}
                cat_list.append(cat_dict)
            return cat_list
        
    except FileNotFoundError:
        print("File is not found")
    except ValueError:
        print("Invalid file format")

print(get_cats_info("D:/Python/HW_4/HW_4.2.txt"))
