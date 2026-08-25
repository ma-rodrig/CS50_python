#  implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many
# cents in change the user is owed.

# prompt amount due: 50 (only 5, 10 or 25 coins)
# while coin_inserted < 50
# prompt insert coin:
# amount due = 50 - coin_inserted -> print
# change_owned = last_coin_inserted - 50 -> print

cost = 50
amount_due = cost
while amount_due > 0:
	print('Amount Due: ' +str(amount_due))
	amount_inserted = int(input('Insert Coin: '))
	if amount_inserted==25 or amount_inserted==10 or amount_inserted==5:
		amount_due -= amount_inserted
if amount_due <0:
	amount_due = -amount_due

print('Change Owed: '+str(amount_due))