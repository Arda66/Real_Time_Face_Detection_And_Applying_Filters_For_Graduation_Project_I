from PIL import Image, ImageEnhance


def Manual_Image_Enhancement(image_filepath, Color_Saturation, contrast_value, sharpness_value, brigtness_value):
    img = Image.open(image_filepath)
    color_img = ImageEnhance.Color(img)
    color_img = color_img.enhance(Color_Saturation)
    contrast_img = ImageEnhance.Contrast(color_img)
    contrast_img = contrast_img.enhance(contrast_value)
    sharpen_img = ImageEnhance.Sharpness(contrast_img)
    sharpen_img = sharpen_img.enhance(sharpness_value)
    brightness_img = ImageEnhance.Brightness(sharpen_img)
    brightness_img.enhance(brigtness_value).show("Result of the Edited Image")

