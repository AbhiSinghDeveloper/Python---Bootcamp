 # An application which tells future based upon the zodiac sign

next = True
while next == True:
    print(''' From all the mentioned Zodiac Signs
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer 
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricorn
    11) Aquarius
    12) Pisces
    ''')

    s = int(input("Pick your sign number and Press Enter to know your future\n"))


    if s==1:
        print("Today, you may receive some kind of material support from family. It is probably for a wise cause, so be sure to use it accordingly, says Ganesha. You may spend the evening with those very loved ones who have supported you.")
    elif s==2:
        print("There is a strong prospect that you will work extremely hard to prove yourself at your workplace today, predicts Ganesha. At times, the returns may not be in proportion to your efforts. You will unwind at the end of the day with a happy and content feeling, expects Ganesha.")
    elif s==3:
        print("Today is an important phase in your life. You will be making a few crucial decisions. At work, you will come up with several fresh ideas, which, along with your willpower, form the winning concoction for your company. In the evening, you may spend a few extra bucks on comforts and entertainment, says Ganesha.")
    elif s==4:
        print("Cancer")
    elif s==5:
        print("Leo")
    elif s==6:
        print("Virgo")
    elif s==7:
        print("Libra")
    elif s==8:
        print("Scorpio")
    elif s==9:
        print("Sagittarius")
    elif s==10:
        print("Capricorn")
    elif s==11:
        print("Aquarius")
    elif s==12:
        print("Pisces")
    else:
        print("Hey You sure about the number?")

    next = True if input("\nShall we do it again? (Y/N) ")=="Y" else False


    if 