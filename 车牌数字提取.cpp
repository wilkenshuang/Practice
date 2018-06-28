#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace std;
using namespace cv;

const int max_value_H = 360 / 2;
const int max_value = 255;
const string window_capture_name = "Video Capture";
const string window_detection_name = "Object Detection";
int low_H = 0, low_S = 0, low_V = 0;
int high_H = max_value_H, high_S = max_value, high_V = max_value;

static void on_low_H_thresh_trackbar(int, void *)
{
	low_H = min(high_H - 1, low_H);
	setTrackbarPos("Low H", window_detection_name, low_H);
}
static void on_high_H_thresh_trackbar(int, void *)
{
	high_H = max(high_H, low_H + 1);
	setTrackbarPos("High H", window_detection_name, high_H);
}
static void on_low_S_thresh_trackbar(int, void *)
{
	low_S = min(high_S - 1, low_S);
	setTrackbarPos("Low S", window_detection_name, low_S);
}
static void on_high_S_thresh_trackbar(int, void *)
{
	high_S = max(high_S, low_S + 1);
	setTrackbarPos("High S", window_detection_name, high_S);
}
static void on_low_V_thresh_trackbar(int, void *)
{
	low_V = min(high_V - 1, low_V);
	setTrackbarPos("Low V", window_detection_name, low_V);
}
static void on_high_V_thresh_trackbar(int, void *)
{
	high_V = max(high_V, low_V + 1);
	setTrackbarPos("High V", window_detection_name, high_V);
}

RNG rng(123);
int main() {
//  	Mat img = imread("C:\\Users\\gd\\Desktop\\test\\037.jpg",IMREAD_COLOR);
	Mat img = imread("C:\\Users\\gd\\Desktop\\test.jpg", 1);
/*
	Mat gray=Mat::zeros(img.size(),CV_8UC2);
	cvtColor(img, gray, COLOR_BGR2GRAY);
	Mat bw = Mat::zeros(img.size(), CV_8UC2);;
	gray.copyTo(bw);
	inRange(img, Scalar(90, 135, 120), Scalar(210, 180, 128), dst);
	threshold(gray,bw, 120, 255, THRESH_BINARY);
	resize(img, dst, Size(1500, 900),0,0,INTER_AREA);
	namedWindow("original", 0);
	resizeWindow("original", Size(1500, 1500));
	imshow("original", img);*/
	namedWindow(window_capture_name, WINDOW_AUTOSIZE);
	namedWindow(window_detection_name, WINDOW_AUTOSIZE);

/*
	createTrackbar("Low H", window_detection_name, &low_H, max_value_H, on_low_H_thresh_trackbar);
	createTrackbar("High H", window_detection_name, &high_H, max_value_H, on_high_H_thresh_trackbar);
	createTrackbar("Low S", window_detection_name, &low_S, max_value, on_low_S_thresh_trackbar);
	createTrackbar("High S", window_detection_name, &high_S, max_value, on_high_S_thresh_trackbar);
	createTrackbar("Low V", window_detection_name, &low_V, max_value, on_low_V_thresh_trackbar);
	createTrackbar("High V", window_detection_name, &high_V, max_value, on_high_V_thresh_trackbar);*/

	//resizeWindow("thresh", Size(1500, 1500));
/*

	int key;
	key = waitKey(0);
	if (key == 'q')
		destroyAllWindows();*/
	
	Mat img_HSV, img_LAB,img_threshold1,img_threshold2,img_threshold3;
// 	img.convertTo(img_HSV, CV_32FC3, 1.0 / 255, 0);
// 	cvtColor(img, img_HSV, COLOR_BGR2HSV);

	cvtColor(img, img_LAB, COLOR_BGR2Lab);
	//inRange(img_HSV, Scalar(low_H, low_S, low_V), Scalar(high_H, high_S, high_V), img_threshold1);
  
	inRange(img, Scalar(180, 180, 180), Scalar(255, 255, 255), img_threshold1);
  
// 	inRange(img_LAB, Scalar(80, 150, 60), Scalar(200, 220, 128), img_threshold2);

	Mat element = getStructuringElement(MORPH_RECT, Size(5, 5));
	morphologyEx(img_threshold1, img_threshold2, MORPH_CLOSE, element);
	vector<vector<Point>> contours,contours0;
	vector<Vec4i> hierarchy;
	findContours(img_threshold2, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
	img_threshold3 = Mat::zeros(img.size(), img.type());

// 	morphologyEx(img_threshold2, img_threshold3, MORPH_OPEN, element);

	vector<vector<Point>> contours_poly(contours.size());
	vector<Rect> boundRect(contours.size());

	for (size_t i = 0; i<contours.size(); i++){
		approxPolyDP(Mat(contours[i]), contours_poly[i], 3, true);
		boundRect[i] = boundingRect(Mat(contours_poly[i]));
	}
	for (size_t i = 0; i < contours.size(); i++) {
		Scalar color = Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255));
		//drawContours(img_threshold3, contours_poly, (int)i, color);
		rectangle(img_threshold3, boundRect[i].tl(),boundRect[i].br(), color);
	}

	imshow(window_capture_name, img);

	imshow(window_detection_name, img_threshold3);

	char key = waitKey(0);
	if (key == 'q')
		destroyAllWindows();
}
