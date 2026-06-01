with open("./Input/Names/invited_names.txt", "r") as file1:
    names = file1.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as file2:
    file_data = file2.read()
    file_data = file_data.replace("Angela", "Rakshith")

for name in names:
    name = name.strip("\n")
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", "w") as file:
        file.write(file_data.replace("[name]", name))
