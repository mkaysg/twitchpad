import asyncio
from twitchio.ext import commands
import vgamepad as vgp
import time
from twitchpad_helper import TwitchpadConfig, read_config_ini
from typing import Optional, Union

TWITCH_CHANNEL = ''
TWITCH_TOKEN = ''
SCHEME = 'XBOX'

# Initialize the virtual gamepad
gamepad = vgp.VX360Gamepad()

# Inialize text mapping

XBOX_BUTTON_VALUES = {
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
    'rt': "RT",
    "r2": "R2"
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

    if is_float(duration): 
        if trigger == 'lt' or trigger == 'l2':
            gamepad.left_trigger_float(value_float=trig_value)
        elif trigger == 'rt' or trigger == 'r2':
            gamepad.right_trigger_float(value_float=trig_value)

        gamepad_update_and_sleep(gamepad, duration)

        if trigger == 'lt' or trigger == 'l2':
            gamepad.left_trigger_float(value_float=0)
        elif trigger == 'rt' or trigger == 'r2':
            gamepad.right_trigger_float(value_float=0)

        gamepad_update_and_sleep(gamepad, 0.1)

    elif duration == "hold":

        if trigger == 'lt' or trigger == 'l2':
            gamepad.left_trigger_float(value_float=trig_value)
        elif trigger == 'rt' or trigger == 'r2':
            gamepad.right_trigger_float(value_float=trig_value)

        gamepad_update_and_sleep(gamepad, 0.1)        

    elif duration == "stop":

        if trigger == 'lt' or trigger == 'l2':
            gamepad.left_trigger_float(value_float=0)
        elif trigger == 'rt' or trigger == 'r2':
            gamepad.right_trigger_float(value_float=0)

        gamepad_update_and_sleep(gamepad, 0.1)

def stop_last_input(ctx, gamepad, last_input):

    print(f"Received command: Stop {last_input} from {ctx.author.name}") 

    input_item = ""

    parts = last_input.split()
    input_item = parts[2]

    print(f"Input Item to stop: {input_item}")

    if parts[1] == "pressed":
        gamepad.release_button(get_button_to_key_mapping(input_item))
    elif parts[1] == "moved":
        if input_item == "LEFTSTICK":
            gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
        elif input_item == "RIGHTSTICK":
            gamepad.right_joystick_float(x_value_float=0, y_value_float=0)
    elif parts[1] == "depressed":
        if input_item == "LT" or input_item == "L2":
            gamepad.left_trigger_float(value_float=0)
        elif input_item == "RT" or input_item == "R2":
            gamepad.right_trigger_float(value_float=0)

    gamepad_update_and_sleep(gamepad, 0.1)

def stop_all_inputs(ctx, gamepad):
    print(f"Received command: Stop all inputs from {ctx.author.name}") 

    gamepad.reset()
    gamepad_update_and_sleep(gamepad, 0.1)

def map_button_to_text(button):
    button_text = ""

    if SCHEME == "XBOX":
        button_text = XBOX_BUTTON_VALUES[button]
    elif SCHEME == "PS":
        button_text = PS_BUTTON_VALUES[button]

    return button_text

def get_button_to_key_mapping(button):
    if SCHEME == "XBOX":
        for key, value in XBOX_BUTTON_VALUES.items():
            if button == value:
                return key
    elif SCHEME == "PS":
        for key, value in PS_BUTTON_VALUES.items():
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
        if SCHEME == "XBOX":
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

        if SCHEME == "XBOX":
            self.triggers_map = ['lt', 'rt']
        elif SCHEME == "PS":
            self.triggers_map = ['l2', 'r2']

        self.duration_map = {
            'tap': 0.2,
            '2tap': 0.4,
            '3tap': 0.6,
            '4tap': 0.8,
            'med': 1.0,
            '2med': 2.0,
            '3med': 4.0,
            '4med': 8.0,
            'long': 10.0,
            '2long': 20.0,
            '3long': 40.0,
            '4long': 60.0,
            'hold': "hold",
            "stop": "stop"
        }

        self.mod_commands_map = ['pause']
        self.last_input = ""

    def update_last_input(self, last_input):
        self.last_input = last_input

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

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
        if joystick in self.joysticks_map:
            if direction in self.joysticks_direction_map:
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
        if trigger in self.triggers_map:
            if is_int(trig_value):

                action = "depressed"
                action = determine_action(action, duration, self.duration_map)
                duration, duration_text = determine_duration(duration, self.duration_map)

                trig_value = limit_trig_value(int(trig_value))

                chat_output = f"@{ctx.author.name} {action} {map_trigger_to_text(trigger)} at {trig_value}% {duration_text}!"
                await ctx.send(f"🎮✨ TWITCHPAD | {chat_output} ✨")                

                push_trig_with_update(ctx, gamepad, trigger, float(trig_value/100), duration)
                self.update_last_input(chat_output)
            else:
                await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name}, please provide a valid number between 0 to 100 for trigger value! ✨")       

    @commands.command(name='press')
    async def press_command(self, ctx, command: str, duration: Optional[str]):
        if duration is None:
            duration = 0.2

        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='tap')
    async def tap_command(self, ctx, command: str): 
        duration = "tap"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='2tap')
    async def tap2_command(self, ctx, command: str):
        duration = "2tap"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='3tap')
    async def tap3_command(self, ctx, command: str):
        duration = "3tap"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='4tap')
    async def tap4_command(self, ctx, command: str):
        duration = "4tap"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='med')
    async def med_command(self, ctx, command: str):
        duration = "med"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='2med')
    async def med2_command(self, ctx, command: str):
        duration = "2med"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='3med')
    async def med3_command(self, ctx, command: str):
        duration = "3med"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='4med')
    async def med4_command(self, ctx, command: str):
        duration = "4med"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='long')
    async def long_command(self, ctx, command: str):
        duration = "long"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='2long')
    async def long2_command(self, ctx, command: str):
        duration = "2long"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='3long')
    async def long3_command(self, ctx, command: str):
        duration = "3long"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='4long')
    async def long4_command(self, ctx, command: str):
        duration = "4long"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='hold')
    async def hold_command(self, ctx, command: str):
        duration = "hold"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='stop')
    async def stop_command(self, ctx, command: str):
        duration = "stop"
        await self.translate_command_to_button(ctx, command, duration)

    @commands.command(name='joy')
    async def joy_command(self, ctx, joystick: str, direction: str, duration: Optional[str]):
        if duration is None:
            duration = 0.2
        await self.translate_command_to_joystick(ctx, joystick, direction, duration)

    @commands.command(name='trig')
    async def push_command(self, ctx, trigger: str, trig_value: str, duration: Optional[str]):
        if duration is None:
            duration = 0.2
        await self.translate_command_to_trig(ctx, trigger, trig_value, duration)

    @commands.command(name='last')
    async def last_command(self, ctx):
        await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name} - last input was \"{self.last_input}\" ✨")

    @commands.command(name='twitchpad')
    async def print_twitchpad(self, ctx):
        await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name} - view commands here: xxx ✨")

    @commands.command(name='astop')
    async def stop_all_command(self, ctx):
        await ctx.send(f"🎮✨ TWITCHPAD | @{ctx.author.name} has stopped all inputs! ✨")
        stop_all_inputs(ctx, gamepad)

    @commands.command(name='lstop')
    async def stop_last_command(self, ctx):
        chat_output = f"@{ctx.author.name} stopped the last command - {self.last_input}!"
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