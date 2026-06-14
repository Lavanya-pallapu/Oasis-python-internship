import datetime

print("Voice Assistant Started")

while True:
    command = input("You: ").lower()

    if command == "hello":
        print("Assistant: Hello Lavanya!")
    elif command == "time":
        print("Assistant:", datetime.datetime.now().strftime("%H:%M:%S"))
    elif command == "date":
        print("Assistant:", datetime.date.today())
    elif command == "exit":
        print("Assistant: Goodbye!")
        break
    else:
        print("Assistant: Command not recognized")