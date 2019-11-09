# Start Here

To get up and running, you'll need a few things.   

pip install discord.py


as well as setting up the bot user on your discord account on.

https://discordapp.com/developers/applications/me

## Running the bot

python3 bot.py

## Running the bot with docker (recommended)

Just getting my initial container out there, nothing fancy, just a ubuntu container with the files slapped in there. 
To run the container, it only need the env var "discord_bot_token" which you will have to figure out how to get...

```shell
docker built -t discord_bot .
docker run -d -e "discord_bot_token=<super_secret_token>" discord_bot
```

