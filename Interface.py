from tkinter import *
from tkinter import filedialog

from Image_Enhancement import Manual_Image_Enhancement
from Real_Time_Face_Detection import face_detection
from Real_Time_Video_Enhancer import Manual_Real_Time_Video_Enhancement
from auto import automatic_brightness_and_contrast
from filters import *
from image_face_detection import image_face_detection
from record_video import record_video


## LICENSED and Made By Arda Dumanoglu ----> This project is made for GRADUATION PROJECT I
     ## ALL RIGHTS RESERVED
     ## PLEASE RUN THAT FILE.

def Color_Overlay_Adjustments():
    top = Toplevel()
    top.geometry("600x300")
    top.title("Color Adjustments")
    title1 = Label(top, text="Adjust the colors with sliders for the "'Color Overlay Filter' " then hit the apply for the result""", fg="red")
    title1.grid(row=0, column=1, columnspan=4)

    red_value = IntVar()
    intensity_value = DoubleVar()
    green_value = IntVar()
    blue_value = IntVar()

    intensity = Scale(top, from_=0, to=1,resolution=0.1,orient=HORIZONTAL,variable=intensity_value).grid(row=2,column=1)
    red = Scale(top, from_=0, to=255,orient=HORIZONTAL,variable=red_value).grid(row=2,column=2)
    green = Scale(top, from_=0, to=255,orient=HORIZONTAL,variable=green_value).grid(row=2,column=3)
    blue = Scale(top, from_=0, to=255,orient=HORIZONTAL,variable=blue_value).grid(row=2,column=4)

    intensity_text= Label(top,text="Intensity").grid(row=1,column=1)
    red_text= Label(top,text="Red").grid(row=1,column=2)
    green_text= Label(top,text="Green").grid(row=1,column=3)
    blue_text= Label(top,text="Blue").grid(row=1,column=4)

    empty_space = Label(top, text="                  ").grid(row=3,column=2)
    apply_button = Button(top, text="Apply", command=lambda: apply_color_overlay(intensity_value.get(),blue_value.get(),green_value.get(),red_value.get()))
    apply_button.grid(padx=30,pady=10,row=4,column=2)

def Manual_Image_Editor():
    image_path = Select_File_With_Path()
    if image_path == "":
        return
    roof = Toplevel()
    roof.geometry("630x200")
    roof.title("Manual_Image_Editor")
    title2 = Label(roof, text="Edit  the selected image with sliders then hit  apply for the result (1  represents original value).", fg="red")
    title2.grid(row=0,column=1,columnspan=5)

    Brightness_value = DoubleVar()
    Brightness_value.set(1)            # We don't want to set default value as 0.0 . So we set as 1 which represented  original image.
    Color_Saturation_Value = DoubleVar()
    Color_Saturation_Value.set(1)
    Sharpness_value = DoubleVar()
    Sharpness_value.set(1)
    Contrast_value = DoubleVar()
    Contrast_value.set(1)

    Color_Saturation = Scale(roof, from_=-10, to=10,resolution=0.1,orient=HORIZONTAL,variable=Color_Saturation_Value).grid(row=2,column=1)
    Brightness = Scale(roof, from_=-10, to=10,resolution=0.1,orient=HORIZONTAL,variable=Brightness_value).grid(row=2,column=2)
    Sharpness = Scale(roof, from_=-10, to=10,resolution=0.1,orient=HORIZONTAL,variable=Sharpness_value).grid(row=2,column=3)
    Contrast = Scale(roof, from_=-10, to=10,resolution=0.1,orient=HORIZONTAL,variable=Contrast_value).grid(row=2,column=4)

    Color_Saturation_text= Label(roof,text="Color Saturation").grid(row=1,column=1)
    Brigtness_text= Label(roof,text="Brightness").grid(row=1,column=2)
    Sharpness_text= Label(roof,text="Sharpness").grid(row=1,column=3)
    Contrast_text= Label(roof,text="Contrast").grid(row=1,column=4)

    empty_space = Label(roof, text="                  ").grid(row=3,column=2)
    apply_button = Button(roof, text="Apply", command=lambda: Manual_Image_Enhancement(image_path,Color_Saturation_Value.get(),Contrast_value.get(),Sharpness_value.get(),Brightness_value.get()))
    apply_button.grid(padx=30,pady=10,row=4,column=2)

    tip = Label(roof, text="If you want to save the edited image\npress 'CTRL+S' when it appears.",fg="red")
    tip.grid(row=4,column=5)

def Manual_Real_Time_Video_Enhancer():
    level = Toplevel()
    level.geometry("630x200")
    level.title("Manual_Real_Time_Video_Editor")
    title3 = Label(level, text="Enhance the Real-Time Video with sliders then hit  apply for the result (1  represents original value).", fg="red")
    title3.grid(row=0,column=1,columnspan=5)

    brightness_value = DoubleVar()
    brightness_value.set(1)            # We don't want to set default value as 0.0 . So we set as 1 which represented  original image.
    color_Saturation_Value = DoubleVar()
    color_Saturation_Value.set(50)
    sharpness_value = DoubleVar()
    sharpness_value.set(1)
    contrast_value = DoubleVar()
    contrast_value.set(1)
    zoom_value = DoubleVar()
    zoom_value.set(1)

    color_saturation = Scale(level, from_=0, to=100,resolution=0.1,orient=HORIZONTAL,variable=color_Saturation_Value).grid(row=2,column=1)
    brightness = Scale(level, from_=0, to=100,resolution=0.1,orient=HORIZONTAL,variable=brightness_value).grid(row=2,column=2)
    sharpness = Scale(level, from_=0, to=100,resolution=0.1,orient=HORIZONTAL,variable=sharpness_value).grid(row=2,column=3)
    contrast = Scale(level, from_= 0, to=100,resolution=0.1,orient=HORIZONTAL,variable=contrast_value).grid(row=2,column=4)
    zoom = Scale(level, from_=0, to=100,resolution=0.1,orient=HORIZONTAL,variable=zoom_value).grid(row=2,column=5)

    color_saturation_text= Label(level,text="Color Saturation").grid(row=1,column=1)
    brigtness_text= Label(level,text="Brightness").grid(row=1,column=2)
    sharpness_text= Label(level,text="Sharpness").grid(row=1,column=3)
    contrast_text= Label(level,text="Contrast").grid(row=1,column=4)
    zoom_text = Label(level,text="Zoom").grid(row=1,column=5)

    Empty_space = Label(level, text="                  ").grid(row=3,column=2)
    apply_button = Button(level, text="Apply", command=lambda: Manual_Real_Time_Video_Enhancement(brightness_value.get(),contrast_value.get(),color_Saturation_Value.get(),zoom_value.get(),sharpness_value.get()))
    apply_button.grid(padx=30,pady=10,row=4,column=2)


def Select_File_With_Path():
    filename = filedialog.askopenfilename(initialdir="C:/",title = "Choose Your Image to Use", filetypes=(("all files","*.*"),("jpeg files","*.jpg"),("png files","*.png")))
    return filename

def Select_Directory_Folder():
    folder_path = filedialog.askdirectory()
    return folder_path

root = Tk()
root.geometry("820x310")
root.title("Face Detection and Applying Filters")

title = Label(root, text="Select the Filter that you want to apply!        (PRESS E TO EXIT SELECTED FILTER)", fg="red")
title.grid(row=0, column=0, columnspan=4)

space = Label(root, text="                  ")
space.grid(row=1, column=0)
sepia_button = Button(root, text="Sepia Filter", padx=30, pady=10, command=lambda: apply_sepia_filter(intensity=0.6))
color_overlay_button = Button(root, text="Color Overlay Filter", padx=30, pady=10,command=Color_Overlay_Adjustments)
hue_sat_button = Button(root, text="Hue Saturation Filter", padx=30, pady=10,command=apply_hue_saturation)
Threshold_button = Button(root, text="Threshold Mode", padx=30, pady=10,command=apply_threshold_mode)
Invert_button = Button(root, text="Invert Mode", padx=30, pady=10,command=apply_invert)
Blur_mask_button = Button(root, text="Circle Focus Blur Filter", padx=30, pady=10,command=lambda: apply_circle_focus_blur_filter(intensity=0.4))
Portrait_button = Button(root, text="Portrait Mode", padx=30, pady=10,command=apply_portrait_mode)
Face_detection_Button = Button(root, text="Real-Time Face Detection",padx=30 , pady=10,command=face_detection)
Record_video_button = Button(root, text="Record Video", padx=20, pady=10, command=lambda: record_video(Select_Directory_Folder()))
Image_face_Detection_button = Button(root, text="Image Face Detection", padx=30, pady=10, command=lambda: image_face_detection(Select_File_With_Path()))
Brightness_Contrast_Enhancer_Button = Button(root, text="Auto Brightness-Contrast Enhancer", padx=30, pady=10, command=lambda: automatic_brightness_and_contrast())
Manual_Image_Enhancement_Button = Button(root, text="Manual Image Enhancer", padx=30, pady=10, command=lambda: Manual_Image_Editor())
Manual_Real_Time_Enhancer_Button = Button(root, text="Manual Real-Time\n Video Enhancer", padx=30, pady=10, command=lambda: Manual_Real_Time_Video_Enhancer())

sepia_button.grid(row=2, column=0)
color_overlay_button.grid(row=2, column=1)
hue_sat_button.grid(row=2, column=2)
Portrait_button.grid(row=2, column=3)


space_2 = Label(root, text="                  ")
space_2.grid(row=3, column=0)

Invert_button.grid(row=4, column=0)
Threshold_button.grid(row=4, column=1)
Blur_mask_button.grid(row=4, column=2)
Face_detection_Button.grid(row=4 , column=3)


space_3 = Label(root, text="                  ")
space_3.grid(row=5, column=0)

Record_video_button.grid(row=6, column=0)
Image_face_Detection_button.grid(row=6,column=1)
Brightness_Contrast_Enhancer_Button.grid(row=6, column=2)
Manual_Image_Enhancement_Button.grid(row=6,column=3)

space_4 = Label(root, text="                  ")
space_4.grid(row=7, column=0)

Manual_Real_Time_Enhancer_Button.grid(row=8,column=0)
root.mainloop()





