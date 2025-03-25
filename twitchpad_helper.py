import configparser

VALID_SCHEMES = ['XBX', 'PS', 'NINT']
DEFAULT_AUTH_VALUE = 'example_channel_name'
DEFAULT_OAUTH_VALUE = 'oauth:exampletokengibberishvalue'
DEFAULT_VOTING_DURATION = 15

class TwitchpadConfig():
	def __init__(self, channel_name="", oauth_token="", scheme="", default_voting_duration=DEFAULT_VOTING_DURATION):
		self.channel_name = channel_name
		self.oauth_token = oauth_token
		self.scheme = scheme
		self.default_voting_duration = default_voting_duration

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

def read_config_ini():
	config = configparser.ConfigParser()
	try:
		config.read('config.ini')
	except Exception as e:
		print(f"Error occured: Make sure that a config.ini file exists and it has valid syntax.")
		print(f"Error message: {e}")
		exit(1)

	channel_name = ""
	oauth_token = ""
	scheme = ""
	default_voting_duration = DEFAULT_VOTING_DURATION

	try:
		channel_name = config['AUTHENTICATION']['CHANNEL_NAME']

		if channel_name is None or channel_name == DEFAULT_AUTH_VALUE:
			raise ValueError("Error occured: Invalid CHANNEL_NAME value - make sure to input your channel name in config.ini without any quotes!")
			exit(1)	

	except Exception as e:
		print(f"Error occured: Make sure that you've entered your channel name in config.ini without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	try:
		oauth_token = config['AUTHENTICATION']['OAUTH_TOKEN']

		if oauth_token is None or oauth_token == DEFAULT_OAUTH_VALUE:
			raise ValueError("Error occured:Invalid OAUTH_TOKEN value - make sure to input your OAUTH token in config.ini without any quotes!")
			exit(1)	
	except Exception as e:
		print(f"Error occured: Make sure that you've entered your generated OAUTH_TOKEN in config.ini without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	try:
		scheme = config['INPUT_SCHEME']['SCHEME']

		if scheme is None or scheme not in VALID_SCHEMES:
			raise ValueError("Error occured: Invalid SCHEME option - make sure to input XBX, PS or NINT without any quotes.")
			exit(1)

	except Exception as e:
		print(f"Error occured: Make sure that you've entered a valid scheme in config.ini - as XBX, PS or NINT without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	try:
		selected_voting_duration = config['VOTING_DURATION']['SECONDS']

		if is_int(selected_voting_duration):
			if int (selected_voting_duration) < 15:
				selected_voting_duration = 15
			elif int(selected_voting_duration) > 120:
				selected_voting_duration = 120
			default_voting_duration = int(selected_voting_duration)
		else:
			print("Ignoring error: Voting duration chosen is not a valid integer in seconds - defaulted to 30 seconds.")

	except Exception as e:
		print(f"Error occured: Make sure that you've entered a valid value for SECONDS in the config.ini, such as 15, 30 or 120 without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	return TwitchpadConfig(channel_name, oauth_token, scheme, default_voting_duration)

		