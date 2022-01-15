import cv2
import numpy as np


def verify_alpha_channel(frame):
    try:
        frame.shape[3]  # looking for the alpha channel which is 4th position is available or not
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # Changing RGB color to  RGB-Alpha channel
    return frame


def apply_hue_saturation():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        s.fill(199)
        v.fill(255)
        hsv_image = cv2.merge([h, s, v])
        out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        frame = verify_alpha_channel(frame)
        out = verify_alpha_channel(out)
        cv2.addWeighted(out, 0.25, frame, 1.0, .23, frame)
        cv2.imshow('Hue Saturation', frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):  # waiting 10 ms delay when we press e to exit the code
            break
    capture.release()
    cv2.destroyAllWindows()


def apply_color_overlay(intensity=0.5, blue=0, green=0,
                        red=0):  # we change the RGB colours as individual to change frame color intensity and it is default as 0 if we didn't change them when we call it.
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        frame = verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        sepia_bgra = (blue, green, red, 1)
        overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
        cv2.addWeighted(overlay, intensity, frame, 1.0, 0,
                        frame)  # last parameter is destination source name which is same as the frame we put it before
        cv2.imshow('Color Overlay', frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):  # waiting 10 ms delay when we press e to exit the code
            break
    capture.release()
    cv2.destroyAllWindows()


def apply_sepia_filter(intensity=0.6):
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        frame = verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        sepia_bgra = (30, 64, 108, 1)  # blue-green-red-alpha values (we can change and see the colors to make decision)
        overlay = np.full((frame_h, frame_w, 4), sepia_bgra,
                          dtype='uint8')  # it makes full sepia color entire frame so we make it full instead of zeros which is everything identical to frame not sepia.
        # we want everything to be identical  to the sepia color so we make it full instead of zeros.   We don't make it np.zeros because it makes everything to identical to frame
        cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
        cv2.imshow('sepia', frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):  # waiting 10 ms delay when we press e to exit the code
            break
    capture.release()
    cv2.destroyAllWindows()


def alpha_blend(frame_1, frame_2, mask):
    alpha = mask / 255.0
    blended = cv2.convertScaleAbs(frame_1 * (1 - alpha) + frame_2 * alpha)
    return blended


def apply_circle_focus_blur_filter(intensity=0.2):  # FIRST WE MAKE A BLURRED FRAME THEN WE MASK CENTER OF THE FRAME THEN WE BLEND IT SO THE CENTER PART IS BLURRED.
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        frame = verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape  # frame height-frame width-frame channel
        y = int(frame_h / 2)
        x = int(frame_w / 2)
        mask = np.zeros((frame_h, frame_w, 4),
                        dtype='uint8')  # we didn't put any color because we make it zeros not full.
        cv2.circle(mask, (x, y), int(y / 2), (255, 255, 255), -1,
                   cv2.LINE_AA)  # (x, y) = center of the circle also called radius
        mask = cv2.GaussianBlur(mask, (21, 21), 11)
        blurred = cv2.GaussianBlur(frame, (21, 21), 11)
        blended = alpha_blend(frame, blurred, 255 - mask)
        frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)  # returning alpha channel to normal RGB channel as original
        cv2.imshow('Circle Focus Blur Filter', frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):  # waiting 10 ms delay when we press e to exit the code
            break
    capture.release()
    cv2.destroyAllWindows()


def apply_portrait_mode():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
        blurred = cv2.GaussianBlur(frame, (21, 21), 11)
        blended = alpha_blend(frame, blurred, mask)
        frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
        cv2.imshow('Portrait Mode', frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):  # waiting 10 ms delay when we press e to exit the code
            break
    capture.release()
    cv2.destroyAllWindows()


def apply_threshold_mode():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 83, 255, cv2.THRESH_BINARY)
        cv2.imshow('Threshold', mask)
        if cv2.waitKey(10) & 0xFF == ord('e'):  # waiting 10 ms delay when we press e to exit the code
            break
    capture.release()
    cv2.destroyAllWindows()


def apply_invert():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        cv2.imshow('Invert Filter', cv2.bitwise_not(frame))
        if cv2.waitKey(10) & 0xFF == ord('e'):  # waiting 10 ms delay when we press e to exit the code
            break
    capture.release()
    cv2.destroyAllWindows()
