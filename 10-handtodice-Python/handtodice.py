# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
        s=[]
        s1=[]
        while(hand==0):
            k=hand%10
            k1=k//10
        s=s.append(k1)
        s1=s1.reverse(s)
	return s1

    			
   