from dataclasses import dataclass

@dataclass
class StudentProfile:
    name: str
    student_id: str
    level: str
    email: str = "not_provided"

student1 = StudentProfile("Ojo Boluwatife Victor", "2346GG", "100LV", "bovic2026@gmail.com")

print(student1)