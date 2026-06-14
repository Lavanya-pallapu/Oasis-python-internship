print("Simple Chat Application")

while True:
    msg = input("User 1: ")

    if msg.lower() == "exit":
        break

    reply = input("User 2: ")

    if reply.lower() == "exit":
        break