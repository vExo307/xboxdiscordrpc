# Xbox Discord RPC
Lightweight Discord RPC for your Xbox games, works with xbox one and xbox 360, made in Python.

### What this is
This shows all your friends what game you are currently playing, and for how long you have been playing it. As of right now that is all it does, however if you have any suggestion feel free to make a pull request, or DM me on Discord if you would rather me implement it. 

### What this is not
This is a extremely early version of this project, so there may be a few bugs, as of right now I know that it works with Xbox 360, and it should work with Xbox One. If you encounter any bugs please submit and issue, and I will work to resolve it ASAP

### How to download and configure this program
When you download it you will have 3 files; Main.py, Config.json, and requirments.txt, simple enough. For just using the program it is not required to do anything in the Main.py, but the Config.json will need some editing. Firstly go to the [Discord Developer Portal](https://discord.com/developers/applications) and create an app, I just named mine Xbox, NOTE: Whatever you name your application is what will show on your RPC as playing, in my case it is "Playing Xbox". In your newly created app you are going to want to copy the client ID, and paste it into the first field of Config.json. Secondly you are going to want to figure out which discord you are using. If you are using the normal discord client, your client will be 0, if you are using PTB, your client will be 1, if you are using Canary your client will be 3. Those are the 3 I currently know about. Nextly you are going to want to find your Xbox Live ID(XUID), and you can do it [here](https://xbonline.live/home/xuid.php), and past it into the XUID spot. Now for the second to last step in the config, you are going to sign up for the Xbox Live API, and receive an API key. It is 60 requests per hour on a free account, so if you set your delay correctly you should be fine. You can always upgrade for a faster delay, and more requests. Once you go to the [API](https://xapi.us/) click sign up, and make your account, you will have to link it with your Xbox Live account. In your dashboard will be your API key, which you can copy and paste into the config slot. Now for the last step of the config, the delay. By default this is 60, meaning 60 seconds between each update. This can be changed to as high or low as you want(Minimum of 15 seconds). Adjust based on if you get rate limited or not. 

### How to use this program 
Once you configure the program we can get to the fun part using it! Make sure you have python version 3.8 installed, and use the following command
> pip3 install -r requirements.txt 
>
Once this is done you use the following command
> python3 main.py
>
Now the program should be running and working! It is required that the program is running whilst you want the presence to be shown.

### License & Me
GNU GPL v3 License
and I am vExo307, heres my discord:
vExo307#5145
