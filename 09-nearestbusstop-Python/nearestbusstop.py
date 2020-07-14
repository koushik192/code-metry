# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
        v=(street//8)
        l=(street-(8*v))
        hi=(8*(v+1))-(street)
        if(l<=hi):
            return 8*v
        else:
            return 8*(v+1)
