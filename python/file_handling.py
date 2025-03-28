# txt_data = "Today is RCB VS CSK MATCH DAY....."
# file_path = "ipl_match.txt"
#
# with open(file_path,"w") as  file:
#     file.write(txt_data)
#     print(f"File has been written: {file_path}")

import os
# file_exists = os.path.exists(file_path)
# print(file_exists)

# reading a json file
# import json
#
# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "He is a cook."
# }
#
# # Use a raw string or double backslashes for the file path
# file_path = r"F:\OneDrive\Desktop\output.json"
#
# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file)
#         print(f"JSON file: {file_path} has been created!")
# except Exception as e:
#     print(f"An error occurred: {e}")


# Working with CSV Files
# import csv
# employees = [["Name","Age","Job"],
#              ["Spongebob","25","Cook"],
#              ["Patrick","30","Cleaner"],
#              ["Samantha","29","Stripper"]]
#
# file_path = "F:/OneDrive/Desktop/employees-data.csv"
#
# try:
#     with open(file_path,"w") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"file has been written.")
#
# except FileExistsError:
#     print("file already exists.")



# reading a file

file_path = "ipl_match.txt"

with open(file_path,"r") as file:
    contents = file.read()
    # contents = json.load(file) to read json file
    print(contents)
