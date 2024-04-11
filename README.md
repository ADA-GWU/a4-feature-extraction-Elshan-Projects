# Task 1: Edge Analysis
* The notebook containing my solution to this task is ___Edge_Analysis_Notebook.ipynb___
* The photo I took for this experiment: ___Original_Images/Edge_Analysis/photo_elshan.jpg___
* Pip dependencies: ___pip install numpy matplotlib opencv-python___
* Canny for Edge Detection, Shi-Tomasi (goodFeaturesToTrack) for Corner Detection, Hough for Line Detecton, Manual Contour Fitting for Ellipse/Circle Detection.
* The parameters for each detection algorithm were manually tuned to yield better results.
* The results are stored at: ___Results/Edge_Analysis_Results___

# Task 2: Active Contour
* The scipt name: ___Contour_Interactive_Elshan.py___
* The sample images to test the script are at: ___Original_Images/Active_Contour___
* The results are stored at: ___Results/Active_Contour___
* Pip dependencies: ___pip install numpy opencv-python scikit-image___
### How to use it: 
1. Run the script from the command line with the image file path as an argument.
#### (For example, ___python Contour_Interactive_Elshan.py Original_Images/Active_Contour/Car_Contour_Sample.jpg___)
3. Once the image window opens, use the mouse to draw an initial contour:
4. Left mouse button click and drag to draw.
5. Release the mouse button to finish drawing.
6. If you need to redraw the contour, press __R__ to reset the image to its original state.
7. Press the __Space Bar__ when you are done drawing the initial contour. The script will then process the image using the active contour algorithm, showing the contour adjustments gradually.
8. The final result will be displayed in a window, and the image with the contour drawn on it will be saved at the following path: ___Results/Active_Contour___ within the script's running directory. The file itself will be named according to the input file but with ____contour_result.png___ appended to the original file name.

# Task 3: Interest points


