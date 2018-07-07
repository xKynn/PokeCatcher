# PokecordCatcher

## Getting Started

You can clone this repo, or hit the big green download button on the top right. 

### Setting Up 
1. You need to have python 3.6 or newer to be able to run this on your device. grab python [here] (https://www.python.org/downloads/latest).  
2. While installing this make sure you tick to install python in PATH, and the option to insall the 'py launcher'.  
3. Once this is done, run setup.bat. This should install all the required dependencies for running the bot.  
4. You will require the token of the account you want to run this bot on, it's better if it's an alt as selfbots violate ToS and you can get banned.  
To grab your token visit [Token Tutorial](https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial).  

### Config  

Open edit-this-example-config.json up with any text editor, now put your token in the "".  
After you are done editing this config, please rename the file to `config.json`.  
Other options in config are:  
 - priority: In this list you can add pokemon that bypass the catch rate, pokemon that you absolutely want to catch.
 - catch_rate: This is a percent out of 100.
 - delay: A delay in seconds to try and catch a pokemon after PokeCord spawns one.
 - delay_on_priority: This can be set to `true` or `false`. True means delay will still apply on priority pokemon, false means an instant catch.
 - priority_only: Setting this to `true` means only priority pokemon will be caught.
 - avoid_list: A list just like priority, add names of pokemon you want the bot to ignore.
 - whitelist_channels: A list of channel IDs, so the bot will only catch pokemon on these channels.
 - blacklist_channels: A list of channel IDs, so the bot will catch in all channels except these.
 - verbose: Setting this to true will add a bit more info to the console when a pokemon spawns, i.e if pokemon was skipped and where the bot tried to catch a pokemon (server and channel name).
 - NOTE: Only one of whitelist or blacklist can have channel IDs at a time, the other needs to be empty
 - TIP: There are two ways to find a channel's ID, either go to the channel, tag the channel with a #, then add a \\ to it, ex: `\#general`, it will present a number in <>, that number is a channel ID you can use.
      - The second way is to go to discord settings > Appearance > Scroll down and enable Developer Mode, then you can right click on a channel in the left side channel bar and click Copy ID.
 - spammers: A list of tokens for spammer accounts. You MUST make sure the spammers in here all have unique and non similar names to each other.  
 - controller: this is an account ID for the account that can give commands to your duelers or spammers. An account ID can be retrieved using the method in the tip above, just send a message, then right click on the account in the message and copy ID.
 - duel_starter: A list of of account Ids and tokens for duel starter accounts. for example.  
 [[id1, token1], [id2, token2], [id3, token3]]
 - duel_accepter: Same format as duel_starter, but these accounts will accept duels from starters only.
 - duel_channels: A list of channels each pair will duel in, this should coincide with the order of duel ids/tokens, id1:token1 starter will duel id1:token1 accepter in channelid1.
 Example: [channelid1, channelid2, channelid3]

Example config:
```
{
  "token": "<your token>",
  "priority": ["Groudon", "Geodude"],
  "catch_rate": 90,
  "delay": 2,
  "delay_on_priority": true,
  "priority_only": false,
  "avoid_list": ["Rattata", "Poochyena"],
  "whitelist_channels": [369081842038603776, 369081842038603779],
  "blacklist_channels": [],
  "spammers": ["MjAzOMzE4MTUwOTU1MDA4.DhTj7g.XLuUPCKUGbr9AIgWZ5F-y-Iynas",
  "MTkxNjA0MTM2OTQzMjg4w.DhTkHQ.NL6xqM3Gd1m-9fWWKrBETumzcIw"],
  "controller": 203819318150955008,
  "duel_starters": [[4614564781424640, "NDYxNDU2NDcxOTgxNDI0NDhTlDQ.3PWYIwnt7v4gGGfjUDgy7z1AqnI"],
                    [4593307651436554, "NDU5MzMwNzU1DM2NTU0.DhTjSg.cEX2RS7EwrtA5Q4Cj1z1fmt5_IY"]],
  "duel_accepters":[[461458938483211, "NDYxNDU4MDc3OTM4NDgzMjEx.Dhw.7MZ2M26M8BfNMsUCZK6wjsfQgTs"],
                    [191604133288320, "MTkxNjAOTQzMjg4MzIw.DhTkHQ.NL6xqM3Gd1m-9fWWKrBETumzcIw"]],
  "duel_channels": [461455567862274, 46229604275200]
}
```

You can use this as a reference to modify your config.json.

### Running the bot
Run `run.bat`.  

## Bug reports and problems

Please open an issue on this repo, you can do this from the issues tab on the top and I'll take a look at it when I can.
