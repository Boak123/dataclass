from dataclasses import dataclass

@dataclass
class CourseIdentifier(frozen=True):
    course_code: str = "CSC101"

course = CourseIdentifier("CYB101")

