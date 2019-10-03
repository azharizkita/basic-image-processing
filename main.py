from PIL import Image
import os

__dir__ = os.path.dirname(__file__)
print('\nProject directoy: '+__dir__)



# plt.imshow(img)
# plt.axis('off')
# plt.tight_layout()
# plt.savefig(__dir__+'/result')
# plt.show()


print('\n1. OPENING AND SAVING AN IMAGE')
print('\nOpening image...')
img = Image.open(__dir__+"/images/fish.jpg")
imageName = 'normal'
imageFormat = 'png'
print('\nSaving as: '+imageName+'.'+imageFormat)
img.save(__dir__+'/'+imageName+'.'+imageFormat)
print('Showing image...')
img.show()
input('\npress enter to continue...\n')
img.close()


print('\n2. Quantize, Dithering, Sampling')
img = Image.open(__dir__+"/images/fish.jpg")
print('\nOpening image...')
imageName = 'quantize'
imageFormat = 'png'
print('\nQuantizing...')
img = img.quantize(16)
print('\nSaving as: '+imageName+'.'+imageFormat)
img.save(__dir__+'/'+imageName+'.'+imageFormat)
print('Showing image...')
img.show()
input('\npress enter to continue...\n')
img.close()