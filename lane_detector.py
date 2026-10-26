import cv2
import numpy as np
import os

#create output folders if they do not exist
os.makedirs("output",exist_ok=True)

def detect_lanes(image_path):
    #step 1 :load the road image 
    image = cv2.imread(image_path)

    if image is None:
        print("error: Image not found")
        print("check the image path:",image_path)
        return
    #save a copy of original image
    cv2.imwrite("output/01_original.jpg",image)

    #step 2: convert BGR image to HSV

    hsv= cv2.cvtColor(image , cv2.COLOR_BGR2HSV)

    #detect white lane markings 
    white_lower = np.array([0,0,180])
    white_upper = np.array([180,60,255])
    white_mask = cv2.inRange(hsv, white_lower,white_upper)
     
    #detect yellow lane markings 
    yellow_lower = np.array([15,60,80])
    yellow_upper = np.array([40,255,255])
    yellow_mask = cv2.inRange(hsv, yellow_lower,yellow_upper)

    #Combine white and yellow masks
    color_mask=cv2.bitwise_or(white_mask,yellow_mask)
    cv2.imwrite("output/02_hsv_mask.jpg",color_mask)

    #step 3 :applying gaussian blur 
    blurred = cv2.GaussianBlur(color_mask,(5,5),0)

    cv2.imwrite("output/03_blurred.jpg",blurred)

    #step 4: apply canny edge detection 
    edges = cv2.Canny(blurred , 50 , 150)

    cv2.imwrite("output/04_canny.jpg",edges)

    #step 5 : Create a region of interest mask
    height , width = edges.shape

    #polygon covering the road area
    polygon = np.array([[
        (int(width * 0.05), height),
        (int(width * 0.4), int(height*0.55)),
        (int(width * 0.6), int(height*0.55)),
        (int(width * 0.95), height),

    ]],dtype=np.int32)

    #create a black mask and fill the road polygon 
    roi_mask = np.zeros_like(edges)
    cv2.fillPoly(roi_mask , polygon , 255)

    #keep edges only inside roi
    roi_edges = cv2.bitwise_and(edges,roi_mask)
    cv2.imwrite("output/05_roi.jpg",roi_edges)
    
    #show detected edges on the original image
    result= image.copy()
    

    #highlight detected edge lines in green 
    result[roi_edges>0]=[0,255,0]
    cv2.imwrite("output/06_lane_detection.jpg",result)

    #create a combined image for easy comparision
    original_resized = cv2.resize(image , (480,270))
    result_resized = cv2.resize(result , (480,270))

    combined = np.hstack((original_resized,result_resized))
    cv2.imwrite("output/07_comparision.jpg",combined)

    print("lane detection completed succesfully")
    print("check the output folder for the processed images")

    #running the program
if __name__ == "__main__":
    detect_lanes("images/road.jpg")


