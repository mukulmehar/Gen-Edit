# Gen-Edit: Edit Images using Text Prompt

This tool can be used for text-guided image editing. It uses Segment Anything Model (SAM) to predict masks of specified oject in an image.
Currently, it supports background extraction and image filling functionalities.

## Installation

This code has been tested with `python3.10.12` on an NVIDIA A6000

```
pip install -e lang-segment-anything/
python -m pip install -e Inpaint-Anything/segment_anything/
python -m pip install -r Inpaint-Anything/lama/requirements.txt
```

Download SAM and LaMa weights (<a href="https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth"> sam_vit_h_4b8939.pth</a> and <a href="https://drive.google.com/drive/folders/1B2x7eQDgecTL0oh3LSIBDGj0fTxs6Ips">big-lama</a>), and put them into `Inpaint-Anything/pretrained_models`. For simplicity, you can also go <a href="https://drive.google.com/drive/folders/1ST0aRbDRZGli0r7OVVOQvXwtadMCuWXg">here</a> to directly download the pretrained models.

## Extract Background

![sofa](https://github.com/mukulmehar/Gen-Edit/assets/54510198/1d35cfee-10f6-4088-8d49-38d8dc3cdf49)
&nbsp; &nbsp; &nbsp; &nbsp;
![sofa_bg](https://github.com/mukulmehar/Gen-Edit/assets/54510198/1e270f21-cf27-4a77-98e4-03c553c4a769)

See `background_extract.ipynb`

## Image Fill

<img title="chair" alt="A picture of chair" src="https://github.com/mukulmehar/Gen-Edit/assets/54510198/b6593807-62fb-48f3-9e49-7e64b28f4e7a" width=320 height=320>
&nbsp; &nbsp; &nbsp; &nbsp;
<img title="chair" alt="A picture of chair" src="https://github.com/mukulmehar/Gen-Edit/assets/54510198/bb468c79-b463-4ff6-9ef7-3f6eada591ca" width=320 height=320>

See `image_fill.ipynb`

## References

[1]: <a href="https://github.com/paulguerrero/lang-sam">lang-sam</a>

[2]: <a href="https://github.com/geekyutao/Inpaint-Anything">Inpaint-Anything</a>
