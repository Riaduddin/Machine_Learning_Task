from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import nltk
import gensim
import pandas as pd
import numpy as np
import fitz
import argparse
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')
stopwords=stopwords.words('english')

class_names=['HR', 'DESIGNER', 'INFORMATION-TECHNOLOGY', 'TEACHER', 'ADVOCATE', 'BUSINESS-DEVELOPMENT', 'HEALTHCARE', 'FITNESS',
          'AGRICULTURE', 'BPO', 'SALES', 'CONSULTANT', 'DIGITAL-MEDIA', 'AUTOMOBILE', 'CHEF', 'FINANCE', 'APPAREL', 
            'ENGINEERING', 'ACCOUNTANT', 'CONSTRUCTION', 'PUBLIC-RELATIONS', 'BANKING', 'ARTS','AVIATION']
def clean_text(text):
    texts=text.lower()
    nltk.tokenize.word_tokenize(texts)
    result=[]
    for word in gensim.utils.simple_preprocess(texts):
      if word not in stopwords and len(word)>3:
        result.append(word)
    result= " ".join(result)
    return result


def tokenization(text):
  with open('tokenizer.json', 'r') as json_file:
    tokenizer_json = json_file.read()
    saved_tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_json)
  test_sequence=saved_tokenizer.texts_to_sequences([text])
  padded_data=pad_sequences(test_sequence,maxlen=1800,padding='post')
  return padded_data

def prediction(text):
  model=tf.keras.models.load_model('model.hdf5')
  category=model.predict([text])
  category=np.argmax
  return category

def read_file(pdf_dir):
  data=pd.DataFrame(columns=['filename','category'])
  for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
      pdf_path=os.path.join(pdf_dir,filename)
      pdf_document=fitz.open(pdf_path)

      pdf_text= ""
      for page_num in range(pdf_document.page_count):
        page=pdf_document.load_page(page_num)
        pdf_text += page.get_text()
      pdf_document.close()
      clean_text=clean_text(pdf_text)
      padded_data=tokenization(clean_text)
      category=prediction(padded_data)
      category=class_labels[category]
      data=data.append({'filename':filename,'category':category},ignore_index=True)

  csv_file='categorized_resumes.csv'
  data.to_csv(csv_file,index=False)



def main():
  parser=argparse.ArgumentParser(description="Process of the pdf directory")
  parser.add_argument("directory",help='Path of the directory')
  args = parser.parse_args()
  directory_path = args.directory

  read_file(directory_path)

if __name__ == "__main__":
    main()
