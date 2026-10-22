from dataclasses import dataclass

@dataclass
class RegistrationResult:
    success: bool
    message: str
    student_id: str = None


reg1 = RegistrationResult(True, "Successful", "ST001")
reg2 = RegistrationResult(False, "Failed", "ST001")

print(reg1)
print(reg2)