import os
import glob
import matplotlib.image as mpimg


#this function loads in images and their labels then places them in a list
def load_dataset(image_dir):
    im_list = []
    images_types = ['day', 'night']

    #iterate through each image in the folder
    for im_type in images_types:
        
        #glob reads in any image with the extension "image_dir/im_type/*"
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):

            #read in the image
            im = mpimg.imread(file)

            #check if the image exists/if it's been correctly read-in
            if not im is None:
                
                #append the image, and its type to the image list
                im_list.append((im, im_type))
    return im_list