# Cat vs Dog Image Classifier

A CNN-based binary image classifier that distinguishes between cat and dog images.

## Dataset

**Source:** [Cat and Dog Dataset - Kaggle](https://www.kaggle.com/datasets/tongpython/cat-and-dog)

Download and extract the dataset. Expected structure:
```
dataset/
├── training_set/
│   ├── cats/
│   └── dogs/
└── test_set/
    ├── cats/
    └── dogs/
```


## Model Architecture

- 3 Convolutional blocks (32, 64, 128 filters)
- BatchNormalization and Dropout for regularization
- 2 Dense layers 128, 62 units)
- Binary classification output (sigmoid)

## Usage

### Training
Run the notebook cells in order:
1. Load and preprocess data (256x256 images)
2. Build the model
3. Train with callbacks (EarlyStopping, ReduceLROnPlateau)


## Results

- Validation Accuracy: ~70%
- Training and validation losses converge together (good generalization)

## Files

- `notebook.ipynb` - Main training and evaluation code
- Model uses image size: 256x256x3
- Batch size: 32