student = {
    "name": "Dharshini",
    "age": 18,
    "department": "ECE"}
print("Student Details:", student)
print("\nName:", student["name"])
student["age"] = 19
print("\nUpdated Age:", student["age"])
student["college"] = "Sathyabama"
print("\nAfter Adding College:", student)
print("\nKeys:", student.keys())
print("\nValues:", student.values())
print("\nItems:", student.items())
student.pop("department")
print("\nAfter Removing Department:", student)
