# Annotations for the [CL-Detection 2023 Challenge](https://cl-detection2023.grand-challenge.org/): Training Dataset

### Imaging Dataset
To download the associated imaging data, visit: [zenodo link](https://zenodo.org/deposit/7787671#).
Note, the **Dataset** of the [CL-Detection 2023 Challenge](https://cl-detection2023.grand-challenge.org/) includes 600 X-ray images (400 for trianing, 50 for validation, 150 for testing) from 3 medical centers. X-ray images were acquired from systems of different vendors such as Sordex CRANEXr Excel Ceph, Sordex Cranex D Ceph and Planmeca ProMax. 

### An overview of the structure training dataset

```bash
TRAIN_DATA_DIRECTORY/
	├── images
    		├── train-stack.mha
	├── labels
		├── train-gt.json
    		└── individual image label.zip
	
```

To open the image from stack you can utilize [SimpleITK](https://simpleitk.readthedocs.io/en/master/) as follows. (according to the grand-challenge.org support participant to follow the container for algorithm as provided by [evalutils]([https://cl-detection2023.grand-challenge.org/](https://comic.github.io/evalutils/))) 


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


Json file groundtruth

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
