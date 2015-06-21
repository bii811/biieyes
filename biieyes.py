#!/usr/bin/python
#biieyes.py
# -S 7 is minimum for ID 041e:4088 Creative Technology, Ltd

import os

if not os.path.exists('biieyespic'):
	os.makedirs('biieyespic')
while True:
	f = os.popen('fswebcam -S 15 -r 320x240 --jpeg 95 --save biieyespic/%d%m%y%H%M%S.jpg')
	out = f.read()
	print(out)
