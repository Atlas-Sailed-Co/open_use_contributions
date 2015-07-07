from PIL import Image
import sys
import os
import math

def computeSpectralEntropy(imageFile):
    im = Image.open(imageFile)
    rgbHistogram = im.histogram()
    rgbEntropy = [] 
    try:
	    for rgb in range(3):
	    	totalPixels = sum(rgbHistogram[rgb * 256 : (rgb + 1) * 256])
	        ent = 0.0
	        for col in range(rgb * 256, (rgb + 1) * 256):
	        	freq = float(rgbHistogram[col]) / totalPixels
	        	if freq > 0:
	        		ent = ent + freq * math.log(freq, 2)
	        ent = -ent
	        rgbEntropy.append( ent )
    except:
       print 'non RGB img'
    return rgbEntropy


def squareImages(imageFile):
	squareSize = 128
	im = Image.open(imageFile)
	name = imageFile.split('/')
	print len(name)
	n = name[len(name)-1]
	w, h = im.size
	i = 0
	print w,h
	print w-squareSize , h-squareSize
	while i < w:
		#print "i ", i
		j = 0
		while j < h:
			#print "j ", j
			save_path = "data/"+str(i)+"-"+str(j)+"-" + n
			#print save_path
			#im.crop( (i, i+squareSize, j, j + squareSize) ).save(save_path)
			#new_img = im.crop( (i, 0, 64, 64) )
			left = i
			top = j
			width = squareSize
			height = squareSize
			box = (left, top, left+width, top+height)
			area = im.crop(box)
			area.save(save_path)
			j = j + squareSize
		i = i + squareSize








#root_dir = './data/'

#print 'Snannon Entropy for Red, Green, Blue:'
root_dir = './data/'

# myCode ="""I could draw you a picture of what 'Collaborate' means. 
#            These words look like many different rising digital waves. 
#            Different, frequencies and periods, but eventually all of the waves will hit at once. 
#            That is a thing to be curious about. 
#            The time of transition. 
#            Thinking about this, it used to be such a impossible thought. 
#            Imagine a human race able to instaneously communicate to everyone at once. 
#            It's a scene of complete chaos when considered with an honest simulation. 
#            But that is not what I am talking about achieving. 
#            The experiment to be performed with the digital wave is similar to the amazing REDDIT button. 
#            Look at all of those people able to coordinate an action. 
#            We want to work on creating fast transitions for large groups of people. 
#            Imagine being able to build a bluetooth meshnet across a college campus just like that. 
#            Or any number of other times when the winners are a collection of individuals who manage to transition quickly and together. 
#            To measure collaboration: record timing traces."""


for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
    	#print file
    	#result = computeSpectralEntropy(os.path.join(directory,file))
    	try:
    		print os.path.join(directory,file)
    		result = computeSpectralEntropy(os.path.join(directory,file))
    		print "Result: ", result
    		spectral_entropy_sum = result[0] + result[1] + result[2]
    		print "spectral Entropy Sum: ", spectral_entropy_sum 
    		if (spectral_entropy_sum > 22):
				im = Image.open(os.path.join(directory,file))
				n = file.split('/')
				name = n[len(n)-1]
				save_path = "./high-ent/" + name
				im.save(save_path)
    	except:
    		pass







