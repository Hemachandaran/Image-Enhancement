# image_processing.py

import numpy as np
import cv2

def histogram_equalization(image):
    """Apply histogram equalization to the Y channel of an image."""
    yuv_image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
    yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])
    return cv2.cvtColor(yuv_image, cv2.COLOR_YUV2RGB)

def contrast_stretching(image, lower_percentile=2, upper_percentile=98):
    """Apply contrast stretching to each channel of an image."""
    channels = cv2.split(image)
    stretched_channels = []
    for channel in channels:
        p2, p98 = np.percentile(channel, (lower_percentile, upper_percentile))
        stretched_channel = cv2.normalize(channel, None, p2, p98, cv2.NORM_MINMAX)
        stretched_channels.append(stretched_channel)
    return cv2.merge(stretched_channels)

def noise_reduction(image, kernel_size=5):
    """Reduce noise in an image using Gaussian Blur."""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def edge_detection(image):
    """Apply Canny edge detection."""
    return cv2.Canny(image, 100, 200)

def morphological_operations(image):
    """Apply morphological operations to reduce noise and enhance features."""
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

def grabcut_segmentation(image):
    """Segment the image using GrabCut algorithm."""
    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    rect = (10, 10, image.shape[1]-10, image.shape[0]-10)
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    return image * mask2[:, :, np.newaxis]

def detect_faces(image):
    """Detect faces in the image using Haar Cascades."""
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return image

def blend_images(image1, image2, alpha=0.5):
    """Blend two images together."""
    return cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)

def denoise_image(image):
    """Denoise the image using Non-Local Means Denoising."""
    return cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

def convert_color_space(image):
    """Convert the image from RGB to HSV color space."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
