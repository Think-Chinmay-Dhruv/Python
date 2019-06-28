
# coding: utf-8

# In[35]:


#Set up

import time
money = 20
cheddarcheese = 0
parmcheese = 0
manchegocheese = 0
level = 1
interest_c = 100
interest_m = 100
interest_p = 100
low_maker = ""


# In[42]:


#Cheese Chooser
def cheesechooser():
    global money
    print("You have $" + str(money) + " in the bank.") 
    time.sleep(2)
    print("To make a cheese, enter the cheese's name in the input bar below")

def cheddar():
    global money, cheddarcheese, interest_c, interest_m, interest_p
    
    if low_maker == "cheddar":
        num_maker_c = input("How many pounds of cheddar do you want to make? (Cheddar costs $2 to make)")
        int_num_c = int(num_maker_c)


        if int_num_c*2 <= money:
            print("You are making " + num_maker_c + " pounds of cheddar")
            time.sleep(2)
            cheddarcheese += int_num_c
            time.sleep(2)
            print("Now, you have " + str(cheddarcheese) + " pounds of cheddar cheese.")
            '''yorn_c = input("Do you want to sell this cheddar now? Customer interest in Cheddar is at " + str(interest_c) + "%."
            low_yorn_c = yorn_c.lower()       


            if low_yorn_c == "yes"'''
            time.sleep(2)
            money_c = (cheddarcheese*2)*interest_c/100
            print("You have sold " + str(cheddarcheese) + " pounds of cheddar. You got $" + str(money_c) + " from the sale")
            cheddarcheese = 0
            time.sleep(2)
            money += money_c
            print("You have $" + str(money) + " in the bank")
            time.sleep(2)
            interest_c -= 5
            interest_m += 5
            interest_p += 5


#Parmesan Function

def parm(): 
        global money, parmcheese, interest_c, interest_m, interest_p
        
        num_maker_p = input("How many pounds of parmesan do you want to make? (Parmesan costs $15 to make)")
        int_num_p = int(num_maker_p)


        if int_num_p*15 <= money:
            print("You are making " + num_maker_p + " pounds of Parmesan")
            time.sleep(2)
            parmcheese += int_num_p
            time.sleep(2)
            print("Now, you have " + str(parmcheese) + " pounds of Parmesan cheese.")
            '''yorn_c = input("Do you want to sell this cheddar now? Customer interest in Cheddar is at " + str(interest_c) + "%."
            low_yorn_c = yorn_c.lower()       


            if low_yorn_c == "yes"'''
            time.sleep(2)
            money_p = (parmcheese*32)*interest_p/100
            print("You have sold " + str(parmcheese) + " pounds of parmesan. You got $" + str(money_p) + " from the sale")
            parmcheese = 0
            time.sleep(2)
            money += money_p
            print("You have $" + str(money) + " in the bank")
            time.sleep(2)
            interest_p -= 5
            interest_m += 5
            interest_c += 5

#Manchego Function

def manchego():
        global manchegocheese, interest_c, interest_m, interest_p

    
    
        num_maker_m = input("How many pounds of manchego do you want to make? (manchego  costs $4 to make)")
        int_num_m = int(num_maker_m)


        if int_num_pm*4 <= money:
            print("You are making " + num_maker_m + " pounds of manchego")
            time.sleep(2)
            manchegocheese += int_num_p
            time.sleep(2)
            print("Now, you have " + str(manchegocheese) + " pounds of manchego cheese.")
            '''yorn_c = input("Do you want to sell this cheddar now? Customer interest in Cheddar is at " + str(interest_c) + "%."
            low_yorn_c = yorn_c.lower()       


            if low_yorn_c == "yes"'''
            time.sleep(2)
            money_p = (manchegocheese*9)*interest_m/100
            print("You have sold " + str(manchegocheese) + " pounds of manchego. You got $" + str(money_m) + " from the sale")
            manchegocheese = 0
            time.sleep(2)
            money += money_m
            print("You have $" + str(money) + " in the bank")
            time.sleep(2)
            interest_p -= 5
            interest_m += 5
            interest_c += 5


# In[ ]:


print("Welcome to Cheese Factory.")
time.sleep(1)
name = input("What is the name of your cheese company? ")


while True:
    maker = input("What cheese do you want to make?")
    low_maker = maker.lower()
    if "parmesan" or "manchego" or "cheddar" in low_maker:
        #Running the code
        if low_maker == "parmesan":
            parm()
        elif low_maker == "manchego":
            manchego()
        elif low_maker == "cheddar":
            cheddar()
    else:
        print("error: entry is not an applicable cheese, please restart program")
        break
    #Cheddar function
    cheesechooser()


    #Checks & Balances
    if money == 120:
        level = 2
    if money == 400:
        level = 3

    

