from google_images_download import google_images_download

keyword = input("Enter the Data class to be created\n")
lim = input("Enter the no of images to be downloaded\n")


response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":keyword,"limit":int(lim),"print_urls":True}   
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
