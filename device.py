from model_util import EventHandler
from interface import Interface, Button, KeyboardKey, KeyboardDeleteKey, TextBox

class Device(EventHandler):
	def __init__(self, name, label, top_left_x, top_left_y, width, height):
		super(Device, self).__init__(name, label, top_left_x, top_left_y, width, height)
		
class TouchScreenDevice(Device):
	def __init__(self, name, label, top_left_x, top_left_y, width, height):
		super(TouchScreenDevice, self).__init__(name, label, top_left_x, top_left_y, width, height)
		
	def create_screen(self, name, label, top_left_x, top_left_y, width, height):
		return TouchScreen(name, label, top_left_x, top_left_y, width, height)

class Screen(EventHandler):

	def __init__(self, name, label, top_left_x, top_left_y, width, height):
		super(Screen, self).__init__(name, label, top_left_x, top_left_y, width, height)

class TouchScreen(Screen):
	
	def __init__(self, name, label, top_left_x, top_left_y, width, height):
		super(TouchScreen, self).__init__(name, label, top_left_x, top_left_y, width, height)

class DeviceBuilder:

	def __init__(self):
		self.device = None

	def set_screen(self, screen, top_left_x, top_left_y):
		'''Setting to default locations'''
		self.device.add_child(screen, top_left_x, top_left_y)
		return self

	def get_result(self):
		return self.device

class TouchScreenDeviceBuilder(DeviceBuilder):
	
	def __init__(self, name, label, top_left_x, top_left_y, width, height):
		self.device = TouchScreenDevice(name, label, top_left_x, top_left_y, width, height)

def constructKeyboard(keyboard, TOUCHBAR_OPTION=1):
	# Add keys.
	transcript_textbox = None
	default_key_width = 170
	default_key_height = 170
	default_touchbar_height = 70
	if TOUCHBAR_OPTION == 1:
		touchbar = ['esc','paste','newSlide','table','picture','shapes','TextBox','copy','presentMode',"<",'bright_1','volumn_1','mute_1','siri_1']
	elif TOUCHBAR_OPTION == 2:
		touchbar = ['End Show', 'slides', 'time', 'rehearse', "<",'bright_2','volumn_2','mute_2','siri_2']
	elif TOUCHBAR_OPTION == 3:
		touchbar = ['bright-', 'slider', 'bright+', 'out_3']
	elif TOUCHBAR_OPTION == 4:
		touchbar = ['out_4', 'light-', 'light+', 'layout', 'launchpad', 'keylight-', 'keylight+', '<<', '>||', '>>', 'mute_4', 'vol-', 'vol+', 'siri_4']

	key_rows = [touchbar,\
	["~\n`",'1','2','3','4','5','6','7','8','9','0',"_\n-","+\n=",'del'],\
	['tab','q','w','e','r','t','y','u','i','o','p',"{\n[","}\n]","|\n\\"],\
	['cap','a','s','d','f','g','h','j','k','l',":\n;","\"\n\'",'return'],\
	['shift1','z','x','c','v','b','n','m',"<\n,",">\n.","?\n/",'shift2'],\
	['fn','ctrl','opt1','cmd1',' ','cmd2','opt2','left',"up\ndown",'right']]

	# Starting key positions.
	key_top_left_x = 0
	key_top_left_y = 0

	for key_row, idx in zip(key_rows, range(len(key_rows))):
		key_width = default_key_width
		key_height = default_key_height

		key_top_left_x = 0
		if idx == 0 and TOUCHBAR_OPTION == 1:
			key_height = default_touchbar_height
			# esc
			key_top_left_x = 110
			key_button = KeyboardKey(key_row[0], key_row[0], key_top_left_x, 0, 140, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# paste, newSlide, 'table','picture','shapes','TextBox',
			key_top_left_x += 140 + 35
			for ii in range(1,7):
				key_button = KeyboardKey(key_row[ii], key_row[ii], key_top_left_x, 0, 150, key_height, transcript_textbox)
				keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
				key_top_left_x += 150 + 30
			# 'copy','presentMode',
			key_top_left_x += 75

			for ii in range(7,9):
				key_button = KeyboardKey(key_row[ii], key_row[ii], key_top_left_x, 0, 160, key_height, transcript_textbox)
				keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
				key_top_left_x += 160 + 30

			# <
			key_top_left_x += 5
			key_button = KeyboardKey(key_row[9], key_row[9], key_top_left_x, 0, 30, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 30
			for i in range(4):
				key_button = KeyboardKey(key_row[i+10], key_row[i+10], key_top_left_x, 0, 160, key_height, transcript_textbox)
				keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
				key_top_left_x += 160
			print(key_top_left_x)
		elif idx == 0 and TOUCHBAR_OPTION == 2:
			key_height = default_touchbar_height
			# end show
			key_top_left_x = 110
			key_button = KeyboardKey(key_row[0], key_row[0], key_top_left_x, 0, 230, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 230 + 230
			# slides
			key_button = KeyboardKey(key_row[1], key_row[1], key_top_left_x, 0, 770, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 770 + 35
			# time
			key_button = KeyboardKey(key_row[2], key_row[2], key_top_left_x, 0, 230, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 230 + 30

			# rehearse
			key_button = KeyboardKey(key_row[3], key_row[3], key_top_left_x, 0, 150, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 150 + 35

			# <
			key_top_left_x += 5
			key_button = KeyboardKey(key_row[4], key_row[4], key_top_left_x, 0, 30, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 30
			for i in range(4):
				key_button = KeyboardKey(key_row[i+5], key_row[i+5], key_top_left_x, 0, 160, key_height, transcript_textbox)
				keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
				key_top_left_x += 160
			print(key_top_left_x)
		elif idx == 0 and TOUCHBAR_OPTION == 3:
			key_height = default_touchbar_height
			# vol-
			key_top_left_x = 1250 - 160 - 30
			key_button = KeyboardKey(key_row[0], key_row[0], key_top_left_x, 0, 150, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# slide
			key_top_left_x += 150
			key_button = KeyboardKey(key_row[1], key_row[1], key_top_left_x, 0, 520, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# vol-
			key_top_left_x += 520
			key_button = KeyboardKey(key_row[2], key_row[2], key_top_left_x, 0, 150, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# out
			key_top_left_x += 150
			key_button = KeyboardKey(key_row[3], key_row[3], key_top_left_x, 0, 100, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 100
			print(key_top_left_x)
		elif idx == 0 and TOUCHBAR_OPTION == 4:
			key_height = default_touchbar_height
			# out
			key_top_left_x = 110
			key_button = KeyboardKey(key_row[0], key_row[0], key_top_left_x, 0, 120, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# light-
			key_top_left_x += 120 + 60
			key_button = KeyboardKey(key_row[1], key_row[1], key_top_left_x, 0, 165, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# light+
			key_top_left_x += 165
			key_button = KeyboardKey(key_row[2], key_row[2], key_top_left_x, 0, 165, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# layout
			key_top_left_x += 165 + 35
			key_button = KeyboardKey(key_row[3], key_row[3], key_top_left_x, 0, 165, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# launchpad
			key_top_left_x += 165 + 35
			key_button = KeyboardKey(key_row[4], key_row[4], key_top_left_x, 0, 165, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# keylight-
			key_top_left_x += 165 + 35
			key_button = KeyboardKey(key_row[5], key_row[5], key_top_left_x, 0, 165, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# keylight+
			key_top_left_x += 165
			key_button = KeyboardKey(key_row[6], key_row[6], key_top_left_x, 0, 165, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# <<
			key_top_left_x += 165 + 35
			key_button = KeyboardKey(key_row[7], key_row[7], key_top_left_x, 0, 140, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# >||
			key_top_left_x += 140
			key_button = KeyboardKey(key_row[8], key_row[8], key_top_left_x, 0, 140, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# >>
			key_top_left_x += 140
			key_button = KeyboardKey(key_row[9], key_row[9], key_top_left_x, 0, 140, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# mute
			key_top_left_x += 140 + 35
			key_button = KeyboardKey(key_row[10], key_row[10], key_top_left_x, 0, 140, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# vol-
			key_top_left_x += 140
			key_button = KeyboardKey(key_row[11], key_row[11], key_top_left_x, 0, 140, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# vol+
			key_top_left_x += 140
			key_button = KeyboardKey(key_row[12], key_row[12], key_top_left_x, 0, 140, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			# siri
			key_top_left_x += 140 + 35
			key_button = KeyboardKey(key_row[13], key_row[13], key_top_left_x, 0, 165, key_height, transcript_textbox)
			keyboard.add_child(key_button, key_top_left_x, key_top_left_y)
			key_top_left_x += 165
			print(key_top_left_x)




		else:
			for key in key_row:
				if key in ['del','tab']:
					key_width = 260
				elif key in ['cap','return']:
					key_width = 305
				elif key in ['shift1',"shift2"]:
					key_width = 395
				elif key in ['cmd1','cmd2']:
					key_width = 215
				elif key in [' ']:
					key_width = 890
				else:
					key_width = 170
				key_button = KeyboardKey(key, key, key_top_left_x, key_top_left_y, key_width, key_height, transcript_textbox)

				keyboard.add_child(key_button, key_top_left_x, key_top_left_y)

				key_top_left_x += key_width + 10

		if idx == 0:
			key_top_left_y += key_height + 40
		else:
			key_top_left_y += key_height + 10
	return keyboard

class TouchScreenKeyboardDeviceDirector:
	@staticmethod
	def construct(name, label, top_left_x, top_left_y, width, height, h_bezel, v_bezel, TOUCHBAR_OPTION=1):
		touch_screen_device_builder = TouchScreenDeviceBuilder(name, label, top_left_x, top_left_y, width, height)
		
		# Place a screen on the device.
		screen = touch_screen_device_builder.device.create_screen('touchscreen', 'touchscreen', top_left_x + h_bezel, top_left_y + v_bezel, width - 2*h_bezel, height - 2*v_bezel)

		default_textbox_margin = 10
		default_textbox_width = screen.width - 2*default_textbox_margin
		default_textbox_height = ((screen.width - 10) / 30) + 20
		default_textbox_character_width = (screen.width - 10) / 30
		default_textbox_character_height = (screen.width - 10) / 30

		# Place a textbox with transciprion phrase at the top of the screen.
		phrase_textbox = TextBox('phrase_textbox', '', default_textbox_margin, default_textbox_margin, 0, 0, 0, 0)
		screen.add_child(phrase_textbox, default_textbox_margin, default_textbox_margin)

		# Place a textbox with transciprion phrase at the top of the screen.
		transcript_textbox = None
		# transcript_textbox = TextBox('transcription_textbox', '', default_textbox_margin, default_textbox_margin + phrase_textbox.top_left_y + phrase_textbox.height, default_textbox_width, default_textbox_height, default_textbox_character_width, default_textbox_character_height)
		# screen.add_child(transcript_textbox, default_textbox_margin, default_textbox_margin + phrase_textbox.top_left_y + phrase_textbox.height)

		# Place a keyboard at the bottom third of the device.
		keyboard_1 = Interface('keyboard_1', 'keyboard_1', 0, 0, screen.width, screen.height)
		keyboard_2 = Interface('keyboard_2', 'keyboard_2', 0, 0, screen.width, screen.height)
		keyboard_3 = Interface('keyboard_3', 'keyboard_3', 0, 0, screen.width, screen.height)
		keyboard_4 = Interface('keyboard_4', 'keyboard_4', 0, 0, screen.width, screen.height)
		screen.add_child(keyboard_1, 0, 0)
		screen.add_child(keyboard_2, 0, 0)
		screen.add_child(keyboard_3, 0, 0)
		screen.add_child(keyboard_4, 0, 0)

		keyboard_1 = constructKeyboard(keyboard_1, TOUCHBAR_OPTION=1)
		keyboard_2 = constructKeyboard(keyboard_2, TOUCHBAR_OPTION=2)
		keyboard_3 = constructKeyboard(keyboard_3, TOUCHBAR_OPTION=3)
		keyboard_4 = constructKeyboard(keyboard_4, TOUCHBAR_OPTION=4)

		return touch_screen_device_builder.set_screen(screen, screen.top_left_x, screen.top_left_y).get_result()

