import configparser

VALID_SCHEMES = ['XBX', 'PS', 'NINT']
DEFAULT_AUTH_VALUE = 'example_channel_name'
DEFAULT_OAUTH_VALUE = 'oauth:exampletokengibberishvalue'

class TwitchpadConfig():
	def __init__(self, channel_name="", oauth_token="", scheme=""):
		self.channel_name = channel_name
		self.oauth_token = oauth_token
		self.scheme = scheme

def read_config_ini():
	config = configparser.ConfigParser()
	try:
		config.read('config.ini')
	except e as Exception:
		print(f"Error occured: Make sure that a config.ini file exists and it has valid syntax.")
		print(f"Error message: {e}")
		exit(1)

	channel_name = ""
	oauth_token = ""
	scheme = ""

	try:
		channel_name = config['AUTHENTICATION']['CHANNEL_NAME']

		if channel_name is None or channel_name == DEFAULT_AUTH_VALUE:
			raise ValueError("Error occured: Invalid CHANNEL_NAME value - make sure to input your channel name in config.ini without any quotes!")
			exit(1)	

	except e as Exception:
		print(f"Error occured: Make sure that you've entered your channel name in config.ini without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	try:
		oauth_token = config['AUTHENTICATION']['OAUTH_TOKEN']

		if oauth_token is None or oauth_token == DEFAULT_OAUTH_VALUE:
			raise ValueError("Error occured:Invalid OAUTH_TOKEN value - make sure to input your OAUTH token in config.ini without any quotes!")
			exit(1)	
	except e as Exception:
		print(f"Error occured: Make sure that you've entered your generated OAUTH_TOKEN in config.ini without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	try:
		scheme = config['INPUT_SCHEME']['SCHEME']

		if scheme is None or scheme not in VALID_SCHEMES:
			raise ValueError("Error occured: Invalid SCHEME option - make sure to input XBX, PS or NINT without any quotes.")
			exit(1)

	except e as Exception:
		print(f"Error occured: Make sure that you've entered a valid scheme in config.ini - as XBX, PS or NINT without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	return TwitchpadConfig(channel_name, oauth_token, scheme)

		