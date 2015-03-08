#!/usr/bin/python
#biieyes.py

import os

if not os.path.exists('biieyespic'):
	os.makedirs('biieyespic')

while(1):
	f = os.popen('fswebcam --greyscale --jpeg 85 -D 1 -l 2 biieyespic/%d%m%y%H%M%S.jpg')
	out = f.read()
	print(out)
