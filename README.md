# Twitchpad - Gamepad Inputs via Chat!

Play any game that supports Xbox Controller / Gamepad input via Twitch Chat!

A simple Python script that leverages on twitchio and vgamepad. For Windows.

## Limitations
* Only games that support input from Xbox Controllers / Gamepads are supported.
* Guide button is not mapped - main concern is chat opening up your Steam Big Picture / Steam Overlay. But I'm aware some emulators use the guide button as a menu to save state, etc. I'd need more opinions on this.
* At the moment, it doesn't support more than one virtual controller. Though, Twitch Chat PvP anyone? Streamer vs Twitch Chat should be possible; you can connect your joystick to be Player 1 then start Twitchpad afterwards to let chat be Player 2. I think.
* Currently, interrupting an ongoing commmand is not possible. A sleep function is, for example, used as a way to hold a button for a given duration. So you'd have to wait out the duration. I'd need to implement a form of multi-threading that can interrupt commands.

## Risks
* Your chat might delete your precious items in-game. Or worst, your saves.
* If Steam recognizes the Virtual Controller and allows Desktop control, chat WILL wreak havoc. You should turn off Desktop Control in Steam Big Picture as such:
`Menu > Settings > Controller > Desktop Layout [Edit] > Settings/gear icon > Disable Steam Input > Confirm `
* Similarly, if you have some middleware between the controller and Windows that allows Desktop navigation with a gamepad, you should disable that.

## First Steps

### Python 3.9 via Miniconda
* Download and install Miniconda. Miniconda is a virtual environment manager for Python that allows you to have different virtual environments of differing Python versions. It manages dependencies that are compatible for a particular Python version.  https://docs.anaconda.com/miniconda/miniconda-install/
* Follow the installation process and recommended steps to install for __one user only__. 

### Twitch OAUTH Token
* __DO NOT SHARE YOUR TOKEN WITH ANYONE__ as it provides access to your account. Treat it like a password.
* __DO NOT SHARE COPIES OF THE SCRIPT__ that could contain your oauth token and channel name. Instead, direct them here.
* Obtain your Twitch OAUTH token for Twitchpad to send / receive chat messages from Twitch API. The Token will allow Twitchpad to authenticate as you. It is private to you and Twitch. https://twitchapps.com/tmi/

### Git
* Install Git to clone and keep the project updated. https://git-scm.com/downloads/win
* Press the 'Click here to download' link and follow through the installation process.

## Cloning the Repository and Installing Dependencies

Once that's done, you can clone the repository and install dependencies with an automated .bat script.

1. Download `Setup_Twitchpad.bat` from Releases. Place it in a new folder. You may receive an anti-malware notification; you can always open the .bat file in Notepad and see what it does.
2. Double-click `Setup_Twitchpad.bat`. The script will clone the Twitchpad repository and run the necessary installation of dependencies.
3. There will be a pop up of a Virtual Controller installer. This comes with the vgamepad library - click through it to get it installed.
4. Once done, Notepad will open `config.ini` for you to enter your Twitch OAUTH token and Twitch Channel name in it.
5. You can also change the scheme to `XBOX`, `PS` or `SWITCH`. This determines which chat inputs will Twitchpad respond to.

## Starting it up!

1. Make sure that you've filled in the necessary info in `config.ini`.
2. Make sure there's no other controllers connected if you want Twitchpad to be the primary Player 1 gamepad.
3. Double-click `Start_Twitchpad.bat`. After a successful authentication to Twitch, it will immediately begin reading inputs from Chat, so be careful!
4. Advisable to have the game in the foreground and focused i.e. you've clicked on it after starting Twitchpad.
5. If you accidentally press on the Command Prompt window and see a static rectangle cursor, this means you've interrupted the script. You can press the title bar of the Command Prompt to let it continue.
6. The Command Prompt logs inputs from Twitch chat and will also display error messages, which can be handy for bug reports.
7. If things get out of control, immediately close Twitchpad. Have fun!

## Keeping things updated...

* Simply double-click `Update_Twitchpad.bat` to pull new updates from the repository!

## Wiki
Head over to the Wiki to view available inputs.

You can also run `!twitchpad` in Twitch chat when the script is running to get a link to the wiki.

## Me
[__Twitch Channel:__](https://www.twitch.tv/mkay_sg)

[__Tip:__](https://paypal.me/mkaysg)

[__Patreon:__](https://www.patreon.com/mkay_sg)


## Special Thanks
* [twitchio](https://github.com/PythonistaGuild/TwitchIO)
* [vgamepad](https://github.com/yannbouteiller/vgamepad)
* [Emree](https://www.twitch.tv/emree) for entertaining the idea during their streams.