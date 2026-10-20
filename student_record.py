from dataclasses import dataclass, field

@dataclass
class StudentProfile:
    name: str
    scores: list[int] = field(default_factory=list)