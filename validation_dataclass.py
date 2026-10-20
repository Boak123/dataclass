from dataclasses import dataclass

@dataclass
class Course:
    credits_unit: int

    def __post_init__(self):
        if self.credits_unit <= 0:
            raise ValueError("credit units cannot be zero")

course = Course(0)