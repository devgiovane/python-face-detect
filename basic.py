from PIL import Image
#
import cnn


image = Image.open('faces/faces_only.jpg')
image, quantity = cnn.detect_face(image)

print(f"Total {quantity} faces detected")

image.show()
