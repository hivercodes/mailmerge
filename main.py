#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



def create_letter(starting_letter, name_of_person):
     new_letter_list = []
     with open(starting_letter, "r") as starting_letter:
        starting_letter_list = starting_letter.read().split(" ")
        insert = f"{name_of_person},\n\nYou"
        for divide in range(len(starting_letter_list)):
            if divide == 1:
                new_letter_list.append(insert)
            else:
                new_letter_list.append(starting_letter_list[divide])

        new_letter = " ".join(new_letter_list)
        return new_letter

def create_mail_list(starting_letter, name_document):
    with open(name_document, "r") as starting_names:
        starting_names_list = starting_names.read().split("\n")
        for name in starting_names_list:
            letter = create_letter(starting_letter, name)
            with open(f"Output/ReadyToSend/{name}.txt", "w") as ready_letter:
                ready_letter.write(letter)



create_mail_list("Input/Letters/starting_letter.txt", "Input/Names/invited_names.txt")