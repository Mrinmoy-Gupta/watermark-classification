# watermark-classification

## Motivation
Training image-based machine learning models requires a substantial amount of data, typically obtained by scraping from the web. However, this data often contains watermarks, which can negatively impact the performance of our models. To address this issue, we may consider utilizing watermark removal techniques.

However, applying these techniques to the entire dataset can be highly inefficient. As a solution, we can develop a watermark detection application, which would identify the presence of watermarks in the images. This would allow us to selectively apply the watermark removal technique only to the images that require it, optimizing the process and improving the efficiency of our data preparation pipeline. Hence our goal was to develop an automated watermark classification model that efficiently recognizes and classifies watermark images

## Comparative study
Selecting the appropiate architecture is crucial for training image recognition models. in this project I compared the performance of densenet121, inceptionv3 and vgg16 to determine the most effective architecture  for our task of image recognition

## Web APP development
Beyond the model itself, we also built an USER-FRIENDLY web application to showcase the ability of our watermark recongnition system. leveraging streamlit, a powerful python library for building interactive web application, we built a seamless and intuitive user interface. it allows the user to upload their images and quickly determine wether they contain watermark, providing a practical and easy solution
