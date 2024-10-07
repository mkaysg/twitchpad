import asyncio
from twitchio.ext import commands
import vgamepad as vgp
import time
from twitchpad_helper import TwitchpadConfig, read_config_ini
from typing import Optional, Union

TWITCH_CHANNEL = ''
TWITCH_TOKEN = ''
SCHEME = 'XBX'

# Initialize the virtual gamepad
gamepad = vgp.VX360Gamepad()

# Inialize text mapping

XBX_BUTTON_VALUES = {
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_A: "A",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_B: "B",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_X: "X",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y: "Y",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP: "UP",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN: "DOWN",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT: "LEFT",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT: "RIGHT",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_START: "START",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_BACK: "BACK",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB: "LEFTSTICKBUTTON",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB: "RIGHTSTICKBUTTON",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER: "LEFTSHOULDERBUTTON",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER: "RIGHTSHOULDERBUTTON"                               
}

PS_BUTTON_VALUES = {
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_A: "X",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_B: "◯",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_X: "⬜",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y: "△",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP: "UP",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN: "DOWN",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT: "LEFT",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT: "RIGHT",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_START: "START",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_BACK: "SELECT",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB: "L3",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB: "R3",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER: "L1",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER: "R1"                               
}

NINT_BUTTON_VALUES = {
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_A: "B",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_B: "A",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_X: "Y",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y: "X",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP: "UP",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN: "DOWN",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT: "LEFT",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT: "RIGHT",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_START: "+",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_BACK: "-",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB: "LEFTSTICKBUTTON",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB: "RIGHTSTICKBUTTON",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER: "SL",
    vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER: "SR"                               
}

STICK_MAP = {
    'ls': "LEFTSTICK",
    'rs': "RIGHTSTICK"
}

DIRECTIONS_MAP = {
    'n': "NORTH",
    'ne': "NORTHEAST",
    'e': "EAST",
    'se': "SOUTHEAST",
    's': "SOUTH",
    'sw': "SOUTHWEST",            
    'w': "WEST",
    'nw': "NORTHWEST"            
}

TRIGGER_MAP = {
    'lt': "LT",
    'l2': "L2",
    'zl': "ZL",
    'rt': "RT",
    "r2": "R2",
    'zr': "ZR"
}

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def limit_trig_value(num):
    if num < 0:
        num == 0
    elif num > 100:
        num == 100

    return num

def gamepad_update_and_sleep(gamepad, duration=0.2):
    gamepad.update()
    time.sleep(float(duration))

def press_button_with_update(ctx, gamepad, button, duration):
    print(f"Received command: {duration} {map_button_to_text(button)} from {ctx.author.name}")

    if is_float(duration): 
        gamepad.press_button(button)
        gamepad_update_and_sleep(gamepad, duration)
        gamepad.release_button(button)
        gamepad_update_and_sleep(gamepad, 0.1)
    elif duration == "hold":
        gamepad.press_button(button)
        gamepad_update_and_sleep(gamepad, 0.1)
    elif duration == "stop":
        gamepad.release_button(button)
        gamepad_update_and_sleep(gamepad, 0.1)

def move_stick_with_update(ctx, gamepad, joystick, x_value, y_value, duration):
    print(f"Received command: {duration} {joystick} {x_value} {y_value} from {ctx.author.name}")        

    if is_float(duration):     
        if joystick == 'ls':
            gamepad.left_joystick_float(x_value_float=x_value, y_value_float=y_value)
        elif joystick == 'rs':
            gamepad.right_joystick_float(x_value_float=x_value, y_value_float=y_value)

        gamepad_update_and_sleep(gamepad, duration)
        
        if joystick == 'ls':
            gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
        elif joystick == 'rs':
            gamepad.right_joystick_float(x_value_float=0, y_value_float=0)

        gamepad_update_and_sleep(gamepad, 0.1)

    elif duration == "hold":
        if joystick == 'ls':
            gamepad.left_joystick_float(x_value_float=x_value, y_value_float=y_value)
        elif joystick == 'rs':
            gamepad.right_joystick_float(x_value_float=x_value, y_value_float=y_value)

        gamepad_update_and_sleep(gamepad, 0.1)

    elif duration == "stop":
        if joystick == 'ls':
            gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
        elif joystick == 'rs':
            gamepad.right_joystick_float(x_value_float=0, y_value_float=0)

        gamepad_update_and_sleep(gamepad, 0.1)

def push_trig_with_update(ctx, gamepad, trigger, trig_value, duration):
    print(f"Received command: {duration} {trigger} {trig_value} from {ctx.author.name}")    

    left_trigger_names = ["LT", "L2", "ZL"]
    right_trigger_names = ["RT", "R2", "ZR"] 

    if is_float(duration): 
        if trigger in left_trigger_names:
            gamepad.left_trigger_float(value_float=trig_value)
        elif trigger in right_trigger_names:
            gamepad.right_trigger_float(value_float=trig_value)

        gamepad_update_and_sleep(gamepad, duration)

        if trigger in left_trigger_names:
            gamepad.left_trigger_float(value_float=0)
        elif trigger in right_trigger_names:
            gamepad.right_trigger_float(value_float=0)

        gamepad_update_and_sleep(gamepad, 0.1)

    elif duration == "hold":

        if trigger in left_trigger_names:
            gamepad.left_trigger_float(value_float=trig_value)
        elif trigger in right_trigger_names:
            gamepad.right_trigger_float(value_float=trig_value)

        gamepad_update_and_sleep(gamepad, 0.1)        

    elif duration == "stop":

        if trigger in left_trigger_names:
            gamepad.left_trigger_float(value_float=0)
        elif trigger in right_trigger_names:
            gamepad.right_trigger_float(value_float=0)

        gamepad_update_and_sleep(gamepad, 0.1)

def stop_last_input(ctx, gamepad, last_input):

    print(f"Received command: Stop the last input by {ctx.author.name} - stopping {last_input}") 

    input_item = ""

    parts = last_input.split()
    input_item = parts[2]

    left_trigger_names = ["LT", "L2", "ZL"]
    right_trigger_names = ["RT", "R2", "ZR"]

    if parts[1] == "pressed":
        gamepad.release_button(get_button_to_key_mapping(input_item))
    elif parts[1] == "moved":
        if input_item == "LEFTSTICK":
            gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
        elif input_item == "RIGHTSTICK":
            gamepad.right_joystick_float(x_value_float=0, y_value_float=0)
    elif parts[1] == "depressed":
        if input_item in left_trigger_names:
            gamepad.left_trigger_float(value_float=0)
        elif input_item in right_trigger_names:
            gamepad.right_trigger_float(value_float=0)

    gamepad_update_and_sleep(gamepad, 0.1)

def stop_all_inputs(ctx, gamepad):
    print(f"Received command: Stop all inputs from {ctx.author.name}") 

    gamepad.reset()
    gamepad_update_and_sleep(gamepad, 0.1)

def map_button_to_text(button):
    button_text = ""

    if SCHEME == "XBX":
        button_text = XBX_BUTTON_VALUES[button]
    elif SCHEME == "PS":
        button_text = PS_BUTTON_VALUES[button]
    elif SCHEME == "NINT":
        button_text = NINT_BUTTON_VALUES[button]

    return button_text

def get_button_to_key_mapping(button):
    if SCHEME == "XBX":
        for key, value in XBX_BUTTON_VALUES.items():
            if button == value:
                return key
    elif SCHEME == "PS":
        for key, value in PS_BUTTON_VALUES.items():
            if button == value:
                return key
    elif SCHEME == "NINT":
        for key, value in NINT_BUTTON_VALUES.items():
            if button == value:
                return key


def map_joystick_to_text(joystick):
    return STICK_MAP[joystick]

def map_joystick_direction_to_text(direction):
    return DIRECTIONS_MAP[direction]

def map_trigger_to_text(trigger):
    return TRIGGER_MAP[trigger]

def determine_action(action, duration, duration_map):
    if duration in duration_map:
        if duration == "stop" or duration == "release":
            action = "stopped"

    return action

def determine_duration(duration, duration_map):
    duration_text = f"for {duration}s"

    if duration in duration_map:
        duration = duration_map[duration]
        
        duration_text = f"for {duration}s"

        if duration == "hold":
            duration_text = f"indefinitely"
        elif duration == "stop" or duration == "release":
            duration_text = f""
    else:
        duration = 0.2
        duration_text = f"for {duration}s"

    return duration, duration_text

# Define a Twitch Bot
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=TWITCH_TOKEN, prefix='!', initial_channels=[TWITCH_CHANNEL])

        # Map commands to buttons
        if SCHEME == "XBX":
            self.command_map = {
                'a': vgp.XUSB_BUTTON.XUSB_GAMEPAD_A,
                'b': vgp.XUSB_BUTTON.XUSB_GAMEPAD_B,
                'x': vgp.XUSB_BUTTON.XUSB_GAMEPAD_X,
                'y': vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y,                        
                'up': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
                'down': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
                'left': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
                'right': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
                'start': vgp.XUSB_BUTTON.XUSB_GAMEPAD_START,
                'back': vgp.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
                'lsbtn': vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
                'rsbtn': vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
                'lsh': vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
                'rsh': vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
            }

        elif SCHEME == "PS":
            self.command_map = {
                'x': vgp.XUSB_BUTTON.XUSB_GAMEPAD_A,
                'c': vgp.XUSB_BUTTON.XUSB_GAMEPAD_B,
                's': vgp.XUSB_BUTTON.XUSB_GAMEPAD_X,
                't': vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y,                        
                'up': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
                'down': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
                'left': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
                'right': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
                'start': vgp.XUSB_BUTTON.XUSB_GAMEPAD_START,
                'select': vgp.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
                'l3': vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
                'r3': vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
                'l1': vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
                'r1': vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
            }

        elif SCHEME == "NINT":
            self.command_map = {
                'b': vgp.XUSB_BUTTON.XUSB_GAMEPAD_A,
                'a': vgp.XUSB_BUTTON.XUSB_GAMEPAD_B,
                'y': vgp.XUSB_BUTTON.XUSB_GAMEPAD_X,
                'x': vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y,                        
                'up': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
                'down': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
                'left': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
                'right': vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
                '+': vgp.XUSB_BUTTON.XUSB_GAMEPAD_START,
                '-': vgp.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
                'lsbtn': vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
                'rsbtn': vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
                'sl': vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
                'l': vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
                'sr': vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
                'r': vgp.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
            }

        self.joysticks_map = ['ls', 'rs']
        self.joysticks_direction_map = {
            'n': [0, 1.0],
            'ne': [0.7, 0.7],
            'e': [1.0, 0],
            'se': [0.7, -0.7],
            's': [0, -1.0],
            'sw': [-0.7, -0.7],            
            'w': [-1.0, 0],
            'nw': [-0.7, 0.7]            
        }

        if SCHEME == "XBX":
            self.triggers_map = ['lt', 'rt']
        elif SCHEME == "PS":
            self.triggers_map = ['l2', 'r2']
        elif SCHEME == "NINT":
            self.triggers_map = ['zl', 'zr']

        self.duration_map = {
            'tap': 0.2,
            'press': 0.4,
            '2press': 0.6,
            '3press': 0.8,
            'med': 1.0,
            '2med': 2.0,
            '3med': 4.0,
            'long': 6.0,
            '2long': 8.0,
            '3long': 10.0,
            'hold': "hold",
            "stop": "stop"
        }

        self.trigger_strength_map = {
            '1': 0.1,
            '2': 0.2,
            '3': 0.3,
            '4': 0.4,
            '5': 0.5,
            '6': 0.6,
            '7': 0.7,
            '8': 0.8,
            '9': 0.9,
            '10': 1.0
        }

        self.mod_commands_map = ['pause']
        self.last_input = ""

    def update_last_input(self, last_input):
        self.last_input = last_input

    async def event_ready(self):
        print(f'Successful Login! Logged in as {self.nick} - Twitchpad is ready!')

        ctx = self.get_channel(TWITCH_CHANNEL)
        if ctx:
            await ctx.send(f"🎮✨ TWITCHPAD is now LIVE! Scheme: {SCHEME} | Use !twitchpad for a link to the commands! ✨")

    async def event_message(self, message):
        # Ignore messages from the bot itself
        # if message.author.name.lower() == TWITCH_NICKNAME.lower():
        #     return

        # Ensure the message has a valid author
        if message.author is None:
            return
        
        await self.handle_commands(message)

    async def translate_command_to_button(self, ctx, command, duration):
        if command in self.command_map:

            action = "pressed"
            action = determine_action(action, duration, self.duration_map)
            duration, duration_text = determine_duration(duration, self.duration_map)

            button = self.command_map[command]

            chat_output = f"@{ctx.author.name} {action} {map_button_to_text(button)} {duration_text}!"
            await ctx.send(f"🎮✨ TWITCHPAD | {chat_output} ✨")

            press_button_with_update(ctx, gamepad, button, duration)
            self.update_last_input(chat_output)

    async def translate_command_to_joystick(self, ctx, joystick, direction, duration):
        if joystick in self.joysticks_map and direction in self.joysticks_direction_map:

            x_value = self.joysticks_direction_map[direction][0]
            y_value = self.joysticks_direction_map[direction][1]

            action = "moved"
            action = determine_action(action, duration, self.duration_map)
            duration, duration_text = determine_duration(duration, self.duration_map)

            chat_output = f"@{ctx.author.name} {action} {map_joystick_to_text(joystick)} {map_joystick_direction_to_text(direction)} {duration_text}!"
            await ctx.send(f"🎮✨ TWITCHPAD | {chat_output} ✨")

            move_stick_with_update(ctx, gamepad, joystick, x_value, y_value, duration)
            self.update_last_input(chat_output)
        else:
            await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name}, please provide a compass direction (n,ne,e,se,s,sw,w,nw)! ✨")

    async def translate_command_to_trig(self, ctx, trigger, trig_value, duration):
        if trig_value is None:
            trig_value = '10'

        if trigger in self.triggers_map and trig_value in self.trigger_strength_map:
            
            trig_value = self.trigger_strength_map[trig_value]

            action = "depressed"
            action = determine_action(action, duration, self.duration_map)
            duration, duration_text = determine_duration(duration, self.duration_map)

            chat_output = f"@{ctx.author.name} {action} {map_trigger_to_text(trigger)} at {(trig_value*100)}% {duration_text}!"
            await ctx.send(f"🎮✨ TWITCHPAD | {chat_output} ✨")                

            push_trig_with_update(ctx, gamepad, trigger, trig_value, duration)
            self.update_last_input(chat_output)
        else:
            await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name}, please provide a valid number between 1 to 10 for trigger strength! ✨")       

    async def input_branches(self, ctx, duration, pad_input, strengthOrDirection):
        pad_input = pad_input.lower()

        if pad_input in self.command_map:
            await self.translate_command_to_button(ctx, pad_input, duration)
        elif pad_input in self.joysticks_map:
            strengthOrDirection = strengthOrDirection.lower()
            await self.translate_command_to_joystick(ctx, pad_input, strengthOrDirection, duration)
        elif pad_input in self.triggers_map:
            await self.translate_command_to_trig(ctx, pad_input, strengthOrDirection, duration)

    @commands.command(name='tap')
    async def tap_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]): 
        await self.input_branches(ctx, "tap", pad_input, strengthOrDirection)

    @commands.command(name='press')
    async def press_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "press", pad_input, strengthOrDirection)

    @commands.command(name='2press')
    async def press2_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "2press", pad_input, strengthOrDirection)

    @commands.command(name='3press')
    async def press3_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "3press", pad_input, strengthOrDirection)

    @commands.command(name='med')
    async def med_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "med", pad_input, strengthOrDirection)

    @commands.command(name='2med')
    async def med2_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "2med", pad_input, strengthOrDirection)

    @commands.command(name='3med')
    async def med3_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "3med", pad_input, strengthOrDirection)

    @commands.command(name='long')
    async def long_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "long", pad_input, strengthOrDirection)

    @commands.command(name='2long')
    async def long2_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "2long", pad_input, strengthOrDirection)

    @commands.command(name='3long')
    async def long3_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "3long", pad_input, strengthOrDirection)

    @commands.command(name='hold')
    async def hold_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "hold", pad_input, strengthOrDirection)

    @commands.command(name='stop')
    async def stop_command(self, ctx, pad_input: str, strengthOrDirection: Optional[str]):
        await self.input_branches(ctx, "stop", pad_input, strengthOrDirection)

    @commands.command(name='last')
    async def last_command(self, ctx):
        await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name} - last input was \"{self.last_input}\" ✨")

    @commands.command(name='twitchpad')
    async def print_twitchpad(self, ctx):
        await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name} - view commands here: https://github.com/mkaysg/twitchpad/blob/main/GUIDE.md ✨")

    @commands.command(name='reset')
    async def stop_all_command(self, ctx):
        await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name} has stopped and reset all inputs! ✨")
        stop_all_inputs(ctx, gamepad)

    @commands.command(name='lreset')
    async def stop_last_command(self, ctx):
        chat_output = f"@{ctx.author.name} resetted the input from the last command - {self.last_input}!"
        await ctx.send(f"🎮✨ TWITCHPAD | {chat_output} ✨") 
        stop_last_input(ctx, gamepad, self.last_input)

    # async def event_command_error(self, ctx, error):
    #     # Check if the error is related to an undefined command
    #     if isinstance(error, commands.CommandNotFound):
    #         await ctx.send(f"🎮✨ TWITCHPAD | {ctx.author.name} ❌ Unknown command: {ctx.content}. Please use a valid command! !twitchpad")

# Run the bot
if __name__ == '__main__':
    current_config = read_config_ini()

    TWITCH_CHANNEL = current_config.channel_name
    TWITCH_TOKEN = current_config.oauth_token
    SCHEME = current_config.scheme

    bot = Bot()
    bot.run()