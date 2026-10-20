from dataclasses import dataclass

@dataclass
class Course:
    course_code: str
    course_name: str
    credits_unit: int = 3
    semester: str = "First"
    is_compulsory: bool = "True"

computer_science = Course("CSC101", "Computer Science")
cyber_security = Course("GST101", "cyber security", 2, "Second", False)
print(computer_science)
print(cyber_security)