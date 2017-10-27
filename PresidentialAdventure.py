def main():
    import turtle
    wn = turtle.Screen()
    aa = turtle.Turtle()
    aa.write("Prestige 10", False, align="center", font=("Arial", 300, "normal"))
    aa.clear()
    import time
    aa.write("Story")
    print("A Presidential Struggle: A Choose Your Own Adventure!")
    print("The year is 2037. You are the newly elected President of the United States. \n"
          "Your predecessors have nearly ruined this great country thanks to their "
          "corruption.\nYou are your country's last hope!")
    time.sleep(2)
    print("Your secretary tells you that the country of Syria calls for humanitarian aid. Will you supply it?")
    time.sleep(1)
    print("1. Provide economic aid   2. Ignore Syria   3. Verbally promise aid, then break your promise 4. Tell your secretary to go away")

    choice1 = input("Make your choice:")

    def provide_aid():
        print("The country recovers from civil war but faces political instability.")

    def ignore_syria():
        print("With no international aid, the country descends into utter chaos.")

    def troll_syria():
        print("The failure of your administration to follow through on promises lowers your prestige. \n")

    def ignore_secretary():
        print("For the 63rd time, you ignore your secretary. \n Rumors of your laziness proliferate.")

    if choice1 == 1:
        provide_aid()
    elif choice1 == 2:
        ignore_syria()
    elif choice1 == 3:
        troll_syria()
    elif choice1 == 4:
        ignore_secretary()

main()