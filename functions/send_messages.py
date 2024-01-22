def show_messages(message):
    """Prints each message in the list."""
    print("showing all the messages:")
    for msg in message:
        print(msg)


def send_messages(messages, sent_messages):
    """Prints each message and move then to a new list."""
    print("\nSending each message:")
    while messages:
        each_message = messages.pop()
        print(each_message)
        sent_messages.append(each_message)


messages = ["today is a good day.", "trust in yourself", "live the moment"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nfinal list:")
print(messages)
print(sent_messages)

