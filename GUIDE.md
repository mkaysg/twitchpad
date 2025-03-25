# Twitchpad Guide

The syntax for Twitchpad follows the general structure of:

`!<input> <optional joystick direction>`

* ___!___ - prefix character required for Twitchpad
* ___input___ - button, joystick or trigger
* ___joystick direction
    * ___joystick direction___ - compass direction (from n,ne,e...nw) when joysticks are set as input

The expanded commands with length and strength modifier follows the general structure of:

`!<length> <input> <(not required for other buttons) joystick direction / trigger strength>`

* ___!___ - prefix character required for Twitchpad
* ___length___ - duration of action
* ___input___ - button, joystick or trigger
* ___joystick direction / trigger strength___
    * ___joystick direction___ - compass direction (from n,ne,e...nw) when joysticks are set as input
    * ___trigger strength___ - number from 0 to 10 indicating trigger strength when triggers are set as input

## Examples
__Using the `XBX` scheme:__

__Tap Shortcuts__ - 

`!a` - tap the A button for 0.2s

`!up` - tap the Up direction button for 0.2s

`!lt` - tap the Left trigger at 100% for 0.2s

`!ls nw` - tap the Left Joystick in northwest direction


__Expanded commands__ - 

`!tap a` - tap the A button for 0.2s

`!press up` - press the Up directional button for 0.4s

`!med ls n` - push the Left Joystick to North for 1.0s

`!long lt 10` - depress the Left Trigger at 100% for 6.0s

`!hold a` - hold the A button indefinitely

`!stop a ` - resets the A button to default

_Note: The stop command cannot interrupt ongoing actions; it will simply reset the button to default, which is to stop engaging that input._


## Reference List
### General Commands
| command   | description |
|-----------|----------|
|!twitchpad  |prints URL to this list of inputs|
|!twstart   |start Twitchpad in Instant mode|
|!twvote   |start Twitchpad in Voting mode|
|!twstop   |stop receiving inputs and set Twitchpad to Standby mode|
|!last       |prints last input in chat|
|!lreset     |resets the last input to default; not for interruption|
|!reset      |resets all inputs to default|


### Tap Shortcuts

| XBX | PS | NINT | Description |
|:----:|:----:|:----:|----------|
|!up|!up|!up|Tap Up Directional Button|
|!down|!down|!down|Tap Down Directional Button|
|!left|!left|!left|Tap Left Directional Button|
|!right|!right|!right|Tap Right Directional Button|
|!a|!x - for X|!b|Tap Bottom Face Button|
|!b|!c - for ◯|!a|Tap Right Face Button|
|!x|!s - for ⬜|!y|Tap Left Face Button|
|!y|!t - for △|!x|Tap Top Face Button|
|!start|!start|!+|Tap Right Menu Button|
|!back|!select|!-|Tap Left Menu Button|
|!lsb|!l3|!lsb|Tap Left Joystick Button|
|!rsb|!r3|!rsb|Tap Right Joystick Button|
|!lb|!l1|!l|Tap Left Shoulder|
|!rb|!r1|!r|Tap Right Shoulder|
|!lt|!l2|!zl|Tap Left Trigger|
|!rt|!r2|!zr|Tap Right Trigger|
|!ls {direction}|!ls {direction}|!ls {direction}|Tap Left Joystick in the specified compass direction|
|!rs {direction}|!rs {direction}|!rs {direction}|Tap Right Joystick in the specified compass direction|

### Joystick Direction
* _Mandatory to provide direction when joystick is entered._

| direction    | compass direction |
|-----------|----------|
|n      |North   |
|ne     |Northeast   |
|e      |East   |
|se     |Southeast   |
|s      |South   |
|sw     |Southwest   |
|w      |West   |
|ne     |Northeast   |

### Expanded Commands
### Length

| length    | duration (seconds) |
|-----------|----------|
|!tap        |0.2s   |
|!press      |0.4s   |
|!2press     |0.6s   |
|!3press     |0.8s   |
|!med        |1.0s   |
|!2med       |2.0s   |
|!3med       |4.0s   |
|!long       |6.0s   |
|!2long      |8.0s   |
|!3long      |10.0s  |
|!hold       |indefinite|
|!stop       |halts that input|

### Inputs (case insensitive)

| XBX | PS | NINT | Description |
|:----:|:----:|:----:|----------|
|up|up|up|Up Directional Button|
|down|down|down|Down Directional Button|
|left|left|left|Left Directional Button|
|right|right|right|Right Directional Button|
|a|x - for X|b|Bottom Face Button|
|b|c - for ◯|a|Right Face Button|
|x|s - for ⬜|y|Left Face Button|
|y|t - for △|x|Top Face Button|
|start|start|+|Right Menu Button
|back|select|-|Left Menu Button
|lsb|l3|lsb|Left Joystick Button|
|rsb|r3|rsb|Right Joystick Button|
|lb|l1|l|Left Shoulder|
|rb|r1|r|Right Shoulder|
|lt|l2|zl|Left Trigger|
|rt|r2|zr|Right Trigger|
|ls|ls|ls|Left Joystick|
|rs|rs|rs|Right Joystick|

### Joystick Direction
* _Mandatory to provide direction when joystick is entered._

| direction    | compass direction |
|-----------|----------|
|n      |North   |
|ne     |Northeast   |
|e      |East   |
|se     |Southeast   |
|s      |South   |
|sw     |Southwest   |
|w      |West   |
|ne     |Northeast   |

### Trigger Strength
* _Default value is 100% if strength is not provided when trigger is entered._

| strength   | trigger strength (%) |
|-----------|----------|
|0      |0%   |
|1      |10%   |
|2      |20%   |
|3      |30%   |
|4      |40%   |
|5      |50%   |
|6      |60%   |
|7      |70%   |
|8      |80%   |
|9      |90%  |
|10     |100%|