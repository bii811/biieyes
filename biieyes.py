#!/usr/bin/python
#biieyes.py

import os

if not os.path.exists('biieyespic'):
	os.makedirs('biieyespic')

while(1):
	f = os.popen('fswebcam -d v4l2:/dev/video0 -i 0 -F 1 -S 1 -r 320x240 --jpeg 90 -l 3 biieyespic/%d%m%y%H%M%S.jpg')
	out = f.read()
	print(out)
