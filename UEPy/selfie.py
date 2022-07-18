import re
import cv2
import mediapipe as mp
import numpy as np
import urllib

import unreal

target_url = "https://www.google.com"
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def can_url(url):
    print('start can_url')
    try:
        res = urllib.request.urlopen(url)
        print("connected " + url)
        selfie.target_url = url
        unreal.CppLib.set_url(True)
    except urllib.error.URLError:
        print("Check your URL")
        selfie.target_url = "https://www.google.com"
        unreal.CppLib.set_url(False)
        return None


def selfie():

    # directory
    project_path = unreal.Paths.project_dir()
    texture_path = project_path + 'Content/Textures/SelfieTextures/'

    if not unreal.DirectoryPath(texture_path):
        print('you should crate: {}'.format(project_path))

    if not unreal.DirectoryPath(texture_path+'Test.uasset'):
        print('you should crate: {}'.format(project_path+'Test.uasset'))

    # Webcam input:
    if re.match(regex, target_url) is None:
        print("Check url")
        return

    # selfie_segmentation
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    with mp_selfie_segmentation.SelfieSegmentation(
        model_selection=1) as selfie_segmentation:
            res = urllib.request.urlopen(selfie.target_url)
            img_np = np.array(bytearray(res.read()), dtype=np.uint8)
            img_origin = cv2.imdecode(img_np, -1)

            # Flip the image horizontally for a later selfie-view display, and convert the BGR image to RGB.
            image_cv = cv2.cvtColor(cv2.flip(img_origin, 1), cv2.COLOR_BGR2RGB)

            # To improve performance, optionally mark the image as not writeable to pass by reference.
            image_cv.flags.writeable = False
            result = selfie_segmentation.process(image_cv)
            image_cv.flags.writeable = True

            image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)

            # blur masking
            binary_mask = result.segmentation_mask > 0.9
            binary_mask3 = np.dstack((binary_mask, binary_mask, binary_mask))
            img_selfie = np.where(binary_mask3, image_cv, 255)
            blured_img = cv2.GaussianBlur(img_selfie, (21, 21), 0)
            blurred_mask = np.zeros(img_selfie.shape, np.uint8)

            # draw masking area
            gray = cv2.cvtColor(img_selfie, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 168, 255, cv2.THRESH_BINARY)[1]
            contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(blurred_mask, contours, -1, (255, 255, 255), 20)

            # output
            img_output = np.where(blurred_mask == np.array([255, 255, 255]), blured_img, img_selfie)
            # cv2.imshow('IPWebCam2', img_output)
            cv2.imwrite(texture_path + 'selfie_sample.jpg', img_output)

            # unreal
            texture_task = build_import_task(texture_path + 'selfie_sample.jpg', '/Game/Textures')
            execute_import_tasks([texture_task])



def build_import_task(filename, destination_path):
    task = unreal.AssetImportTask()

    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', 'Test')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', False)
    return task


def execute_import_tasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    print('imported Task(s)')