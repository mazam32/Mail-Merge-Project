list_of_names = []
with open("/Users/muhammadhamdazam/Documents/Python Programs/Day 24/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as file:
    for names in file.readlines(33):
        list_of_names.append(names[:-1])
    print(list_of_names)

with open("/Users/muhammadhamdazam/Documents/Python Programs/Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as file:
    default_text = file.read()
    default_text = default_text.replace("Angela", "Muhammad Hamd")
    for names in list_of_names:
        new_text = default_text.replace("[name]", names)
        with open(f"/Users/muhammadhamdazam/Documents/Python Programs/Day 24/Mail Merge Project Start/Output/ReadyToSend/letter_to_{names}", "w") as letter:
            letter.write(new_text)