print("📝 Simple To-Do List")
print("--------------------")
print("a) View your tasks")
print("b) Add a new task")
print("c) Remove all tasks")
print("d) Remove a task")
print("--------------------")

choice = input("Enter \'a\' or \'b\' or \'c\':")
if (choice=="a"):
    with open("list.txt","r") as f:
        data = f.read()
    if (data==""):
        print("There is no any tasks in ur todo list.")
    else:
        print("Your Tasks:")
        print(data)

elif(choice=="b"):  
    tasks = input("Enter your tasks:")

    with open("list.txt","a") as f:
        f.write(tasks+"\n")
    print("\n✅ Task added successfully!")

    with open("list.txt", "r") as f:
        print("\nUpdated To-Do List:")
        print(f.read().strip())

elif(choice=="c"):
    with open("list.txt","w") as f:
        f.write("")
    print("\n✅ All tasks removed successfully!")
elif(choice=="d"):
    with open("list.txt","w") as f:
        data = f.readlines()
        

else:
    print("❌ Invalid choice! Please enter 'a' or 'b' or 'c'.")

