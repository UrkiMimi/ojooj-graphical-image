#Libraries
from PIL import Image
import json

#Clamp function
def clamp(num, min, max):
    if num >= max:
        return max
    elif num <= min:
        return min
    else:
        return num

#Main conversion script
def imageToOJ(imagePath, resFactor=1):
    # Import and scale image
    image = Image.open(imagePath).convert('RGB')
    width, height = [round(image.size[0]/resFactor), round(image.size[1]/resFactor)]
    image = image.resize((width, height))

    # Seperate image by channel
    pixelR = image.getchannel('R').getdata()
    pixelG = image.getchannel('G').getdata()
    pixelB = image.getchannel('B').getdata()

    # Generate uppercase alphabet characters for brightness levels
    chars = []
    for i in range(26):
        chars.append(chr(65+i))

    #bruh
    ojStr = ''
    ojList = []

    # For loop for adding the characters from each channel
    for r in range(width*height):
                ojStr += chars[clamp(pixelR[r] // 26, 0,25)]
                ojStr += chars[clamp(pixelG[r] // 26, 0,25)]
                ojStr += chars[clamp(pixelB[r] // 26, 0,25)]

    # bruh number 2
    ojStr = ('*'.join(ojStr[i:(i + width*3)] for i in range(0, len(ojStr), width*3)))

    # bruh number 3
    # Convert string to proper list (yes im stupid)
    temp = ''
    for str in ojStr:
        if str == '*':
            ojList.append(temp)
            temp = ''
        else:
            temp += str

    ojList.append(temp)
    return ojList

# Prep JSON file and export image
imageJsn = json.loads('{}')
imageJsn['image'] = imageToOJ('ojgi test.gif')

# Export JSON
with open('example.json','w') as f:
    f.write(json.dumps(imageJsn,indent=2))