from PIL import Image, GifImagePlugin

PanelWidth = 2
PixelWidth = 32

PanelHeight = 2
PixelHeight = 32

MatrixDimensions = (PixelWidth,PixelHeight)

gifFilename = 'buybuybuy.gif'
gifObject = Image.open(gifFilename)

if not gifObject.is_animated:
	raise Exception("GIF is Not Animated")
print('{} is {} frame long'.format(gifFilename, gifObject.n_frames))

for frameIndex in range(0,gifObject.n_frames):
	
	gifObject.seek(frameIndex)
	ledFrame = gifObject.resize(MatrixDimensions)

	ledFrameRGB = ledFrame.convert('RGB')
	print(ledFrameRGB)
	print(ledFrameRGB.getbands())


	# Traverse Panel #1
	for x in range(0, PixelWidth):
		for y in range(0, PixelHeight):
			print(ledFrameRGB.getpixel((x,y)))

	# print(ledFrameRGB.getdata(['R']))


	# ledFrameRGB.show()
	break # only show first frame




# 4 Panel Pattern
# Row	LED Array Indices
# 0 	15 <---- 0
# 1 	16 ---> 31
# 2 	47 <--- 32
# 3 	48 ---> 63
# 4 	79 <--- 64
# 5 	80 ---> 95
# 6 	111 <-- 96
# 7 	112 --> 127
# 8 	143 <-- 128
# 9 	144 --> 159
# 10 	175 <-- 160
# 11 	176 --> 191
# 12 	207 <-- 192
# 13 	208 --> 223
# 14 	239 <-- 224
# 15 	240 --> 245

# 16    261 <-- 246
#
#