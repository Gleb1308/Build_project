import numpy as np
from helper_funcs import *


blank = np.zeros((512, 512, 3), np.uint8)
cv.imshow('Blank', blank)
# frame = frame_plot([[100, 60, 130, 130], [230, 230, 420, 450]], ['car1', 'car2'], blank)
# cv.imshow('frame', frame)
width = 250
cv.line(blank, (100, 250), (100 + width, 250), (0, 255, 0), 2)
cv.putText(blank, 'Car1', (100, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Transformed', blank)
cv.waitKey(0)
