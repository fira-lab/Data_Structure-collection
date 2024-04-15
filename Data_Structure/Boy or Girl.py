def determine_gender(username):
    distinct_chars = set(username)
    if len(distinct_chars) % 2 == 0:
        return "IGNORE HIM!"
    else:
        return "CHAT WITH HER!"
username = input("Enter the username: ")
result = determine_gender(username)
print(result)