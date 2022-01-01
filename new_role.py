def show_messages(messages):
    '''
    Prints each short messages in the list
    '''
    for message in messages:
        print(f'My new role for the year is:\n{message.title()}\n')

some_lists = ['today is a blessing', '2022 is japa year', 'adding more trucks this year', 'taking  care of my health' ]
show_messages(some_lists)

def show_messages(messages, sent_messages):
    while messages:
        the_same_message = messages.pop()
        print(f'{the_same_message}')
        sent_messages.append(the_same_message)

def send_messages(sent_messages):
    print('\nAll the messages have been sent:\n ')
    for sent_messages in sent_messages:
        print(sent_messages)

messages = ['today is a blessing', '2022 is japa year', 'adding more trucks this year', 'taking  care of my health' ]
sent_messages = []

show_messages(messages, sent_messages)
send_messages(sent_messages)

show_messages(messages[:], sent_messages)