import configparser

VALID_SCHEMES = ['XBOX', 'PS']

class TwitchpadConfig():
	def __init__(self, channel_name="", oauth_token="", scheme=""):
		self.channel_name = channel_name
		self.oauth_token = oauth_token
		self.scheme = scheme

def read_config_ini():
	config = configparser.ConfigParser()
	try:
		config.read('custom-config.ini')
	except e as Exception:
		print(f"Error occured: Make sure that a config.ini file exists and it has valid syntax.")
		print(f"Error message: {e}")
		exit(1)

	channel_name = ""
	oauth_token = ""
	scheme = ""

	try:
		channel_name = config['AUTHENTICATION']['CHANNEL_NAME']
	except e as Exception:
		print(f"Error occured: Make sure that you've entered your channel name in config.ini without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	try:
		oauth_token = config['AUTHENTICATION']['OAUTH_TOKEN']
	except e as Exception:
		print(f"Error occured: Make sure that you've entered your generated OAUTH_TOKEN in config.ini without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	try:
		scheme = config['INPUT_SCHEME']['SCHEME']

		if scheme not in VALID_SCHEMES:
			raise ValueError("Invalid scheme option - make sure to input XBOX or PS as the SCHEME without any quotes.")
			exit(1)			

	except e as Exception:
		print(f"Error occured: Make sure that you've entered a valid scheme in config.ini - as XBOX or PS without any quotes.")
		print(f"Error message: {e}")
		exit(1)

	return TwitchpadConfig(channel_name, oauth_token, scheme)

		