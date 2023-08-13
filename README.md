# Machine_Learning_Task
## Download the Model
[Model](https://drive.google.com/file/d/1C26_H58Kiqy-PKe_3jvPItwDzQ3P7Pqm/view?usp=sharing)
### Reason of selection of deep learning model:
 - Categorizing the resume involves capturing complex patterns and features in text data and machine learning model can be utilized but for the individually features not finding the context of the patterns.
 - Performance of the training model can be seen easily which helps to adjust the model for better training and that can not be done in the machine leanring model.
### PreProcessing
 - Tokenization are used for extracting features from the resume
 - 1800 maxlen is chosen because it uniform the every class distribution for their own maximum length.
 - glove or any pretrained models are not applied because of their poor performance. The reason is the resume text are not derived from any book or any full sentence. However, the glove or other vectorization of the models are derived from any meaning full sentence or any book. So there is no any compatibility here.
### Instruction for running the model
 - Pull the whole github reprository and download the model.
 - install the required files using the below command:
   ```
   pip install requirements.txt
   ```
 - run the script
   ```
   python script.py path/to/dir
   ```
 - It will return as csv file like the above categorized_resumes.csv and will also store the file in their respective categorized folder automatically.
Note: All files should be in the same directory.
