#выбор из меню
print("""Menu:
1. File
2.View
3.Exit
""")

choice = input("Enter your choice: ")
if choice == "1":
    print("You have selected 'File' menu")
elif choice == "2":
    print("You have selected 'View' menu")
elif choice == "3":
    print("Stopping")
else:
    print("Incorrect choice")
#выбор в зависимости от данного значения
is_ready = True
state_msg = is_ready and "Ready" or "Not ready yet"
print (state_msg)
#тернарная операция
is_ready = False
print("Ready" if is_ready else "Not ready yet")
