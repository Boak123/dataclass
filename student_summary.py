from dataclasses import dataclass, asdict

@dataclass
class StudentSummary:
    student_id: str
    name: str
    score: int
    grade: str = ""

    def __post_init__(self):
        if not 0 <= self.score <= 100:
            raise ValueError(f"Invalid score: {self.score}. Must be between 0 and 100.")

        self.grade = self._calculate_grade()

    def _calculate_grade(self) -> str:
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 45:
            return "D"
        else:
            return "F"


student_sum1 = StudentSummary("1234GG", "OJO", 80)
print(student_sum1)

new_summary = asdict(student_sum1)
print(new_summary)