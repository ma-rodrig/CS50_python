#implement a program that prompts the user for items, one per line,
# until the user inputs control-d (which is a common way of ending
# one’s input to a program). Then output the user’s grocery list in
# all uppercase, sorted alphabetically by item, prefixing each line
# with the number of times the user inputted that item

from collections import OrderedDict

list = {
}
#getting items
while True:
    try:
        item=input().strip().upper()
    except EOFError:
        break
    else:
        if item in list:
            list[item]+=1
        else:
            list[item]=1
#sort list
sorted_keys = sorted(list.keys())
sorted_list = {key:list[key] for key in sorted_keys}
#print list
for item in sorted_list:
    print( sorted_list[item], item)
