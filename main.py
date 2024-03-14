print("""Welcome to the Story Builder!
We are about to write a cute little story. You choose the details, and I'll put it all together. Sounds good? Let's go!""")

is_on = True
while (is_on == True):
    color = input("Give me a color: ").lower()
    animal = input("Give me an animal: ").lower()
    vegetable = input("Give me a vegetable: ").capitalize()
    fruit = input("Give me a fruit: ").lower()
    adjective = input("Give me an adjective: ").lower()
    verb = input("Give me a verb: ").lower()
    noun = input("Give me a noun: ").lower()

    print(
        f"Once upon a time, there was a big, {color} house, in a big. {color} forest. In there, lived a {color}-haired witch with her pet {animal} named {vegetable}. One day, {vegetable} decided to go for a walk and search for some juicy {fruit}s. "
        f"She searched and searched, but all the {fruit}s she was finding were {adjective}. Suddenly, she realised that it was getting dark and she had no idea where she was! There was only one thing left to do: {verb}. "
        f"As {vegetable} was {verb}ing, she smelled a familiar smell of {noun} - it was her witch! And she was holding the biggest, juiciest {fruit} that {vegetable} has ever seen. She ran up to the witch and happily jumped on her shoulder. "
        f"The witch grunted as {vegetable} wasn't the lightest {animal}, but quickly found her composure and gave her a little head pat. They found their way home together and enjoyed a big, yummy portion of the {fruit}. THE END.")

    restart = input("That was fun! Would you like to go again? ").lower()

    if restart == "no":
        is_on = False
