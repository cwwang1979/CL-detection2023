# Annotations for the [CL-Detection 2023 Challenge](https://cl-detection2023.grand-challenge.org/): Training Dataset

### Imaging Dataset
To download the associated imaging data, visit: [zenodo link](https://zenodo.org/deposit/7787671#).
Note, the **Dataset** of the [CL-Detection 2023 Challenge](https://cl-detection2023.grand-challenge.org/) includes 600 X-ray images (400 for training, 50 for validation, 150 for testing) from 3 medical centers. X-ray images were acquired from systems of different vendors such as Sordex CRANEXr Excel Ceph, Sordex Cranex D Ceph and Planmeca ProMax. 

CL-Detection 2023 Challenge utilized the ITK (.mha) format of stack image as training. The 3D image is a cube where:
- x is the maximum width of all the contained images
- y is the maximum height of all the contained images
- z indicates which image it actually pertains

### An overview of the structure training dataset

```bash
TRAIN_DATA_DIRECTORY/
	├── images #Download from zenodo
    		├── train-stack.mha
	└── labels #Download from https://github.com/cwwang1979/CL-detection2023
		└── train-gt.json
    		
```

We provide you with a training set of pre-processing code to convert stack images to individual images, remove zero padding from individual images, and save them in your local directory as below tree directory structure. Please kindly check the code as follows [pre_processing_train_stack.py](pre_processing_train_stack.py).


```bash
PRE_PROCESS_TRAIN_SET/
	├── pre_processing_train_stack.py #Pre-process code 
	├── train-stack.mha #Training stacked images from zenodo
	├── unprocessed_images #Individual images with zero padding
		├── 0.bmp 
		.
		.
		.
		└── 399.bmp
    
	├── processed_images #Processed images without zero padding
		├── 0.bmp 
		.
		.
		.
		└── 399.bmp
    		
```


Or you can access the image from stack directly utilizing [SimpleITK](https://simpleitk.readthedocs.io/en/master/) as follows. (according to the grand-challenge.org support participant to follow the container for algorithm as provided by [evalutils]([https://cl-detection2023.grand-challenge.org/](https://comic.github.io/evalutils/))) 


```bash
import SimpleITK as sitk

pth='./'train_stack.mha'
stacked_img = sitk.ReadImage(pth)

#access the first image
img_id=1

one=stacked_img[:,:,imgid-1]

```

```bash
import SimpleITK as sitk

pth='./'train_stack.mha'
stacked_img = sitk.ReadImage(pth)

#access with numpy 
image_data = SimpleITK.GetArrayFromImage(stacked_img)

# Load individual image from image stack
img_id=1
image = np.array(image_data[img_id,:,:,:])
```


Json file groundtruth format. Dictionary "point" consist of [x,y,z], whereas x is x-coordinate of annotation, y is y-coordinate of annotation, and z indicates the image id or order (start from 1). While dictionary "point" is the constant to convert the image into the physical domain in mm, for example, if a reference landmark point has "scale" = 0.1, it shows each pixel equal to 0.1 mm.  

```bash
{
    "name": "Orthodontic landmarks",
    "type": "Multiple points",
    "points": [
        {
            "name": 1,
            "point": [
                835,
                996,
                1
            ],
            "scale": "0.1"
        },
        {
            "name": 2,
            "point": [
                1473,
                1029,
                1
            ],
            "scale": "0.1"
        },
	
.
.
.
        {
            "name": 38,
            "point": [
                1991,
                1498,
                400
            ],
            "scale": "0.096"
        }
    ]
}
```

### Reference
If you are using this dataset or some part of it, please cite the following article:
1. A joint challenge paper for 2023 challenge, which will be submitted after the MICCAI 2023 challenge.

2. Wang C* et al. (2016) A benchmark for comparison of dental radiography analysis algorithms, Medical Image Analysis 31, 63-76 (IF=13.828, 2/113 COMPUTER SCIENCE, INTER. APPLICATIONS)

3. Wang* et al.(2015) Evaluation and Comparison of Anatomical Landmark Detection Methods for Cephalometric X-Ray Images: A Grand Challenge, IEEE Transactions on Medical Imaging 34(9) 1-11 (IF=11.037, 5/136 RADIOLOGY, NUCLEAR MEDICINE & MEDICAL IMAGING) 


### License
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

### Contact Information
- Prof. Ching-Wei Wang : cweiwang@mail.ntust.edu.tw ; cwwang1979@gmail.com
- Mr. Hikam Muzakky : m11123801@mail.ntust.edu.tw
