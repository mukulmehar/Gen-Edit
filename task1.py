# import sys
# print(sys.executable)
import argparse
import os
from PIL import Image
from lang_sam import LangSAM
from lang_sam.utils import draw_segmentation_masks
import torchvision.transforms as transforms

def validate_file(f):
    if not os.path.exists(f):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f

def out_file(f):
    return f

data_dir = './pose_editing_examples/'

# parse command line args
parser = argparse.ArgumentParser(description="Avataar_Task_1")
parser.add_argument('--image', '-i', dest="input_filename", type=validate_file, help='path to input image to be masked', metavar="IFILE")
parser.add_argument('--prompt', '-p', type=str, help='text-prompt for the object to be masked')
parser.add_argument('--output', '-o', dest="output_filename", type=out_file, help='path of masked image file to be generated', metavar="OFILE")

args = parser.parse_args()
# print(vars(args))

# print(args.input_filename)
# print(type(args.input_filename))

model = LangSAM()
# image_pil = Image.open(data_dir + args.image).convert("RGB")
image_pil = Image.open(args.input_filename).convert("RGB")
text_prompt = args.prompt
masks, boxes, phrases, logits = model.predict(image_pil, text_prompt)

transform = transforms.Compose([
    transforms.PILToTensor()
])

img_tensor = transform(image_pil)
mask_image = draw_segmentation_masks(img_tensor, masks, colors="red")
transform = transforms.ToPILImage()
img = transform(mask_image)
img.save(args.output_filename)