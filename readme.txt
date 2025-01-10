A discord bot that provides the user with information about current stages and shop items. Utilizes the Nintendo app API to retrieve personalized stats for the user. Connects to Microsoft Azure for MySQl for the User Database.
The project is mainly created for a private community due to sensitive data. The bot utilizes user token in order to log into their NSO app, and is recommended not to share tokens with untrusted sources. As an extra layer of security the bot uses AES GCM for a layer of proection.

In order to run the bot, you'll need the API token for the discord bot and to download the package dependencies found in requirements.txt
Once you are ready run python main.py will turn the bot on. 


pip install -r requirements.txt
