import streamlit as st 
import os
import imageio
import tensorflow as tf 
from utils import load_data, num_to_char
from modelutil import load_model

# Set the layout to the streamlit app as wide 
st.set_page_config(layout='wide')

# Setup the sidebar
with st.sidebar: 
    st.header('LipReader `version 1`')
    st.subheader('With the help of Speech recognition model')
    st.image('https://img.freepik.com/free-vector/flat-creativity-concept-illustration_52683-64279.jpg')
    st.title('LipReader')
    st.info('This application is developed using the LipNet model.')
    st.text('!!Works only on the given data!!')
    


    st.title('Lip Reading Application') 
# Generating a list of options or videos 
options = os.listdir(os.path.join('..', 'data', 's1'))
selected_video = st.selectbox('Choose video', options)

# Generate two columns 
col1, col2 = st.columns(2)

if options: 

    # Rendering the video 
    with col1:
        st.info('The video will be played below') 
        file_path = os.path.join('..','data','s1', selected_video)
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

        # Rendering inside of the app
        video = open('test_video.mp4', 'rb') 
        video_bytes = video.read() 
        st.video(video_bytes)

        


    with col2: 
        st.info('POV of the Machine learning Model')
        video, annotations = load_data(tf.convert_to_tensor(file_path))
        st.image('animation.gif', width=400)


        st.image('https://hackster.imgix.net/uploads/attachments/1299854/screen_shot_2021-05-18_at_1_20_20_pm_ujcNowYDP8.png?auto=compress%2Cformat&w=740&h=555&fit=max')


        model = load_model()
        yhat = model.predict(tf.expand_dims(video, axis=0))
        decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()


        # Convert prediction to text
        st.subheader('The Decoded result:')
        converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
        st.info(converted_prediction)
        
        

