# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
        nofc=(eggs)//(12)
        co=(nofc)%12
        if(co==0):
            return co
        else:
            return co+1
