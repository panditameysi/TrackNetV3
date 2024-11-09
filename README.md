### Step 1: Set Up Python Conda Environment

### Step 2: Prepare and Download Testing Data from Google Drive for Testing or Original Raw Data Zip from S3

Preapare Zip File of Raw Data Folders : video and csv

After Unzipping file.zip we will get video and csv folders

Run the following command to download the sample data file:

```bash
python download_file.py --file_id 1U3qVaP6s9WqnfTqqdVtNz19kmu0ErfYq
```
```bash
s3 cp ./ ./
```
### Step 3: Unzip the Downloaded Data

Unzip the `sample_data_10.zip`(file_name.zip) file:

```bash
unzip sample_data_10.zip
```

### Step 4: Prepare the Dataset

Run the dataset preparation script:

```bash
python prepare_dataset.py
```

### Step 5: Train the Model

Train the model using the following command:

```bash
python train_mgpu.py --num_frame 3 --epochs 30 --batch_size 4 --learning_rate 0.001 --save_dir exp
```
