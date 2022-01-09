from tkinter import *
from tkinter import filedialog
from filters import *
from Real_Time_Face_Detection import face_detection
from record_video import  record_video
from image_face_detection import image_face_detection
from PIL import ImageTk,Image

def Color_Overlay_Adjustments():
    top = Toplevel()
    top.geometry("600x300")
    top.title("Color Adjustments")
    title = Label(top, text="Adjust the colors with sliders for the "'Color Overlay Filter' " then hit the apply for the result""", fg="red")
    title.grid(row=0,column=1,columnspan=4)

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
    apply_button = Button(top, text="Apply", command=lambda :apply_color_overlay(intensity_value.get(),blue_value.get(),green_value.get(),red_value.get()))
    apply_button.grid(padx=30,pady=10,row=4,column=2)

def Select_Image_With_Path():
    filename = filedialog.askopenfilename(initialdir="C:/",title = "Select Your Image for Face Detection", filetypes=(("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    return filename


root = Tk()
root.geometry("700x250")
root.title("Face Detection and Applying Filters")

title = Label(root, text="Select the Filter that you want to apply!        (PRESS E TO EXIT SELECTED FILTER)", fg="red")
title.grid(row=0, column=0, columnspan=4)

space = Label(root, text="                  ")
space.grid(row=1, column=0)
sepia_button = Button(root, text="Sepia Filter", padx=30, pady=10, command=lambda : apply_sepia_filter(intensity=0.6))
color_overlay_button = Button(root, text="Color Overlay Filter", padx=30, pady=10,command=Color_Overlay_Adjustments)
hue_sat_button = Button(root, text="Hue Saturation Filter", padx=30, pady=10,command=apply_hue_saturation)
Threshold_button = Button(root, text="Threshold Mode", padx=30, pady=10,command=apply_threshold_mode)
Invert_button = Button(root, text="Invert Mode", padx=30, pady=10,command=apply_invert)
Blur_mask_button = Button(root, text="Circle Focus Blur Filter", padx=30, pady=10,command=lambda :apply_circle_focus_blur_filter(intensity=0.4))
Portrait_button = Button(root, text="Portrait Mode", padx=30, pady=10,command=apply_portrait_mode)
Face_detection_Button = Button(root, text="Real Time Face Detection",padx=30 , pady=10,command=face_detection)
Record_video_button = Button(root, text="Record Video",padx=20 , pady=10,command=record_video )
Image_face_Detection_button = Button(root, text="Image Face Detection",padx=30 , pady=10,command=lambda :image_face_detection(Select_Image_With_Path()))


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
root.mainloop()





