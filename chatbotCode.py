firstName = input("Hello! I am a chat bot and I would like you to fill out this survey.\n\nWhat is your name?\n")
print("\nGreetings, " + firstName + ".\n\n")
favFood = input("What is your favorite food?\n")
print("\nYour favorite food is " + favFood + ", " + firstName + "? Okay.\n\n")
favColor = input("What is your favorite color, " + firstName + "?\n")
print("\nSo " + favColor + " is your favorite color, " + firstName + "? Thats cool.\n\n")
leastFavAnimal = input("What animal do you hate the most?\n")
print("\nYeah, I don't like the " + leastFavAnimal + " either, " + firstName + ".\n\n" )
print("\nBased on your answers, your name is " + firstName + ", your favorite food is " + favFood + ", your favorite color is " + favColor + ", and you hate the " + leastFavAnimal + " more than any other animal. \n\nThank you for completing this survey.")