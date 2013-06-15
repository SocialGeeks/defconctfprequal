# Initial screen  
	badmedicine  
	login  

	Username:  

# Progress  
Whatever username you put in is transformed to hex and dropped into a cookie.  It is not a straight ASCII to hex conversion though.  You need to change the cookie so that it makes you the admin user.  If you just put admin into the cookie, you get an error saying it needs to be in hex.  

# Solution
The value of each letter varied by its offset. I initally figured that the value of the next letter was somehow based on the value of the previous one but it turned out each letter position just had its own set of possible values. So an n in position 1 was different than an n in position 5 but once you had the values you could construct any string you wanted.

admim = 09c8259ca3
barfn = 0acd3a93a0
so admin is obviously 09c8259ca0 -> "the key is The key is: who wants oatmeal raisin anyways twumpAdby"

also oatmeal raisin is the superior cookie so what the hell.
