import os
import cv2

def slice_image(image, horizontal, vertical):
  x,y,_ = image.shape
  num_y = y//horizontal
  num_x = x//vertical
  imgs = []
  for i in range(num_x):
    for j in range(num_y):
    
      start_pos_x = horizontal*i
      end_pos_x = horizontal*(i+1)
      start_pos_y = vertical*j
      end_pos_y = vertical*(j+1)
      img = image[start_pos_x:end_pos_x,start_pos_y:end_pos_y,:]
      imgs.append(img)
  return imgs  
  
abs_path_input = "C:\\Users\\Borealis\\Desktop\\NSCR\\crop_project\\perioxi_meletis\\ground truth_1"
abs_path_output = "C:\\Users\\Borealis\\Desktop\\NSCR\\crop_project\\perioxi_meletis\\output_ground truth"

for image_name in os.listdir(abs_path_input):
  image_path =os.path.join(abs_path_input ,image_name)
  img = cv2.imread(image_path)
  sliced_image_list = slice_image(img,227,227)  
  for i, sliced_image in enumerate(sliced_image_list):
    sliced_image_path = os.path.join(abs_path_output, image_name)
    sliced_image_path = sliced_image_path.replace('.jpg', '') + '_sliced' + str(i) + '.jpg' 
    cv2.imwrite(sliced_image_path, sliced_image)
    
    
