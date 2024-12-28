# Image Processing App

![image](https://github.com/user-attachments/assets/98318c8c-6766-4932-b2f5-0f6b0f562524)

## Description

**Image Enhancer Pro** is an advanced image processing web application built with Streamlit. It allows users to upload images and apply various enhancement techniques to improve their visual quality. The app provides an intuitive interface for real-time image processing, making it accessible for both beginners and advanced users.

## Features

- **Image Uploading**: Easily upload images from your local device.
- **Histogram Equalization**: Enhance image contrast by adjusting intensity distribution.
- **Contrast Stretching**: Adjust contrast based on specified percentile values.
- **Noise **: noise using Gaussian Blur techniques.
- **Edge Detection**: Highlight edges within the image using Canny edge detection.
- **Morphological Operations**: Enhance features with morphological transformations.
- **GrabCut Segmentation**: Isolate specific regions or objects in the image.
- **Face Detection**: Identify and mark faces within uploaded images.
- **Image Blending**: Combine two images for creative effects.
- **Color Space Conversion**: Convert between different color spaces (e.g., RGB to HSV).

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```
   github.com/Hemachandaran/Image-Enhancement.git
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`.

## Usage

1. Upload an image using the file uploader.
2. Select the desired enhancement options from the sidebar.
3. Adjust parameters using sliders for real-time feedback.

## Example Outputs

Below are some example outputs of the application:

### Original Image

![image](https://github.com/user-attachments/assets/34dfa0bc-27ec-4008-a31f-880bdba096ae)


### Enhanced Image
1. Histogram Equalization AND Contrast Stretching : ![image](https://github.com/user-attachments/assets/7150020b-7b2b-4ca9-8dd5-e7a9f52c43ea)
2. Edge Detection : ![image](https://github.com/user-attachments/assets/f28cef8e-8f49-4426-ae80-fa8c63d27a2d)
3. Noice and Face Detection ![image](https://github.com/user-attachments/assets/0535ae7d-6f91-45d1-a770-4d184023b6dc)
4. Morphological Operations : ![image](https://github.com/user-attachments/assets/e27f2d28-61c9-4beb-aa18-6499a2995fd6)
5. GrabCut Segmentation : ![image](https://github.com/user-attachments/assets/a7e9e478-2968-417d-93c0-b50caa7db808)
6. Face Detection : ![image](https://github.com/user-attachments/assets/d07b2ccf-7474-43f9-9faa-a2e76c41d0c1)
7. Image Blending : ![image](https://github.com/user-attachments/assets/ac48eac3-c44c-4fd2-a1ea-220b86c762f0)
8. Color Space Conversion : ![image](https://github.com/user-attachments/assets/30f4d3fe-1ddb-47e4-8298-101d1827d9cf)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - For providing an easy-to-use framework for building web applications.
- [OpenCV](https://opencv.org/) - For powerful image processing capabilities.

