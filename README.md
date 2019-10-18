# Smart-Signature-Verification-System

A Web App uisng Django to recognize two signature using image processing.The process involves taking two signature made by the same individual .The objective of signature verification systems is to discriminate if a given signature is genuine (produced by the claimed individual), or a forgery (produced by an impostor).
After uploading below subprocesses will start.

Preprocessing –  With the use of Contrast-limited adaptive histogram equalization (CLAHE) to properly equalize the histogram and after that reading that image into grayscale.
Segmenting Strokes Pixels – To find and segment out the strokes in the signature but before that, the image has to be normalized.
Finding Orientation & its Frequency –  To find the orientation of each and every pixel of the normalized image and estimate the signature stroke across the signature image it is done by calculating the frequency of strokes for each chunk of the image i.e. distributing the signature image into a fixed block size.
Image Enhancement Normalizing –  To enhance the image by using oriented filters
Proper Thresholding – The proper thresholding and normalize the image between 0 and 1 and thinning the thresholded signature image and removing irrelevant points and noise in the image.
Features extraction – To extract features like corners and curves out of the image


***WEB APP FRONT END LOOK*** where user can upload two images of signature of same individual to be compared
![Image of Web App Front End Look](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture.PNG)

***User will Upload Images through Web App***
![Image of Uploading Image](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture2.PNG)

***After Uploading the image so result is being processed so page will show a response that page is loading***
![Image of Result Processing](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture3.PNG)


# Input
***Reference Image Uploaded***
![Image of Reference Image](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture9.PNG)

***Image to be Compared uploaded***                
![Image of Image to be Compared](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture10.PNG)

# OUTPUT

***Graph showing is how its to extract features like corners and curves out of the both of the image***
![Image of Graph](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture4.PNG)

***Graph showing how it matching all the extracted features of both of the images using matchmaker algorithm***
![Image of Graph](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture5.PNG)

## Final Result 
***Showing the Accuracy as a Result as signature match score of compared Image***
![Image of Result](https://github.com/basant01/Smart-Signature-Verification-System/blob/master/Web-App%20Images/Capture6.PNG)


***Application Folder - Contains all the pages of Web App***

***Data Folder - Contains the Dataset used for this Web App***

***Libraries Folder - Contains code of all Libraries used for image processing***

***SignatureVerificationApplication Folder - Contains the main code for Web Application***



