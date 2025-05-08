setone = {1,2,3,4,5}
print(setone)

print(setone & {1,3}) # & se hmlog set ka intersection find kr skte h 
print(setone | {1,3}) # | se hmlog set ka union find kr skte h 
print(setone | {1,3,4,4,5,6,7}) # | se hmlog set ka union find kr skte h 

print(setone - {1,2,3,4,5}) # set ko pura subtract kr dene se set() output aata h jo ki wo ek dict type hota h 