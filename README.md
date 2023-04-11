# Val Discord Bot
Welcome to the all in one Valorant Discord Bot. Using this bot will allow you to get information from valorant without having to open the application. Once everything it implemented you should be able to view your personal items from the store, view your match history, get Valorant news and more. 

# Obtaining a Bot Token
Prior to using the bot, a valid token recieved from Discord is necessary to validate actions requested and sent by the bot.
To obtain one, visit [https://discord.com/developers/]. Afterwards, create a new application.  
<img src="https://user-images.githubusercontent.com/97611396/230943000-27c6f01b-69e3-4cad-99e4-c800c4bba5e8.png" width="400" />  
Afterwards, access the Bot tab and create a new bot.
<img src="https://user-images.githubusercontent.com/97611396/230943920-048eb493-be13-49d9-af2f-668bdb30b1b9.png" width="800" />  
Now, just copy the bot's token to be used later and set it's permission level to administrator.

# Adding the Bot to your server
<img src="https://user-images.githubusercontent.com/97611396/231051226-27ee85ed-3805-4474-b6c2-406e6fe9d71e.png" width="400" />
In the OAUTH2 Link generator, select bot for the scope and adminstrator for the permissions. The link at the bottom will be a link that will allow you to add the bot to any applicable server.  

# How to run
Provide here instructions on how to use your application.   
- Download the latest release from the right hand side of Github.
- On the command line, obtain the following libraries: 
```
pip install discord.py
pip install requests
pip install valorant
```
- Within the createToken.py file adjust the TOKEN field to use the token of your bot's token.
```
keepToken = ''
```
- Run main.py

![image](https://user-images.githubusercontent.com/97611396/231052823-30e45265-fae1-4217-a3b6-76a109574b9d.png)
![image](https://user-images.githubusercontent.com/97611396/231052875-ba652d17-5cd9-49ca-9631-56796d5bf4e4.png)

# How to contribute
Follow this project board to know the latest status of the project: [https://github.com/orgs/cis3296s23/projects/70]([http://...])  

### How to build
- Use this github repository: ... 
- Specify what branch to use for a more stable release or for cutting edge development.  
- Use VSC or other IDEs supporting Python (PyCharm, atom, PyDev, etc...)
- Necessary libraries include: valorant, requests, discord
- What file and target to compile and run. 
- What is expected to happen when the app start. 
