import binary_pic_gen
import cv2
import numpy as np

pic=binary_pic_gen.gen(100,10000,10)
cv2.imshow('Pattern',pic)
cv2.waitKey()
cv2.cv2.destroyAllWindows()