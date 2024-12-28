# app.py

import streamlit as st
import numpy as np
from PIL import Image
from image_processing import (
    histogram_equalization,
    contrast_stretching,
    noise_reduction,
    edge_detection,
    morphological_operations,
    grabcut_segmentation,
    detect_faces,
    blend_images,
    denoise_image,
    convert_color_space  # Ensure this line is included
)

# Streamlit application starts here
st.title("Advanced Image Processing App")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Load and display the original image
    image = Image.open(uploaded_file).convert('RGB')
    original_image = np.array(image)
    
    st.image(original_image, caption='Original Image', use_container_width=True)

    # Sidebar options for image processing
    st.sidebar.header("Enhancement Options")

    # Initialize the enhanced image as the original
    enhanced_image = original_image.copy()

    # Histogram Equalization
    if st.sidebar.checkbox("Histogram Equalization"):
        enhanced_image = histogram_equalization(enhanced_image)

    # Contrast Stretching with sliders for lower and upper percentiles
    lower_percentile = st.sidebar.slider("Lower Percentile for Contrast Stretching", 0.0, 100.0, 2.0)
    upper_percentile = st.sidebar.slider("Upper Percentile for Contrast Stretching", 0.0, 100.0, 98.0)
    
    if st.sidebar.checkbox("Contrast Stretching"):
        enhanced_image = contrast_stretching(enhanced_image.astype(np.uint8), int(lower_percentile), int(upper_percentile))

    # Noise Reduction with a slider for kernel size
    kernel_size = st.sidebar.slider("Kernel Size for Noise Reduction", 1, 21, 5) 
    if kernel_size % 2 == 0:
        kernel_size += 1  
        
    if st.sidebar.checkbox("Noise Reduction"):
        enhanced_image = noise_reduction(enhanced_image.astype(np.uint8), kernel_size)

    # Edge Detection
    if st.sidebar.checkbox("Edge Detection"):
        enhanced_image = edge_detection(enhanced_image.astype(np.uint8))

    # Morphological Operations
    if st.sidebar.checkbox("Morphological Operations"):
        enhanced_image = morphological_operations(enhanced_image.astype(np.uint8))

    # GrabCut Segmentation
    if st.sidebar.checkbox("GrabCut Segmentation"):
        enhanced_image = grabcut_segmentation(enhanced_image.astype(np.uint8))

    # Face Detection
    if st.sidebar.checkbox("Face Detection"):
        enhanced_image = detect_faces(enhanced_image.astype(np.uint8))

    # Blend Images (for demonstration purposes; you can upload another image to blend with)
    second_uploaded_file = st.file_uploader("Choose a second image to blend...", type=["jpg", "jpeg", "png"], key="second")
    if second_uploaded_file is not None:
        second_image = Image.open(second_uploaded_file).convert('RGB')
        second_image_array = np.array(second_image)

        if st.sidebar.checkbox("Blend Images"):
            blended_image = blend_images(enhanced_image.astype(np.uint8), second_image_array.astype(np.uint8))
            enhanced_image = blended_image

    # Denoise Image
    if st.sidebar.checkbox("Denoise Image"):
        enhanced_image = denoise_image(enhanced_image.astype(np.uint8))

    # Convert Color Space (to HSV as an example)
    if st.sidebar.checkbox("Convert Color Space to HSV"):
        enhanced_image = convert_color_space(enhanced_image.astype(np.uint8))

    # Display the final enhanced image after all selected processing steps
    st.image(enhanced_image.astype(np.uint8), caption='Enhanced Image', use_container_width=True)

    # Optionally add footer or additional information about the app here.
