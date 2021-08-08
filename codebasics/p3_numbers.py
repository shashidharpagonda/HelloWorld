"""
1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
"""
len=92
width=48.8
area =len*width
print('1',area)

"""
2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
   Find out using python, how many dollars is the shopkeeper going to give you back?
"""
no_of_chips_Pkts=9
cost_of_each_pkt=1.49
total_cost=9*1.49
change_frm_shopkeeper=20-total_cost
print('2 change from shop keeper is: ',str(change_frm_shopkeeper))

"""
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
   If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
   Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
"""
area=5.5**2
tilecost=500
total_cost_for_tiles=area*tilecost
print('3 total cost for tiles:',total_cost_for_tiles)

"""
4. Print binary representation of number 17
"""

dec=17
bRep=bin(17)
print('4 Binary rep of',dec,'is:',bRep)
print('4 Binary rep of',dec,'is:',format(dec,'b'))




