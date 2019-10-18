from django.shortcuts import render
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import Context,loader
import json
import os
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt
import requests
import re
import pymysql
import sys
import argparse
import cv2
from matplotlib import pyplot as plt
from Libraries.ExtractKeypoints.ExtractKeypoints import extractKeypoints

# Create your views here.
def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', help='Provide signature image path needs to be verified', type=str, default='C:/Users/jashok/OneDrive - Huron Consulting Group/Documents/SignatureVerification/SignatureVerification/SignatureRecognition-master/SignatureRecognition-master/Data/12.jpg')
    parser.add_argument('--ref_image', help='Provide reference signature image path needs to be verified', type=str, default='C:/Users/jashok/OneDrive - Huron Consulting Group/Documents/SignatureVerification/SignatureVerification/SignatureRecognition-master/SignatureRecognition-master/Data/signature.jpg')
    parser.add_argument('--thres', help='Signature matching threshold', type=int, default=20)
    parser.add_argument('--visual', help='Visulisation of result', type=bool, default=True)
    return parser.parse_args()

def home(request):
    return render(request,'index.html')
@csrf_exempt
def func_hello(requests):
	try:
		if(requests.method=='POST'):
			print(requests.body)
			data = json.loads((requests.body))
			print(data)
			refImagePath = 'C:/SignatureRecognition-master/Data/'+data["refImage"]

			compareImagePath = 'C:/SignatureRecognition-master/Data/'+data["compImage"]

			print(refImagePath)
			print(compareImagePath)
			# args = setup()
			print('----|| INIT MODULE ||----')
			img1 = cv2.imread(refImagePath, cv2.IMREAD_GRAYSCALE)
			kp1, des1 = extractKeypoints(img1)
			img2 = cv2.imread(compareImagePath, cv2.IMREAD_GRAYSCALE)
			kp2, des2 = extractKeypoints(img2)

			bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
			matches = sorted(bf.match(des1, des2), key=lambda match: match.distance)

			img4 = cv2.drawKeypoints(img1, kp1, outImage=None)
			img5 = cv2.drawKeypoints(img2, kp2, outImage=None)


			f, axarr = plt.subplots(1, 2)
			axarr[0].imshow(img4)
			axarr[1].imshow(img5)
			plt.show()

			img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, flags=2, outImg=None)
			plt.imshow(img3)
			plt.show()

			score = 0
			retVal = ""
			for match in matches:
				score += match.distance
			if score / len(matches) < 10:
				print("RESULT: Signature match with score = {}".format(100-(score / len(matches))))
				retVal = ("RESULT: Signature match with score = {}".format(100-(score / len(matches))))
			else:
				print("RESULT: Signature does not match.")
				retVal = ("RESULT: Signature does not match.")
			print('----|| MODULE ENDED ||----')
		return HttpResponse(retVal)

	except Exception as e:
		return HttpResponse(e)
