"""
Escrito por Jesús Omar Cuenca Espino 
A01378844@itesm.mx

25/03/2021
"""

import cv2
from math import copysign, log10

def rotate180(img):
    """
    Returns a copy of the img rotated 180 degrees

    Args:
        img (cv2.Matrix): The image to be rotated

    Returns:
        cv2.Matrix: The image Rotated 180 degrees
    """
    return cv2.rotate(img, cv2.ROTATE_180)

def mirror(img):
    """
    Returns a copy of the img rotated 180 degrees

    Args:
        img (cv2.Matrix): The image to be rotated

    Returns:
        cv2.Matrix: The image Rotated 180 degrees
    """
    return cv2.flip(img, 1)

def toGrey(img):
    """
    Returns a GreyScale Version of the image.

    Args:
        img (cv2.Matrix): Image to be converted to GreyScale.

    Returns:
        cv2.Matrix: The image turned into GreyScale
    """
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def resize(img,width : int,height : int,inter = cv2.INTER_AREA):
    """
    Resizes the Images to the apropiate values if possible.

    Args:

        img (cv2.Matrix): The image to be edited.
        width (int): The target width of the resulting image.
        height (int): The target height of the resulting image.
        inter (cv2.InterpolationEnum, optional): Type of Interpolation for CV to use, cv2.INTER_AREA | cv2.INTER_CUBIC | cv2.INTER_LINEAR. Defaults to cv2.INTER_AREA.

    Returns:
        cv2.Matrix: Returns the image with the size altered to [width] and [height]
    """
    return cv2.resize(img, (width,height), interpolation = inter)

def calculateHuMoments(fName : str):
    img = cv2.imread(fName,cv2.IMREAD_GRAYSCALE)
    _,img = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
    huMoments = cv2.HuMoments(cv2.moments(img))
    for i in range(0,7):
        moment = -1 * copysign(1.0, huMoments[i]) * log10(abs(huMoments[i]))
        print(f"Hu Moment {i} = {moment}")



if __name__ == "__main__":
    img = cv2.imread("image_A.jpg")
    cv2.imwrite('rotate.jpg', rotate180(img))
    cv2.imwrite('mirror.jpg', mirror(img))
    img = cv2.imread("image_B.jpg")
    cv2.imwrite('resize.jpg', toGrey(resize(img,300,200)))
    imgs = ("image_A.jpg","rotate.jpg","mirror.jpg","image_B.jpg","resize.jpg")
    LINES = "---------------------"
    for i in imgs:
        print(LINES + " " + i + " " + LINES)
        print()
        calculateHuMoments(i)
        print()