from difflib import SequenceMatcher as SM
cameras_dict = {}

def check_similarities_ratio(s1, s2):
    return SM(None, s1, s2).ratio()

def check_dictionary(camera_model, dict):
    
    # Loop through camera dictionary, checking the current model to
    # existing models to see the similarity in model names
    for item in dict:
        
        # check the similarity ratio of our camera models
        # If they're close to being the same, associate current 
        # camera model with existing camera model name,
        # otherwise insert new camera model by name 
        if check_similarities_ratio(item, camera_model) > 0.90:
            cameras_dict[item][camera_model] = item
        else:
            cameras_dict[camera_model] = {camera_model:camera_model}
            
def insert_into_dictionary(camera_model,dict):
    
    # Only insert unique camera model entries
    if camera_model not in dict:
        
        # If camera model dictionary is not empty check the existing models
        # to see if they're a close match to current camera model,
        # If camera dictionary is empty, just insert
        if len(dict) > 0:
            check_dictionary(camera_model,dict.copy())  
        else:
            cameras_dict[camera_model] = {camera_model:camera_model}
              
def run():
    
    # Read through the camera list 1 line at a time
    with open('camera_list.txt', 'r') as f:
        for camera_model in f:
            insert_into_dictionary(camera_model.rstrip(),cameras_dict)
    f.closed
run()
