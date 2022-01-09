import cv2
import os


####### This function is used for resizing watermark images. Not for any type of image filtering.
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]
    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image
    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)
    # return the resized image
    return resized


###### This class is created for recording videos. It has video output attributes to create and save the out file in an entered path(import os).
class CFEVideoConfiguration(object):
    # Standard Video Dimensions Sizes
    ###### This dictionary file contains some resolutions as keys and width, height values in tuples accordingly.
    STD_DIMENSIONS =  {
        "360p": (480, 360),
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    # Video Encoding, might require additional installs
    ###### These are 2 different video file types and the video codec(XVID). XVID video codec works well with windows and with the file types .avi and .mp4.
    VIDEO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        #'mp4': cv2.VideoWriter_fourcc(*'H264'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    width           = 640
    height          = 480
    dims            = (640, 480)
    capture         = None
    video_type      = None
    ###### We want to set the res to 480p as default
    def _init_(self, capture, filepath, res="480p", *args, **kwargs):
        self.capture = capture
        self.filepath = filepath
        ###### Here, get_dims() function will take the value that has entered optionally when the class instance created in the filters.py file.
        self.width, self.height = self.get_dims(res=res)
        self.video_type = self.get_video_type()

    # Set resolution for the video capture
    ###### As default, we can set the witdh using index 3, and set the height using index 4, using VideoCaptureObject.set() method.
    def change_res(self, width, height):
        self.capture.set(3, width)
        self.capture.set(4, height)

    ###### This function returns the width and height.
    ###### When called; if the entered parameter value for res is in the dictionary attribute of this class called STD_DIMENSIONS, sets the width and heigth instance attributes as in the dictionary file.
    ###### With the new dimensions, calls the change_res and changes the sizes of the capture object.
    ###### Then sets the dim instance attribute as the new width,height tuple.
    def get_dims(self, res='480p'):
        width, height = self.STD_DIMENSIONS['480p']
        if res in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[res]
        self.change_res(width, height)
        self.dims = (width, height)
        return width, height

    ###### This function is used for finding the video extention name from the given filename and returns it for video recording purposes only.
    ###### If the extention name isn't in the VIDEO_TYPE dictionary, .avi is set as default.
    def get_video_type(self):
        filename, ext = os.path.splitext(self.filepath)
        if ext in self.VIDEO_TYPE:
          return  self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']