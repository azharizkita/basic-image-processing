from PIL import Image
import os

__dir__ = os.path.dirname(__file__)

def openSave():
    print('Opening image...')
    img = Image.open(__dir__+"/images/fish.jpg")
    imageName = 'normal'
    imageFormat = 'png'
    print('Saving as: '+imageName+'.'+imageFormat)
    img.save(__dir__+'/'+imageName+'.'+imageFormat)
    print('Image saved on '+__dir__)
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def quantize():
    img = Image.open(__dir__+"/images/fish.jpg")
    print('Quantizing image...')
    img = img.quantize(16)
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def convertRGB():
    img = Image.open(__dir__+"/images/fish.jpg")
    imageName = 'RGB'
    print('Converting into '+imageName+' Mode...')
    img = img.convert(imageName)
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def convertL():
    img = Image.open(__dir__+"/images/fish.jpg")
    imageName = 'L'
    print('Converting into '+imageName+' Mode...')
    img = img.convert(imageName)
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def convertP():
    img = Image.open(__dir__+"/images/fish.jpg")
    imageName = 'P'
    print('Converting into '+imageName+' Mode...')
    img = img.convert(imageName)
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def crop():
    img = Image.open(__dir__+"/images/fish.jpg")
    width, height = img.size
    print('Cropping image...')
    img = img.crop((100,100,width/2,height/2))
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def flip():
    img = Image.open(__dir__+"/images/fish.jpg")
    print('Flipping image...')
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def rotate(degree):
    img = Image.open(__dir__+"/images/fish.jpg")
    print('Rotating image with',degree,'degree...')
    img = img.rotate(degree)
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def copyPaste():
    img = Image.open(__dir__+"/images/fish.jpg")
    width, height = img.size
    print('Pasting image...')
    img.paste(img.resize((int(width/2),int(height/2))), (int(width/10),int(height/10)))
    print('Showing image...')
    img.show()
    input('\npress enter to continue...\n')
    img.close()

def histogramRGB():
    print('Loading matplotlib library...')
    import matplotlib.pylab as plt
    img = Image.open(__dir__+"/images/fish.jpg")
    print('Processing image...')
    r, g, b = img.split()
    maximumValue = [max(r.histogram()), max(g.histogram()), max(b.histogram())]
    print('Showing Histogram...')
    plt.figure(figsize=(40,40))
    plt.subplot(1,3,1).set_ylim([0, max(maximumValue)]); plt.bar(range(256), r.histogram(), color='r'); plt.title('Red Channel')
    plt.subplot(1,3,2).set_ylim([0, max(maximumValue)]); plt.bar(range(256), g.histogram(), color='g'); plt.title('Green Channel')
    plt.subplot(1,3,3).set_ylim([0, max(maximumValue)]); plt.bar(range(256), b.histogram(), color='b'); plt.title('Blue Channel')
    plt.show()
    input('\npress enter to continue...\n')
    img.close()

if __name__ == "__main__":
    openSave()
    quantize()
    convertRGB()
    convertL()
    convertP()
    crop()
    flip()
    rotate(45)
    copyPaste()
    histogramRGB()
