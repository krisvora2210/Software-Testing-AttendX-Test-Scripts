# Test: Attendance marking in AttendX
def mark_attendance(student_id, status):
    if status in ["Present", "Absent"]:
        return f"Attendance marked {status} for {student_id}"
    return "Invalid status"

print(mark_attendance("S101", "Present"))
print(mark_attendance("S102", "Late"))