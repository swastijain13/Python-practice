import json
import re


# def is_valid_name(name):
#     return isinstance(name, str) and re.fullmatch(r"[A-Za-z ]+", name) is not None

# def is_valid_email(email):
#     return isinstance(email, str) and re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

# def is_numeric(value):
#     return re.match(r'^\d+$', str(value)) is not None

# def is_valid_string_array(arr):
#     return isinstance(arr, list) and all(isinstance(item, str) for item in arr)


# print("Name:", data.get("name"), end=" | ")
# if(is_valid_name(data.get("name"))):
#     print("Name is valid.")
# else:
#     print("Name should have only english alphabets!")



# print("Email:", data.get("email"), end=" | ")
# if(is_valid_email(data.get("email"))):
#     print("Email is valid")
# else:
#     print("Email is not valid!")



# print("Age:", data.get("age"), end=" | ")
# if(is_numeric(data.get("age"))):
#     print("Age is valid")
# else:
#     print("Age should only be numeric!")


# print("Contact:", data.get("contact"), end=" | ")
# if(is_numeric(data.get("contact"))):
#     print("Contact number is valid")
# else:
#     print("Contact number should only be numeric!")


# print("Skills:", data.get("skills"), end=" | ")
# if(is_valid_string_array(data.get("skills"))):
#     print("Valid skills")
# else:
#     print("All skills should be strings!")

# print("Employer:", data.get("employer"), end=" | ")
# if(isinstance(data.get("employer"), str)):
#     print("Valid Employer name")
# else:
#     print("Employer name should be string type!")



with open('sample.json') as f:
    data = json.load(f)

print(data)
