# Start Here

To get up and running, you'll need a few things.   

```shell
pip install discord.py
```

as well as setting up the bot user on your discord account on.

https://discordapp.com/developers/applications/me

## Running the bot with docker (recommended)

Just getting my initial container out there, nothing fancy, just a ubuntu container with the files slapped in there. 
To run the container, it only need the env var "discord_bot_token" which you will have to figure out how to get...

```shell
docker built -t discord_bot .
docker run -d -e "discord_bot_token=<super_secret_token>" discord_bot
```

### Test/Prod Workflows

Github actions is going to provide mechanism to deploy this app to my self-hosted runner. 

* 'test_" must prefix all of your branch names. 
* only 1 'instance' of each enviornment will be availble at a time
* after a branch 'passes' testing, create a pull request to merge it into master.

### What Next?

- [x] create github actions flow to test container build process on server
- [x]  create github action flow to deploy container on home server
- [ ]  improving quotes.json, adding more gifs.
- [ ]  improving readme... 
- [ ]  creating the branch/merge workflow gating mechanism. 
