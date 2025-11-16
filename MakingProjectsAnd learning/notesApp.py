import json
print("----Notes📝----")
print("1.View Notes")
print("2.Add Notes")
print("3.Delete all")
print("4.Delete a specific note")
print("5.Edit note")
user_choice = int(input("Enter your choice:"))

def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except:
        return []
if (user_choice==1):
    notes = load_notes()
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

elif (user_choice==2):
    new_notes = input("Enter notes:")
    notes = load_notes()
    notes.append(new_notes)
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)
    print("Saved:", notes)

elif(user_choice ==3):
    with open("notes.json","w")as f:
        json.dump([], f, indent=4)

elif(user_choice ==4):
        # Load notes
    notes = load_notes()
    # Show notes
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

    # Get number
    delete_index = int(input("Enter note number to delete: "))

    # Convert to list index
    real_index = delete_index - 1

    # Delete
    notes.pop(real_index)

    # Save
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)

    print("Note deleted!")

elif user_choice == 5:
    # Load notes
    notes = load_notes()


    # Show notes
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

    edit_index = int(input("Enter note number to edit: ")) - 1

    # Get new text
    new_text = input("Enter new text: ")

    # Replace in list
    notes[edit_index] = new_text

    # Save updated list
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)

    print("Note edited successfully!")

else:
    print("Invalid choice!")