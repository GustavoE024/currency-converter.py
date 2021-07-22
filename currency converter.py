def conversor(kind_dollar,value_yuan):
    dollar=input("¿how many  dollars" +kind_dollar+ "do I have?:  ")
    dollar=float(dollar)
    yuan=dollar/value_yuan
    yuan=round(yuan,  4)
    yuan=str(yuan)
    print("have $"+yuan+"yuan")


menu = """
Welcome coversor money $ ;)

1 - Dollar us
2 - Dollar canadian
3 - Dollar australian

choose an option"""

option =input(menu)

if option=="1":
    conversor("US",6.49)
elif option=="2":
   conversor("canadian",5.09)
elif option=="3":
    conversor("australian",4.76)
else:
    print("enter a correct option please")

