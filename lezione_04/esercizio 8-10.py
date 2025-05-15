text:list[str] = ["Ciao francesco", "Ieri ho mangiato la pizza", "Domani vado al mare"]

def send_messages(text:list[str]):

    sent_messages:list[str] = []
    
    while len(text) > 0:
        
        message = text.pop(0)
        print(message)
        sent_messages.append(message)

    return sent_messages


sent_messages:list[str] = send_messages(text)
print(sent_messages)
print(text)