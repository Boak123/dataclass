from dataclasses import dataclass

@dataclass
class Course:
    course_code: str
    credits_unit: int

first = Course("CSC101", 3)
second = Course("CSC101", 3)

print(first)
print(first == second)