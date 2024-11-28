money = (float(input("How much money do you have?")))

#Banaanit maksavat 1,49 euroa / kg, ja yksi banaani painaa 170 grammaa.
#Omenat maksavat 2,49 euroa / kg, ja yksi omena painaa 170 grammaa.
#Appelsiinit maksavat 1,99 euroa / kg, ja yksi appelsiini painaa 270 grammaa.

bananas = money//(1.49*0.17)
apples = money//(2.49*0.17)
oranges = money//(1.99*0.27)

print("You can buy", bananas ,"bananas.")
print("You can buy", apples ,"apples.")
print("You can buy", oranges, "oranges.")