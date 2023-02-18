# ML_CNN_detection


<h3 align="center">Skin cancer detection application</h3>



<div>
  <p>The purpose of this application is given a picture of a mole the application returns the probablity of being malign  </p>
    <p>This project has given me the opportunity to further my Vue Js skills as well as learn about Convultional Neurel Networks</p>
<p>Further information about the application will be provided shortly </p>

  <p>The Web App gives the user to upload a photo of a specific mole. The app will return a prediction of what categoring the mole is in :Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec), basal cell carcinoma (bcc), benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl), dermatofibroma (df), melanoma (mel), melanocytic nevi (nv) and vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc). </p>

<h4>Tech stack of Web App and Tools:</h4>
  
- Front-end: Vue Js
  
- Backend: Flask Restful
  
 - Axios library is used to consume the Flask API
  
 - Tools: Tensorflow, keras, Python, Jupyter notebooks, matplotlib, scikit-learn, Flask, Vue Js
  
  
 <h4>Machine Learning Algorithm:</h4>

- Data was obtained from Kaggle. It consisted of dermatoscopic images from different populations. Cases include a representative collection of all important diagnostic cateogories in the realm of pigmented lesions. 
 <a href="https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000?select=hmnist_28_28_L.csv" target="_blank">Link to data </a>
 
- A convolutional Neurel Network (CNN) was used for this task. It is a subtype of Neural Network. The built-in convolutional layer reduces the high dimensionality of images without losing its infromation. 
  
- Results of model:
<img src="https://user-images.githubusercontent.com/90276026/219903679-dd99eed7-18fa-4fb0-b277-5adaa41b4697.png" width="400" height="400" />
  
  <h4>Walk through of application:</h4>
  


https://user-images.githubusercontent.com/90276026/219856815-ac6e793c-545d-4578-8026-1a252bd54fc0.mp4



  <h4>Challenges and Areas of future work:</h4>
  
- Increase accuracy of model: Augmenting the dataset to produce more samples of the lesser lables 
- Build a mobile application 


 
</div>
