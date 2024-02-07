with open('./Input/Names/invited_names.txt') as invited_names:
    names_list = invited_names.readlines()
    invited = []
    for num in range(0, len(names_list)):
        invited.append(names_list[num].strip())

for name in invited:
    with open('./Input/Letters/starting_letter.txt') as starting_letter:
        starting_letter = starting_letter.read()
        with open(f'./Output/ReadyToSend/{name}_letter.txt', mode='w') as new_letter:
            new_letter.write(starting_letter.replace('[name]', name))

print(names_list)