import os
import argparse
from pathlib import Path
from PIL import Image
from lang_sam import LangSAM
from lang_sam.utils import draw_segmentation_masks
import torchvision.transforms as transforms
import numpy as np
import cv2

from numpy import asarray

import sys
print(sys.executable)

def validate_file(f):
    if not os.path.exists(f):
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f

def validate_dir(f):
    dir = os.path.dirname(f)
    if not os.path.exists(dir):
        raise argparse.ArgumentTypeError("{0} does not exist".format(dir))
    return f

# The standard work-around: first convert to greyscale 
def img_grey(data):
    return Image.fromarray(data * 255, mode='L').convert('L')

# parse command line args
parser = argparse.ArgumentParser(description="Avataar_Task_2")

parser.add_argument('--image', '-i', type=validate_file, help='path to input image', required=True)
parser.add_argument('--prompt', '-p', type=str, help='text-prompt for the object to be extracted', required=True)
parser.add_argument('--out', '-o', type=validate_dir, help='path to output image', required=True)

args = parser.parse_args()

# input_image_name = Path(args.image).stem
# out_image_name = Path(args.out).stem
# print(input_image_name)
# print(out_image_name)

model = LangSAM()

image_pil = Image.open(args.image).convert("RGB")
masks, boxes, phrases, logits = model.predict(image_pil, args.prompt)
binary_masked_img = img_grey(masks.squeeze().detach().cpu().numpy().astype(np.uint8))
image_pil.putalpha(binary_masked_img)
image_pil.save(args.out)