import numpy as np
import cv2
from skimage import exposure
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import sys
import os
import time

def draw_contour(event, x, y, flags, param):
    global pts, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pts = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        pts.append((x, y))
        cv2.line(img, pts[-2], pts[-1], (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        pts.append((x, y))
        cv2.line(img, pts[-2], pts[-1], (0, 255, 0), 2)
        # Close the contour
        cv2.line(img, pts[-1], pts[0], (0, 255, 0), 2)


def apply_active_contour(image, initial_pts):


    gray_image = rgb2gray(image)
    
    equalized_image = exposure.equalize_adapthist(gray_image)
    
    edges = cv2.Canny((equalized_image * 255).astype(np.uint8), 100, 200)
    
    smoothed_edges = gaussian(edges, 1)

    initial_pts_np = np.array(initial_pts)
    initial_pts_np = np.fliplr(initial_pts_np) 

    snake = active_contour(smoothed_edges,
                           initial_pts_np,
                           alpha=0.01,  
                           beta=1,      
                           gamma=0.01,  
                           convergence=0.01,
                           max_num_iter=5000,  
                           boundary_condition='periodic')

    return snake


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        sys.exit(1)
    
    temp_img = img.copy()
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", draw_contour)

    global pts
    pts = []  
    global drawing 
    drawing = False  

    while True:
        cv2.imshow("Image", img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('r'):
            img = temp_img.copy()
        elif k == 32:  # Space bar key
            break

    cv2.destroyAllWindows()

    print("\nWait for the initialization of the algorithm...")
    print("\nThis can take around 40-50 seconds...\n")
    if pts:
        snake = apply_active_contour(temp_img, pts)
        
        snake_xy = np.fliplr(snake).astype(np.int32)

        # Simulate intermediate steps
        steps = 700  
        for i in range(1, steps + 1):
            intermediate_pts = pts + (snake_xy - pts) * i / steps
            temp_img_with_step = temp_img.copy()
            cv2.polylines(temp_img_with_step, [intermediate_pts.astype(np.int32)], isClosed=True, color=(0, 255, 0), thickness=3)
            cv2.imshow("Adjusting Contour", temp_img_with_step)
            cv2.waitKey(30)  
        time.sleep(1)

        cv2.polylines(temp_img, [snake_xy], isClosed=True, color=(0, 255, 0), thickness=3)
        cv2.imshow("Final Result", temp_img)
        
        result_path = "Results/Active_Contour"
        if not os.path.exists(result_path):
            os.makedirs(result_path)
        filename = os.path.splitext(os.path.basename(image_path))[0] + "_contour_result.png"
        result_image_path = os.path.join(result_path, filename)
        cv2.imwrite(result_image_path, temp_img)
        print(f"Result saved at {result_image_path}")

        cv2.destroyAllWindows()