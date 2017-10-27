import turtle
import time
import os

name = ""


def squareChoice(bb):
    for i in range(4):
        bb.forward(100)
        bb.left(90)

def choice1result (aa):                              #choice A main branch 1
    global bb, name
    aa.clear()
    clear_b(bb)
    aa.write("Syria recovers, but your foreign policy faces heavy criticism in the US.", False, align = "center", font = ("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.goto(0, 300)
    aa.write("It has been revealed that Russia is making nukes. How will you respond, President" + name + "?", False, align = "center", font = ("Courier", 20, "normal"))
    aa.goto(0, 260)
    aa.write("1. Place economic sanctions on Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 220)
    aa.write("2. Send 500 American inspectors and diplomats to Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 180)
    aa.write("3. Do nothing", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 140)
    aa.write("4. Initiate nuclear war with Russia.", False, align="center", font=("Courier", 15, "normal"))
    choice_boxes(bb)

def choice1_1_result (aa):                                      #russia nuke conseq 1
    global bb
    aa.clear()
    clear_b(bb)
    aa.write("Russia faces food shortages. The nuclear program is disbanded.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.write("Just to make sure, you send diplomats and nuclear inspectors to Russia.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    choice1_2_result(aa)



def choice1_2_result(aa):                               # russia nuke conseq 2
    global bb, name
    aa.clear()
    clear_b(bb)
    aa.write("1,000 nuclear warheads are found. The Americans mysteriously disappear.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.goto(0, 100)
    aa.write("Congress demands that your declare war on Russia for these atrocities.", False, align = "center", font = ("Courier", 15, "normal"))
    aa.goto(0, 50)
    aa.write("In a rush, you follow through with Congress's demands and declare war on Russia.", False, align = "center", font = ("Courier", 15, "normal"))
    time.sleep(3)
    aa.clear()
    aa.goto(0, 340)
    aa.write("The fear of nuclear war creates worldwide chaos.", False, align = "center", font = ("Courier", 20, "normal"))
    aa.goto(0, 310)
    aa.write("President" + name + ", what is our next course of action?", False, align = "center", font = ("Courier", 20, "normal"))
    aa.goto(0, 260)
    aa.write("1. Claim that it was a prank. Take back your declaration of war.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 220)
    aa.write("2. MURICA! Begin targeting Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 180)
    aa.write("3. Ask your international allies to help you fight Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 140)
    aa.write("4. Do nothing and hide in your presidential bunker.", False, align="center", font=("Courier", 15, "normal"))
    choice_boxes(bb)


def choice1_3_result(aa):                       #russia nuke conseq 3
    global bb
    aa.clear()
    clear_b(bb)
    aa.write("Democrats and Republicans question your competence. No rumors of impeachment. Yet.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.write("In your lazy delusion, you have accidentally declared war on Russia.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    choice1_4_result(aa)




def choice1_4_result(aa):                           #russia nuke conseq 4
    global bb, name
    aa.clear()
    clear_b(bb)
    aa.write("The US enters a state of emergency and prepares its nuclear arsenal.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.goto(0, 340)
    aa.write("The fear of nuclear war creates worldwide chaos.", False, align = "center", font = ("Courier", 20, "normal"))
    aa.goto(0, 310)
    aa.write("President" + name+ ", what is our next course of action?", False, align = "center", font = ("Courier", 20, "normal"))
    aa.goto(0, 260)
    aa.write("1. Claim that it was a prank. Take back your declaration of war.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 220)
    aa.write("2. MURICA! Begin targeting Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 180)
    aa.write("3. Ask your international allies to help you fight Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 140)
    aa.write("4. Do nothing and hide in your presidential bunker.", False, align="center", font=("Courier", 15, "normal"))
    choice_boxes(bb)


def choice1_4_1_result(aa):                         #russia nuke war, first choice
    global bb
    aa.clear()
    clear_b(bb)
    aa.up()
    aa.goto(0, 100)
    aa.write("Too late. Russia's first strike has reached the US and turned your country into a wasteland.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, -100)
    aa.write("You are remembered as the President who lost the War.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.goto(0, 0)
    aa.write("GAME OVER. BE MORE DECISIVE NEXT TIME.", False, align= "center", font=("Courier", 25, "bold"))

def choice1_4_2_result(aa):
    global bb, gif2, gif
    wn = turtle.Screen()
    aa.clear()
    clear_b(bb)
    aa.goto(0, 500)
    aa.write("Select the Russian city that you will strike first. Click on your desired target.", False, align = "center", font = ("Courier", 20, "normal"))
    wn.addshape(os.path.expanduser('russiaclear2.gif'))
    gif = turtle.Turtle()
    gif.speed(0)
    gif.hideturtle()
    gif.shape(os.path.expanduser('russiaclear2.gif'))
    gif.goto(0, 150)
    gif.stamp()
    gif2 = turtle.Turtle()
    wn.addshape(os.path.expanduser('crosshairs2.gif'))
    gif2.shape(os.path.expanduser('crosshairs2.gif'))
    gif2.up()
    gif2.goto(-412, 352)
    gif2.down()
    gif2.stamp()
    gif2.up()
    gif2.goto(-151, 70)
    gif2.down()
    gif2.stamp()
    gif2.up()
    gif2.goto(126, -48)
    gif2.down()
    gif2.stamp()
    gif2.up()
    gif2.goto(-420, 220)
    gif2.down()
    gif2.stamp()
    gif2.up()

    aa.color("Blue")
    aa.up()
    aa.goto(-412, 325)
    aa.write("1", False, align= "center", font=("fixedsys", 35, "bold"))
    aa.up()
    aa.goto(-420, 220)
    aa.write("2", False, align="center", font=("fixedsys", 35, "bold"))
    aa.up()
    aa.goto(-151, 70)
    aa.write("3", False, align="center", font=("fixedsys", 35, "bold"))
    aa.up()
    aa.goto(126, -48)
    aa.write("4", False, align="center", font=("fixedsys", 35, "bold"))

    aa.color("black")
    aa.goto(0, -250)
    aa.write("Zone 1 (Saint Petersburg): A strategic port. The lifeline of Russia. Twenty Russian nuclear submarines and 300 nukes.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, -290)
    aa.write("Zone 2 (Moscow): The political, social, and economic center of Russia. Population: 15,000,000. Estimate: 2,000 nukes. ", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, -330)
    aa.write("Zone 3 (Yekaterinburg): A massive industrial center. Estimates say 7,500 nukes are stored here.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, -370)
    aa.write("Zone 4 (Novosibirsk): Population: 7,500,000. Supplies water, electricity, military aircraft and nuclear fuel.", False, align="center", font=("Courier", 15, "normal"))

def stpetersburg_attack (aa):
    global bb, gif2, gif, name
    wn = turtle.Screen()
    clear_b(bb)
    wn.addshape(os.path.expanduser('explosion2.gif'))
    gif3 = turtle.Turtle()
    gif3.speed(0)
    gif3.hideturtle()
    gif3.shape(os.path.expanduser('explosion2.gif'))
    gif3.up()
    gif3.goto(-412, 352)
    gif3.down()
    gif2.clear()
    gif3.stamp()
    time.sleep(1.5)
    aa.clear()
    time.sleep(1)
    gif3.clear()
    gif.clear()
    aa.up()
    aa.goto(0, 100)
    aa.write("With its main port destroyed, Russia can no longer deploy its nuclear submarines.", False, align= "center", font=("Courier", 25, "normal"))
    aa.goto(0, -100)
    aa.write("Russia surrenders.", False, align= "center", font=("Courier", 25, "normal"))
    time.sleep(3)
    aa.clear()
    aa.goto(0, 0)
    aa.write("CONGRATULATIONS, PRESIDENT" + name + ". YOU WIN.", False, align= "center", font=("Courier", 25, "bold"))

def moscow_attack (aa):
    global bb, gif2, gif
    wn = turtle.Screen()
    clear_b(bb)
    wn.addshape(os.path.expanduser('explosion2.gif'))
    gif3 = turtle.Turtle()
    gif3.speed(0)
    gif3.hideturtle()
    gif3.shape(os.path.expanduser('explosion2.gif'))
    gif3.up()
    gif3.goto(-420, 220)
    gif3.down()
    gif2.clear()
    gif3.stamp()
    time.sleep(1.5)
    aa.clear()
    time.sleep(1)
    gif3.clear()
    gif.clear()
    aa.up()
    aa.goto(0, 100)
    aa.write("With its government destroyed, Russia cannot retaliate.", False, align= "center", font=("Courier", 25, "normal"))
    aa.goto(0, -100)
    aa.write("You nuke all other sites. It's the only way to be sure.", False, align= "center", font=("Courier", 25, "normal"))
    time.sleep(3)
    aa.clear()
    aa.goto(0, 0)
    aa.write("YOUR 8-YEAR TERM HAS ENDED. THANKS FOR PLAYING.", False, align= "center", font=("Courier", 25, "bold"))

def yekat_attack(aa):
    global bb, gif2, gif
    wn = turtle.Screen()
    clear_b(bb)
    wn.addshape(os.path.expanduser('explosion2.gif'))
    gif3 = turtle.Turtle()
    gif3.speed(0)
    gif3.hideturtle()
    gif3.shape(os.path.expanduser('explosion2.gif'))
    gif3.up()
    gif3.goto(-151, 70)
    gif3.down()
    gif2.clear()
    gif3.stamp()
    time.sleep(1.5)
    aa.clear()
    time.sleep(1)
    gif3.clear()
    gif.clear()
    aa.up()
    aa.goto(0, 100)
    aa.write("Russia now has no economy and only a handful of nukes.", False, align= "center", font=("Courier", 25, "normal"))
    aa.goto(0, -100)
    aa.write("A chance strike lands on your presidential bunker.", False, align= "center", font=("Courier", 25, "normal"))
    time.sleep(3)
    aa.clear()
    aa.goto(0, 0)
    aa.write("REST IN PEACE. GAME OVER.", False, align= "center", font=("Courier", 25, "bold"))

def nov_attack(aa):
    global bb, gif2, gif
    wn = turtle.Screen()
    clear_b(bb)
    wn.addshape(os.path.expanduser('explosion2.gif'))
    gif3 = turtle.Turtle()
    gif3.speed(0)
    gif3.hideturtle()
    gif3.shape(os.path.expanduser('explosion2.gif'))
    gif3.up()
    gif3.goto(126, -48)
    gif3.down()
    gif2.clear()
    gif3.stamp()
    time.sleep(1.5)
    aa.clear()
    time.sleep(1)
    gif3.clear()
    gif.clear()
    aa.up()
    aa.goto(0, 100)
    aa.write("You have chosen poorly. Russia immediately retaliates.", False, align= "center", font=("Courier", 25, "normal"))
    aa.goto(0, -100)
    aa.write("By a slim margin, America prevails in the nuclear war.", False, align= "center", font=("Courier", 25, "normal"))
    time.sleep(3)
    aa.clear()
    aa.goto(0, 0)
    aa.write("THE WORLD HAS BECOME A WASTELAND. GAME OVER.", False, align= "center", font=("Courier", 25, "bold"))

def choice1_4_3_result(aa):
    global bb
    aa.clear()
    clear_b(bb)
    aa.write("Not a single nation chooses to side with either the US or Russia. Nuclear war is imminent.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.write("Congress advises that you strike Russia first.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    choice1_4_2_result(aa)

def choice1_4_4_result(aa):
    global bb
    aa.clear()
    clear_b(bb)
    aa.write("Congress impeaches you for laziness.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(3)
    aa.clear()
    aa.write("When you exit the bunker, the US has become a violent wasteland.", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(3)
    aa.clear()
    aa.write("GAME OVER", False, align="center", font=("Courier", 25, "normal"))
    time.sleep(3)
    aa.clear()
    aa.write("THANK YOU FOR PLAYING!", False, align="center", font=("Courier", 15, "normal"))
    time.sleep(3)
    aa.clear()


def choice2result (aa):                                         # choice B main branch 1
    global bb, name
    aa.clear()
    clear_b(bb)
    aa.write("Political stability increases, however militants still threaten Syria.", False, align = "center", font = ("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.goto(0, 300)
    aa.write("It has been revealed that Russia is making nukes. How will you respond, President" + name + "?", False, align = "center", font = ("Courier", 20, "normal"))
    aa.goto(0, 260)
    aa.write("1. Place economic sanctions on Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 220)
    aa.write("2. Send 500 American inspectors and diplomats to Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 180)
    aa.write("3. Do nothing", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 140)
    aa.write("4. Initiate nuclear war with Russia.", False, align="center", font=("Courier", 15, "normal"))
    choice_boxes(bb)


def choice3result (aa):                                                     #choice C main branch 1
    global bb, name
    aa.clear()
    clear_b(bb)
    aa.write("The militants are destroyed. Syria faces political unrest.", False, align = "center", font = ("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.goto(0, 300)
    aa.write("It has been revealed that Russia is making nukes. How will you respond, President" + name + "?", False, align="center", font=("Courier", 20, "normal"))
    aa.goto(0, 260)
    aa.write("1. Place economic sanctions on Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 220)
    aa.write("2. Send 500 American inspectors and diplomats to Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 180)
    aa.write("3. Do nothing", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 140)
    aa.write("4. Initiate nuclear war with Russia.", False, align="center", font=("Courier", 15, "normal"))
    choice_boxes(bb)


def choice4result (aa):                                                      #choice D main branch 1
    global bb, name
    aa.clear()
    clear_b(bb)
    aa.write("Rumors of your laziness spread.", False, align = "center", font = ("Courier", 15, "normal"))
    time.sleep(2)
    aa.clear()
    aa.goto(0, 300)
    aa.write("It has been revealed that Russia is making nukes. How will you respond, President" + name + "?", False, align="center", font=("Courier", 20, "normal"))
    aa.goto(0, 260)
    aa.write("1. Place economic sanctions on Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 220)
    aa.write("2. Send 500 American inspectors and diplomats to Russia.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 180)
    aa.write("3. Do nothing", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 140)
    aa.write("4. Initiate nuclear war with Russia.", False, align="center", font=("Courier", 15, "normal"))
    choice_boxes(bb)


def choice(x, y):
    global aa, choose_click, second_click, nuclear_war, russia_nuke
    print("x:", x, "y:", y)
    if choose_click == True:
        if x > -350 and x < -250 and y > 0 and y < 100:
            choice1result(aa)
            choose_click = False
            second_click = True
        elif x > -150 and x < -50 and y > 0 and y < 100:
            choice2result(aa)
            choose_click = False
            second_click = True
        elif x > 50 and x < 150 and y > 0 and y < 100:
            choice3result(aa)
            choose_click = False
            second_click = True
        elif x > 250 and x < 350 and y > 0 and y < 100:
            choice4result(aa)
            choose_click = False
            second_click = True
        else:
            print("President, your mouse needs repositioning.")
    elif second_click == True:
        if x > -350 and x < -250 and y > 0 and y < 100:
            choice1_1_result(aa)
            second_click = False
            nuclear_war = True
        elif x > -150 and x < -50 and y > 0 and y < 100:
            choice1_2_result(aa)
            second_click = False
            nuclear_war = True
        elif x > 50 and x < 150 and y > 0 and y < 100:
            choice1_3_result(aa)
            second_click = False
            nuclear_war = True
        elif x > 250 and x < 350 and y > 0 and y < 100:
            choice1_4_result(aa)
            second_click = False
            nuclear_war = True
        else:
            print("President, your mouse is in the wrong place.")
    elif nuclear_war == True:
        if x > -350 and x < -250 and y > 0 and y < 100:
            choice1_4_1_result(aa)
            nuclear_war = False
        elif x > -150 and x < -50 and y > 0 and y < 100:
            choice1_4_2_result (aa)
            nuclear_war = False
            russia_nuke = True
        elif x > 50 and x < 150 and y > 0 and y < 100:
            choice1_4_3_result(aa)
            nuclear_war = False
            russia_nuke = True
        elif x > 250 and x < 350 and y > 0 and y < 100:
            choice1_4_4_result(aa)
            nuclear_war = False
        else:
            print("Choose wisely.")
    elif russia_nuke == True:
        if x > -457 and x < 370 and y > 306 and y < 400:
            stpetersburg_attack(aa)
            russia_nuke = False
        if x > -466 and x < -376 and y > 173 and y < 266:
            moscow_attack(aa)
            russia_nuke = False
        if x > -190 and x < -110 and y > 27 and y < 109:
            yekat_attack(aa)
            russia_nuke = False
        if x > 84 and x < 170 and y > -90 and y < -6:
            nov_attack(aa)
            russia_nuke = False
        else:
            print("President, our intelligence has indicated that no significant targets are located in that area.")
def clear_b (bb):
    bb.clear()

def choice_boxes(bb):
    bb.hideturtle()
    bb.up()
    bb.goto(-350, 0)
    bb.down()
    for i in range(4):
        squareChoice(bb)
        bb.up()
        bb.seth(0)
        bb.forward(200)
        bb.down()
    bb.up()
    bb.goto(-300, 40)
    bb.write("1", False, align= "center", font=("fixedsys", 20, "bold"))
    bb.goto(-100, 40)
    bb.write("2", False, align= "center", font=("fixedsys", 20, "bold"))
    bb.goto(100, 40)
    bb.write("3", False, align= "center", font=("fixedsys", 20, "bold"))
    bb.goto(300, 40)
    bb.write("4", False, align= "center", font=("fixedsys", 20, "bold"))



def main():
    global name, choose_click, aa, bb

    wn = turtle.Screen()
    # wn.bgcolor("black")
    aa = turtle.Turtle()
    # aa.color("White")
    bb = turtle.Turtle()
    # bb.color("White")
    sleep_time = 3                                                      #variable for sleeping time
    bb.speed(0)
    aa.up()
    aa.hideturtle()
    aa.goto(0, 200)
    aa.write("POTUS", False, align="center", font = ("Times", 60, "normal"))
    time.sleep(sleep_time)
    aa.clear()
    aa.goto(0, 180)
    aa.write("The year is 2037. You are the President of the United States.", False, align="center", font = ("Courier", 30, "bold"))
    time.sleep(sleep_time)
    aa.goto(0, 130)
    aa.write("Decades of corruption have ruined the US.", False, align="center", font = ("Courier", 30, "bold"))
    time.sleep(sleep_time)
    aa.clear()
    aa.write("You are the last hope.", False, align="center", font = ("Courier", 30, "bold"))
    time.sleep(sleep_time)
    aa.clear()

    aa.goto(0, 200)
    aa.write("Enter your last name, President", False, align="center", font=("Courier", 20, "normal"))
    name = raw_input("My last name is:")                                                                #raw input does not work with numbers
    time.sleep(1)
    aa.clear()
    aa.goto(0, 300)
    aa.write("Secretary: President " + name + ", the civil war in Syria has escalated. Will you provide aid?", False, align="center", font=("Courier", 20, "normal"))
    aa.goto(0, 260)
    aa.write("1. Provide economic and military aid.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 220)
    aa.write("2. Provide only economic aid.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 180)
    aa.write("3. Provide military aid.", False, align="center", font=("Courier", 15, "normal"))
    aa.goto(0, 140)
    aa.write("4. Ignore your secretary.", False, align="center", font=("Courier", 15, "normal"))


    choice_boxes(bb)

    choose_click = True
    wn.onscreenclick(choice)
    turtle.done()




main()