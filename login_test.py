# Test: Login functionality of AttendX
def test_login(username, password):
    if username == "student1" and password == "pass123":
        return "Login Successful"
    return "Invalid Credentials"

print(test_login("student1", "pass123"))   # expected: Login Successful
print(test_login("student1", "wrong"))     # expected: Invalid Credentials
print(test_login("", ""))   # expected: Invalid Credentials (empty fields)