employees = ["John", "Alice", "David", "Sophia", "Michael"]

search_name = input("Enter employee name to search: ")

if search_name in employees:
    print("Record Found")
else:
    print("Record Not Found")
