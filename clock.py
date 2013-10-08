#!/usr/bin/env python

from launchpad import Launchpad
from datetime import datetime
from time import sleep
import sys
from pytz import timezone
import signal

try:
	lp = Launchpad()
except IOError:
	print "no Launchpad, no demo, dude."
	sys.exit(1)

def sigint_handler(signal, frame):
	lp.reset()
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

london = timezone('Europe/London')

DIGITS = [
	[
		" ** ",
		"*  *",
		"*  *",
		" ** ",
	],
	[
		"  * ",
		"  * ",
		"  * ",
		"  * ",
	],
	[
		"*** ",
		"  **",
		" *  ",
		"****",
	],
	[
		"****",
		"  * ",
		"*  *",
		" ** ",
	],
	[
		" *  ",
		"*   ",
		"****",
		"  * ",
	],
	[
		"****",
		"**  ",
		"  **",
		"*** ",
	],
	[
		"*   ",
		"*** ",
		"*  *",
		" ** ",
	],
	[
		"****",
		"   *",
		"  * ",
		" *  ",
	],
	[
		"****",
		" ** ",
		"*  *",
		" ** ",
	],
	[
		" ** ",
		"*  *",
		" ***",
		"   *",
	],
]

def print_digit(digit, coords, colour):
	x0, y0 = coords
	digit_pixels = DIGITS[digit]
	for y in range(0, 4):
		for x in range(0, 4):
			lp.screen[y + y0][x + x0] = colour if digit_pixels[y][x] == '*' else 0x00

while True:
	current_time = datetime.now(tz=london)
	print_digit(current_time.hour / 10, (0, 1), 0x03)
	print_digit(current_time.hour % 10, (4, 1), 0x30)
	print_digit(current_time.minute / 10, (0, 5), 0x30)
	print_digit(current_time.minute % 10, (4, 5), 0x03)
	lp.commit()

	sleep(0.25)
