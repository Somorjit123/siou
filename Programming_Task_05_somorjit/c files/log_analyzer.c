login_attempts = [
    "Success",
    "Failed",
    "Failed",
    "Success",
    "Failed",
    "Success"
]

total_attempts = len(login_attempts)
successful_logins = login_attempts.count("Success")
failed_logins = login_attempts.count("Failed")

print("Total Attempts:", total_attempts)
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)

print("\nWhy monitoring failed logins is important?")
print("Monitoring failed logins helps detect unauthorized access attempts,")
print("brute-force attacks, and suspicious activities, improving system security.")

