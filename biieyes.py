#!/usr/bin/python
#biieyes.py

import os

if not os.path.exists('biieyespic'):
	os.makedirs('biieyespic')

while(1):
	f = os.popen('fswebcam -S 1 -r 320x240 --greyscale --jpeg 85 -l 3 biieyespic/%d%m%y%H%M%S.jpg')
	out = f.read()
	print(out)
