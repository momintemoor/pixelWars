fileName = "users.txt"


def view_users():
    all_users = []
    with open(fileName) as f:
        for line in f:
            all_users.append({"user": line.rstrip("\n\r")})
    return all_users

def update_users(input):
    with open(fileName, "a") as file:
        file.write(input + "\n")