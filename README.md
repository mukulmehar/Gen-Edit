# Gen-Edit: Edit Images Using Text Prompt

## Installation

This code has been tested with `python3.10.12` on an NVIDIA A6000

```
pip install -e lang-segment-anything/
python -m pip install -e Inpaint-Anything/segment_anything/
python -m pip install -r Inpaint-Anything/lama/requirements.txt
```

Download SAM and LaMa weights (<a href="https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth"> sam_vit_h_4b8939.pth</a> and <a href="https://drive.google.com/drive/folders/1B2x7eQDgecTL0oh3LSIBDGj0fTxs6Ips">big-lama</a>), and put them into `Inpaint-Anything/pretrained_models`. For simplicity, you can also go <a href="https://drive.google.com/drive/folders/1ST0aRbDRZGli0r7OVVOQvXwtadMCuWXg">here</a> to directly download the pretrained models.

## References

[1]: <a href="https://github.com/paulguerrero/lang-sam">lang-sam</a>

[2]: <a href="https://github.com/geekyutao/Inpaint-Anything">Inpaint-Anything</a>