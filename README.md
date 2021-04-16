# Age-Gender-Detection
- UTKFace data downloaded from [Kaggle](https://www.kaggle.com/jangedoo/utkface-new) (using Kaggle API)
- The labels of each face image is embedded in the file name, formated like ***age_gender_race_date&time.jpg***
- Built a 4-layered CNN and added a multiple outputs full connected layer
  - Age is a regression problem, so I used **RELU** as the output activation function and **Mean Absolute Error** as the loss function
  - Gender is a classification problem, so I used **sigmoid** as the output activation function and **Binary Crossentropy** as the loss function
- Ran the model on 250 epochs with early stopping if the val_loss does not improve
- Made prediction on the test data
- Saving model

- GUI using TKinter
- Clicking a real time image using CV2
- Predicting using the saved weights on real time image or an image in the directory
