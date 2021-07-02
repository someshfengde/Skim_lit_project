import tensorflow as tf 
import pandas as pd 
import numpy as np  
import gdown 
import zipfile
class_names = ['BACKGROUND', 'CONCLUSIONS', 'METHODS', 'OBJECTIVE', 'RESULTS']

@st.cache(ttl = 900, max_entries = 3)
def download_and_unzip_model():
    gdown.download('https://drive.google.com/uc?id=1do7b5zE_Xf8gThqiGutgaILPSFE67rHs',output= './output.zip')
    with zipfile.ZipFile("./output.zip","r") as zip_ref:
        zip_ref.extractall("./")

@st.cache(ttl = 900, max_entries = 3)
def get_model(model_path):
    download_and_unzip_model()

    model = tf.keras.models.load_model(model_path)
    return model 

def split_char(text):
  return " ".join(list(text))

def preprocess_text(text):
    sample = []
    
    splitted_text = text.splitlines()

    for line_no,line in enumerate(splitted_text):
        line_data  = {}
        target_text = line.lower().replace('!@#$%^&*:",.<>',"")
        line_data['text'] = target_text.lower()
        line_data['line_number'] = line_no
        line_data['total_lines'] = len(splitted_text)- 1 
        sample.append(line_data)
    
    dataframe = pd.DataFrame(sample)
    
    textual_data_to_feed = dataframe.text.to_numpy()
    line_numbers_encoded = tf.one_hot(dataframe.line_number.to_numpy(),depth = 15)
    
    total_lines_encoded = tf.one_hot(dataframe.total_lines.to_numpy(),depth = 20)
    
    text_characters = [split_char(scentence) for scentence in textual_data_to_feed]
    return line_numbers_encoded,total_lines_encoded,textual_data_to_feed,text_characters
    

def predict_on_text(text,model):
    line_numbers,total_lines,text_data, text_char  = preprocess_text(text)
    prediction = model.predict((line_numbers,total_lines,tf.cast(text_data,'string'),tf.cast(text_char,'string')))
    array_of_preds = list(tf.argmax(prediction , axis = 1).numpy())
    pred_with_label = [class_names[x] for x in array_of_preds]

    return text_data, pred_with_label

def get_prediction(text):
    model = get_model('./big_model_4_ip')
    textual_data,pred_with_label = predict_on_text(text,model)
    return textual_data , pred_with_label

