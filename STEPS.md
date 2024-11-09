### Step 1: Set Up Python Conda Environment

### Step 2: Download Data from Google Drive for Testing

Run the following command to download the sample data file:

```bash
python download_file.py --file_id 1U3qVaP6s9WqnfTqqdVtNz19kmu0ErfYq
```

### Step 3: Unzip the Downloaded Data

Unzip the `sample_data_10.zip` file:

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
