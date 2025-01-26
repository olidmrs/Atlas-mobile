import numpy as np
from PIL import Image


im = Image.open('imageprocessing/image_test/test1.png')
arr = list(im.getdata())
arr = np.array(arr)
arr = arr[:, :-1]
print(arr)

# image = np.zeros((arr.shape))

# def transform_image(image : np.ndarray) -> np.ndarray:
#     blue_lower = np.array([0, 0, 100])
#     blue_upper = np.array([100, 100, 255])
#     road_mask = np.all((image >= blue_lower) & (image <= blue_upper), axis=-1)
#     flood_filled = road_mask.astype(np.uint8)

#     y, x = np.where(flood_filled == 1)
#     start_point = (x[0], y[0])  
    
#     flood_filled = cv2.floodFill(flood_filled, None, start_point, 1)[1]
#     binary_matrix = flood_filled
#     return binary_matrix

# print(transform_image(image))