import easyocr
import matplotlib.pyplot as plt

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify languages ('en' for English)
print("Model Loaded..")

# Load the image
image_path = 'img_to_text.jpeg'  # Replace 'image.jpg' with your image file path
#image = easyocr.imload(image_path)

# Perform text detection and recognition
result = reader.readtext(image_path)

print('Result.....!!!!')
for (bbox, text, prob) in result:
    print(f'Text: {text}, Probability: {prob}')

# Print extracted text
# for detection in result:
#     print(detection[1])  # Extracted text

# Alternatively, you can visualize the detection boxes and text on the image
# for detection in result:
#     top_left, top_right, bottom_right, bottom_left = detection[0]
#     box = [top_left, top_right, bottom_right, bottom_left, top_left]
#     x, y = zip(*box)
#     plt.plot(x, y, 'r-')
#     plt.text(x[0], y[0], detection[1], color='b')
#     plt.imshow(image)
#     plt.axis('off')
#     plt.show()