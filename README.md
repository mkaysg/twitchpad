# Twitchpad - Gamepad Inputs via Chat!

Play any game that supports Xbox Controller / Gamepad input via Twitch Chat!

A simple Python script that leverages on twitchio and vgamepad. For Windows.

![Twitchpad Preview](https://i.imgur.com/Yiatlum.png "Twitchpad Preview")

## Limitations
* Only games that support input from Xbox Controllers / Gamepads are supported.
* Guide button is not mapped - main concern is chat opening up your Steam Big Picture / Steam Overlay. But I'm aware some emulators use the guide button as a menu to save state, etc. I'd need more opinions on this.
* PS Scheme doesn't send inputs as DualShock 4 controller for simplicity reasons; it will still send as Xbox Controller input. It is more for emulated games to match their control scheme, whereas PC games tend to default to Xbox button scheme.
* Stream latency is the biggest issue - this means games that are frame sensitive will require an impressive amount of anticipation from Chat, which makes Twitchpad more suitable for turn-based games. But never underestimate chat.
* At the moment, it doesn't support more than one virtual controller. I do like the idea of Twitch Chat PvP though! Streamer vs Twitch Chat should be possible; you can connect your joystick to be Player 1 then start Twitchpad afterwards to let chat be Player 2. I think. But the stream latency will give you the advantage unless its turn-based.
* Currently, interrupting an ongoing commmand is not possible. Twitchpad uses a sleep function as a way to hold a button for a given duration. So you'd have to wait out the duration.

## Risks
* Your chat might delete your precious items in-game. Or worst, your saves.
* If Steam recognizes the Virtual Controller and allows Desktop control, chat WILL wreak havoc. You should turn off Desktop Control in Steam Big Picture as such:
`Menu > Settings > Controller > Desktop Layout [Edit] > Settings/gear icon > Disable Steam Input > Confirm `
* Similarly, if you have some middleware between the controller and Windows that allows Desktop navigation with a gamepad, you should disable that.

## First Steps

### Twitch OAUTH Token
* __DO NOT SHARE YOUR TOKEN WITH ANYONE__ as it provides access to your account. Treat it like a password.
* __DO NOT SHARE COPIES OF THE SCRIPT__ that could contain your oauth token and channel name. Instead, direct them here.
* Obtain your Twitch OAUTH token for Twitchpad to send / receive chat messages from Twitch API. The Token will allow Twitchpad to authenticate as you. It is private to you and Twitch. https://twitchapps.com/tmi/
* Keep the token somewhere safe!

### ViGEmBus Setup
* Next, as vgamepad depends on ViGEmBus to emulate a virtual controller, you will have to install it manually first. You can get `ViGEmBusSetup_x64.msi` from [here](https://github.com/nefarius/ViGEmBus/releases/download/setup-v1.17.333/ViGEmBusSetup_x64.msi)!

## Downloading and Configuring Twitchpad

1. Once you've obtained your OAUTH token and installed ViGEmBus, you can download the latest `Twitchpad.7z` file from Releases.
2. After downloading, unzip the file in a folder of your choice.
3. You will see a  `config.ini` file. Double-click it to to enter your Twitch OAUTH token and Twitch Channel name in it.
4. You can also change the scheme to `XBX`, `PS` or `NINT`. This determines which chat inputs Twitchpad will respond to.

## Starting it up!

1. Make sure that you've filled in the necessary info in `config.ini`.
2. Make sure there's no other controllers connected if you want Twitchpad to be the Player 1 gamepad.
3. Double-click `Twitchpad.exe`. After a successful authentication to Twitch, it will inform you its connected and a message will be printed to your Chat. It will immediately begin reading inputs from Chat, so be careful! If it fails to authenticate or to read the data from `config.ini`, double-check that your channel name, OAUTH token and Scheme are correctly entered.
4. It's advisable to have the game in the foreground and focused i.e. you've clicked on it after starting Twitchpad.
5. If you've accidentally pressed on the Command Prompt window and see a static rectangle cursor, this means that you have interrupted the script. You can press the title bar of the Command Prompt or press Enter to let it continue.
6. The Command Prompt logs inputs from Twitch chat and will also display error messages, which can be handy for bug reports!
7. If things get out of control, immediately close Twitchpad. Have fun! :>

## Keeping things updated...

* If you have a Github account, you may track the project via the top-right button `Watch > check the Releases box`
* Currently there's no method for auto-updating

## Wiki
Head over to the Wiki to view available inputs.

You can also run `!twitchpad` in Twitch chat when the script is running to get a link to the wiki!

## If you are cloning the repo...

This project was developed in a virtual environment using Python 3.9.

## Other Unimportant Stuff
[__Twitch Channel__](https://www.twitch.tv/mkay_sg) | [__Tip__](https://paypal.me/mkaysg) | [__Patreon__](https://www.patreon.com/mkay_sg)

## Special Thanks
* [twitchio](https://github.com/PythonistaGuild/TwitchIO)
* [vgamepad](https://github.com/yannbouteiller/vgamepad)
* [ViGEmBus](https://github.com/nefarius/ViGEmBus)