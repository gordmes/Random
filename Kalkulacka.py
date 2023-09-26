import time
Číslo1= float (input("Zadej první číslo: "))
operace= input ("Zadej znamenko: ")
Číslo2= float (input("Zadej druhé číslo: "))
if operace== "+":
    print(Číslo1+Číslo2)
elif operace== "-":
    print(Číslo1-Číslo2)
elif operace== "*":
    print(Číslo1*Číslo2)
elif operace== "/":
    print (Číslo1/Číslo2)
else: 
    print ("Chybnej vypocet")
time.sleep(360)