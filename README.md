# Assignment - 6
## Problem Statement
<img width="756" alt="Screenshot 2023-02-10 at 10 44 25 PM" src="https://user-images.githubusercontent.com/118976187/218154347-cd71eee5-cba1-4ef2-b7bf-49176ee8ca24.png">

## Code Details

Code is devided into six files. Five of them are py files & one ipynb file. Link for them are as below:
- [data.py](https://github.com/achalgarg14/session_6/blob/main/data.py) - For data loading and data augmentation
- [model_class.py](https://github.com/achalgarg14/session_6/blob/main/model_class.py) - Defining the model class
- [train_model.py](https://github.com/achalgarg14/session_6/blob/main/train_model.py)
- [test_model.py](https://github.com/achalgarg14/session_6/blob/main/test_model.py) - Function for testing the model
- [model_training.py](https://github.com/achalgarg14/session_6/blob/main/model_training.py) - For training the model
- [Session_6_Assignment.ipynb](https://github.com/achalgarg14/session_6/blob/main/Session_6_Assignment.ipynb)

All of these py files are imported into Session_6_Assignment.ipynb after uploading in google drive. 

## Summary of Model:
<img width="397" alt="Screenshot 2023-02-10 at 11 02 40 PM" src="https://user-images.githubusercontent.com/118976187/218157939-9f8508a0-c69d-4341-bd8e-da37f5624d9b.png">

## Performance Summary:
Best Training Accuracy: 80.26%
Best Test Accuracy: 84.70% (Epoch: 181)

##Training Log (last few steps)
```
EPOCH: 170
Loss=0.7844630479812622 Batch_id=390 Accuracy=79.89: 100%|██████████| 391/391 [00:17<00:00, 22.32it/s]
 Average Training Loss=0.006605938062667847, Accuracy=79.892


Test set: Average loss: 0.4547, Accuracy: 8449/10000 (84.49%)

EPOCH: 171
Loss=0.88832688331604 Batch_id=390 Accuracy=79.93: 100%|██████████| 391/391 [00:17<00:00, 22.43it/s]
 Average Training Loss=0.006574953840970993, Accuracy=79.93


Test set: Average loss: 0.4553, Accuracy: 8463/10000 (84.63%)

EPOCH: 172
Loss=0.9251648187637329 Batch_id=390 Accuracy=79.79: 100%|██████████| 391/391 [00:17<00:00, 22.33it/s]
 Average Training Loss=0.006619830800294876, Accuracy=79.788


Test set: Average loss: 0.4555, Accuracy: 8460/10000 (84.60%)

EPOCH: 173
Loss=0.7840496301651001 Batch_id=390 Accuracy=80.13: 100%|██████████| 391/391 [00:19<00:00, 20.02it/s]
 Average Training Loss=0.006541335673332214, Accuracy=80.13


Test set: Average loss: 0.4535, Accuracy: 8451/10000 (84.51%)

EPOCH: 174
Loss=0.842926025390625 Batch_id=390 Accuracy=79.60: 100%|██████████| 391/391 [00:17<00:00, 22.55it/s]
 Average Training Loss=0.006637060525417328, Accuracy=79.602


Test set: Average loss: 0.4548, Accuracy: 8453/10000 (84.53%)

EPOCH: 175
Loss=0.9005335569381714 Batch_id=390 Accuracy=79.74: 100%|██████████| 391/391 [00:17<00:00, 22.34it/s]

 Average Training Loss=0.006606146742105484, Accuracy=79.742

Test set: Average loss: 0.4537, Accuracy: 8456/10000 (84.56%)

EPOCH: 176
Loss=0.7939257621765137 Batch_id=390 Accuracy=80.03: 100%|██████████| 391/391 [00:18<00:00, 21.65it/s]
 Average Training Loss=0.006560333894491195, Accuracy=80.026


Test set: Average loss: 0.4522, Accuracy: 8445/10000 (84.45%)

EPOCH: 177
Loss=0.9306212067604065 Batch_id=390 Accuracy=80.04: 100%|██████████| 391/391 [00:17<00:00, 22.76it/s]
 Average Training Loss=0.006576395016908646, Accuracy=80.036


Test set: Average loss: 0.4530, Accuracy: 8458/10000 (84.58%)

EPOCH: 178
Loss=0.7930035591125488 Batch_id=390 Accuracy=79.71: 100%|██████████| 391/391 [00:17<00:00, 22.43it/s]
 Average Training Loss=0.006603272533416748, Accuracy=79.712


Test set: Average loss: 0.4550, Accuracy: 8466/10000 (84.66%)

EPOCH: 179
Loss=1.0288158655166626 Batch_id=390 Accuracy=80.02: 100%|██████████| 391/391 [00:17<00:00, 22.64it/s]
 Average Training Loss=0.006608883231878281, Accuracy=80.02


Test set: Average loss: 0.4551, Accuracy: 8463/10000 (84.63%)

EPOCH: 180
Loss=0.939805269241333 Batch_id=390 Accuracy=79.93: 100%|██████████| 391/391 [00:18<00:00, 21.70it/s]
 Average Training Loss=0.006583288416862488, Accuracy=79.932


Test set: Average loss: 0.4564, Accuracy: 8444/10000 (84.44%)

EPOCH: 181
Loss=0.7822792530059814 Batch_id=390 Accuracy=79.91: 100%|██████████| 391/391 [00:17<00:00, 22.69it/s]
 Average Training Loss=0.006592179801464081, Accuracy=79.908


Test set: Average loss: 0.4532, Accuracy: 8470/10000 (84.70%)

EPOCH: 182
Loss=0.8004782199859619 Batch_id=390 Accuracy=79.92: 100%|██████████| 391/391 [00:17<00:00, 22.37it/s]
 Average Training Loss=0.006556265882253647, Accuracy=79.918


Test set: Average loss: 0.4561, Accuracy: 8455/10000 (84.55%)

EPOCH: 183
Loss=0.8121778964996338 Batch_id=390 Accuracy=79.91: 100%|██████████| 391/391 [00:17<00:00, 22.55it/s]
 Average Training Loss=0.006593397493362426, Accuracy=79.912


Test set: Average loss: 0.4552, Accuracy: 8464/10000 (84.64%)

EPOCH: 184
Loss=0.9332171678543091 Batch_id=390 Accuracy=80.05: 100%|██████████| 391/391 [00:17<00:00, 21.98it/s]
 Average Training Loss=0.006585856477022171, Accuracy=80.05


Test set: Average loss: 0.4571, Accuracy: 8456/10000 (84.56%)

EPOCH: 185
Loss=1.007601022720337 Batch_id=390 Accuracy=79.95: 100%|██████████| 391/391 [00:17<00:00, 22.53it/s]
 Average Training Loss=0.006609790542125702, Accuracy=79.946


Test set: Average loss: 0.4533, Accuracy: 8457/10000 (84.57%)

EPOCH: 186
Loss=0.8820130825042725 Batch_id=390 Accuracy=79.84: 100%|██████████| 391/391 [00:18<00:00, 21.65it/s]
 Average Training Loss=0.006580075416564942, Accuracy=79.844


Test set: Average loss: 0.4557, Accuracy: 8455/10000 (84.55%)

EPOCH: 187
Loss=0.7195507287979126 Batch_id=390 Accuracy=79.85: 100%|██████████| 391/391 [00:17<00:00, 22.11it/s]
 Average Training Loss=0.006578385450839996, Accuracy=79.852


Test set: Average loss: 0.4540, Accuracy: 8455/10000 (84.55%)

EPOCH: 188
Loss=0.6714286804199219 Batch_id=390 Accuracy=80.13: 100%|██████████| 391/391 [00:18<00:00, 21.71it/s]
 Average Training Loss=0.006547041136026383, Accuracy=80.13


Test set: Average loss: 0.4537, Accuracy: 8453/10000 (84.53%)

EPOCH: 189
Loss=0.7800072431564331 Batch_id=390 Accuracy=80.26: 100%|██████████| 391/391 [00:17<00:00, 22.60it/s]
 Average Training Loss=0.006563224010467529, Accuracy=80.264


Test set: Average loss: 0.4555, Accuracy: 8465/10000 (84.65%)

EPOCH: 190
Loss=0.7903677821159363 Batch_id=390 Accuracy=79.91: 100%|██████████| 391/391 [00:17<00:00, 22.52it/s]
 Average Training Loss=0.006588157232999802, Accuracy=79.912


Test set: Average loss: 0.4531, Accuracy: 8465/10000 (84.65%)

EPOCH: 191
Loss=0.9071797132492065 Batch_id=390 Accuracy=80.07: 100%|██████████| 391/391 [00:17<00:00, 21.84it/s]
 Average Training Loss=0.006564309729337693, Accuracy=80.074


Test set: Average loss: 0.4564, Accuracy: 8453/10000 (84.53%)

EPOCH: 192
Loss=1.0352210998535156 Batch_id=390 Accuracy=79.83: 100%|██████████| 391/391 [00:17<00:00, 21.86it/s]

 Average Training Loss=0.006616116199493408, Accuracy=79.834

Test set: Average loss: 0.4551, Accuracy: 8441/10000 (84.41%)

EPOCH: 193
Loss=0.7693213224411011 Batch_id=390 Accuracy=79.86: 100%|██████████| 391/391 [00:17<00:00, 22.72it/s]
 Average Training Loss=0.006595038524866104, Accuracy=79.862


Test set: Average loss: 0.4560, Accuracy: 8441/10000 (84.41%)

EPOCH: 194
Loss=0.7456497550010681 Batch_id=390 Accuracy=79.94: 100%|██████████| 391/391 [00:17<00:00, 22.50it/s]
 Average Training Loss=0.006573520458936691, Accuracy=79.94


Test set: Average loss: 0.4546, Accuracy: 8457/10000 (84.57%)

EPOCH: 195
Loss=0.8115904331207275 Batch_id=390 Accuracy=79.75: 100%|██████████| 391/391 [00:17<00:00, 22.21it/s]
 Average Training Loss=0.006631649228334427, Accuracy=79.75


Test set: Average loss: 0.4527, Accuracy: 8460/10000 (84.60%)

EPOCH: 196
Loss=0.7880194187164307 Batch_id=390 Accuracy=79.96: 100%|██████████| 391/391 [00:17<00:00, 21.73it/s]
 Average Training Loss=0.006574212167263031, Accuracy=79.964


Test set: Average loss: 0.4565, Accuracy: 8442/10000 (84.42%)

EPOCH: 197
Loss=0.6617103815078735 Batch_id=390 Accuracy=79.95: 100%|██████████| 391/391 [00:17<00:00, 22.46it/s]
 Average Training Loss=0.006591491751670837, Accuracy=79.954


Test set: Average loss: 0.4544, Accuracy: 8445/10000 (84.45%)

EPOCH: 198
Loss=0.8353649377822876 Batch_id=390 Accuracy=79.80: 100%|██████████| 391/391 [00:19<00:00, 20.31it/s]
 Average Training Loss=0.006634996507167816, Accuracy=79.796


Test set: Average loss: 0.4552, Accuracy: 8457/10000 (84.57%)

EPOCH: 199
Loss=0.8100250959396362 Batch_id=390 Accuracy=79.83: 100%|██████████| 391/391 [00:17<00:00, 22.26it/s]
 Average Training Loss=0.006632002103328705, Accuracy=79.832


Test set: Average loss: 0.4549, Accuracy: 8460/10000 (84.60%)

Total Number of incorrectly predicted images by model type BN is 1540
```

## Accuracy & Loss Graph
<img width="929" alt="Screenshot 2023-02-10 at 11 06 20 PM" src="https://user-images.githubusercontent.com/118976187/218158572-71c6646e-50f5-44a4-9761-1d180d451132.png">

## Overall Prediction Summary
<img width="256" alt="Screenshot 2023-02-10 at 11 06 50 PM" src="https://user-images.githubusercontent.com/118976187/218158689-a86a3760-b4ef-4c84-99dc-d90c5097eb0f.png">
