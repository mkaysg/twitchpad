# Twitchpad - Gamepad Inputs via Chat!

Play any game that supports the Xbox 360 Controller input via Twitch Chat!

A simple Python script that leverages on twitchio and vgamepad. For Windows only.

## Pre-Requisites

### Python 3
* Install Python 3. https://www.python.org/downloads/

### Twitch OAUTH Token
* Obtain your Twitch OAUTH token for Twitchpad to send authorized requests as you to Twitch API. https://twitchapps.com/tmi/
* DO NOT SHARE YOUR TOKEN WITH ANYONE as it provides access to your account. Treat it like a password.
* DO NOT SHARE COPIES OF THE SCRIPT that could contain your oauth token and channel name. Instead, direct them here.

### Git
* Install Git to clone and keep the project updated. https://git-scm.com/downloads/win

## Setting it up

1. Download the Setup_Twitchpad.bat file from Releases and place it in a new folder on your PC. 
2. Then double-click the file to clone the Twitchpad repository and run the necessary installation of dependencies.
3. There will be a pop up of a Virtual Controller installer that comes with the vgamepad library - simply click through it to get it installed.
4. Once done, you will be reminded to open the newly generated config.ini file to enter your Twitch OAUTH token and Twitch Channel name in it.
5. You can also change the scheme between `XBOX` or `PS` that determines which chat inputs will Twitchpad respond to.

## Starting it up!

1. Make sure that you've filled in the necessary deets in the config.ini file as above.
2. Make sure there's no other controllers connected as we want the Virtual Gamepad to be the primary gamepad / player 1 gamepad.
3. Double-click the Start_Twitchpad.bat file in the folder. The script will immediately begin reading inputs from Chat, so be careful!
4. Make sure your game is in the foreground and focused i.e. you've clicked on it after starting Twitchpad.
5. A Command Prompt window will appear. Make sure not to click on it as it may interrupt the Command Prompt. If you've accidentally interrupted it, press the title bar of the Command Prompt.
6. The Command Prompt logs inputs from Twitch chat and will also throw error messages, which can be handy for bug reports.
7. If things go awry, immediately close Twitchpad. This may accidentally happen if Steam Input takes over and allows Desktop control, which is a big no-no.

## Keeping things updated...

* Simply run the Update_Twitchpad.bat file to pull new updates from the repository!

## Limitations
* Only games that support input from an Xbox 360 controller are supported.
* Guide button is the only button not mapped - main concern is to prevent chat from opening up your Steam Big Picture / Steam overlay? But I understand some emulators may use the guide button as a menu to save state, etc. I'd need to deliberate more on this.
* At the moment, it doesn't support more than one virtual controller.
* Currently, doesn't support interrupting a command due to using a sleep function as a way to press a button for a given duration. I probably need to implement multi-threading that can help interrupt commands.

## Risks
* Your chat might delete your precious items in-game. Or worst, your saves.
* If Steam hooks into the Virtual Controller to allow Desktop control, chat may wreak havoc. You should turn off Desktop Control in Steam Big Picture as such:
`Menu > Settings > Controller > Desktop Layout [Edit] > Settings/gear icon > Disable Steam Input > Confirm `

## Wiki
Head over to the Wiki to view available inputs.

You can also run `!twitchpad` in Twitch chat when the script is running to get a link to the wiki.

## Other Stuff
__Twitch Channel:__ https://www.twitch.tv/mkay_sg

__Tip:__ https://paypal.me/mkaysg


## Special Thanks
Special thanks to Emree for entertaining the idea during a few Gran Turismo 4 streams. 