import cv2
import pandas as pd
import numpy as np
from google.colab import drive
from google.colab.patches import cv2_imshow

# Mount Google Drive
drive.mount('##\\ur drive link##\\') #<-- Updated this path

# Update the image path to the correct location on the new PC
img_path = r'/##\\drive link of the image\\##'  # <-- Update this path if needed
img = cv2.imread(img_path)

# Declare global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading CSV file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv_path = r'##\\drive link for csv file##\\'  # <-- Updated this path
csv = pd.read_csv(csv_path, names=index, header=None)

# Function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    cname = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2_imshow(img)  # Display image in Colab
    if clicked:
        # cv2.rectangle(image, start point, endpoint, color, thickness) -1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display(Color name and RGB values)
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img, text, start, font(0-7), fontScale, color, thickness, lineType)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
