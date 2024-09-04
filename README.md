# LipReading-Webapp
you can refer our paper - https://www.preprints.org/manuscript/202312.0928/v1

We have developed a web application that can generate subtitles for any video uploaded in which the person’s mouth is visible.  We have developed our model using 3D-convolution network and LSTM bidirectional. Our model can make sentence level predictions based only on visual moments of lips. The lips region is segmented and created a animated gif and this was used as pre-trained data to train our model.

# Model
The segmentation of mouth region is done statically and by using imageio and use its mimsave  create an animation gif that our model will learn to decode.

 ![image](https://github.com/user-attachments/assets/80265fd6-2004-4799-b5f5-bafee888d3f1)

Fig-1 : The segmented region

To train our model we used CNN and LSTM	 combined architecture as it is a powerful approach to process sequential data with both spatial and temporal dependencies. The 3D convolution Network is better for working with videos. Similar to 2D convolution(spatial convolution), 3D convolution works by moving a kernel (also called a filter) across the input data to extract local characteristics. The kernel's size corresponds to the depth, height, and width of the data, and it spatially moves over the input volume. The kernel calculates the element-wise dot product with the relevant input sub-volume at each point. To create a feature map with high-level representations of the input volume, this process is repeated for all points. The output of the CNN is then fed into the LSTM as sequential data, where the LSTM captures temporal dependencies and patterns. In this architecture dense, dropout and bidirectional e able to convert paths through Temporeal component while using LSTM. As for the optimizer adam optimizer was used the final model was implemented using streamlit.

# RESULTS
![image](https://github.com/user-attachments/assets/e5d9e65e-40f8-4f0e-b32f-4f312d48987f)
![image](https://github.com/user-attachments/assets/ea508071-5e50-4f30-9805-c54261a06016)
![image](https://github.com/user-attachments/assets/b4eb1e01-d517-4740-a82f-fec5f82800b5)

We propose a web application LipReader where user can upload any video in which mouth movements are visible in the frame and the get the predicted end-to-end sentence level text which can be used as subtitles for the video. The accuracy of our model is 97% . The predicted text can reduce the time for subtitles creators and people with hearing impairments. Also people who can’t speak can record there videos and get predicted text and use text to audio convertor to have there own voice instead of using sign language. 
Refer ppt for better understanding
