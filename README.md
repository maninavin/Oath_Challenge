# Oath_Challenge
Username and Password validation
Setup Details: 
1.	Pre-requisites: Python 3.6, Flask, sqllite3, hashlib, virtualenv
2.	Pre-requisites can be installed by running following command: pip install -r reqirements.txt 
3.	Command to run flask server: python server.py
4.	URL:  127.0.0.1:5000
Instructions:
Credentials stored in a database are:
Username: mani
Password: Mani@123
URL:  127.0.0.1:5000
Implementation Details:
1.	Following are the validations I have done for username and password
a.	User will be successfully able to login if valid username and password is entered (Username: mani, Password: Mani@123)
b.	I have created SQL lite database to store the user credentials
c.	I have done client-side validations using JavaScript
d.	Password is stored in a (SHA256) hashed format in a database.
e.	So, whenever user enters a password it calculates the hash of the value and verifies if the hash matches with the value stored in database.
f.	If an incorrect username is entered, then “Username not found – Click on forgot username link to recover it” message will be displayed.
g.	If an incorrect password is entered, then “Incorrect Password – Click on forgot password link to recover it” message will be displayed.
Validation Coverage:
I have added following validations for password
•	Password must contain atleast one lowercase letter
•	Password must contain atleast an uppercase letter
•	Password must contain atleast a number
•	Password must contain a special character
•	Length of password must be atleast 8 characters.
I have created hyperlinks for Forgot Password/ Forgot Username

Planned Coverage:
1.	Apart from the above implementation I have researched and planned to implement following: 
a.	XSS and SQL injection handling
b.	Implement HTTPS (https://www.theverge.com/2018/2/8/16991254/chrome-not-secure-marked-http-encryption-ssl)
c.	Flask based backend uses base64 encoding by default to encrypt messages. It becomes important to add salt so that session information doesn't get decrypted easily. I will decrypt the session cookie using base64 encoding and see if I can see any confidential information in clear text.
d.	I went through the blog which explains the above issue in details https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session
Queries:
a.	For username validation whether special characters will be allowed or not? 
b.	Users email ID can be used for username field or not?



