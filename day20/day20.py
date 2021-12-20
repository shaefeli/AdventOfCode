#This solution runs pretty fast
#Pad an image 
def pad_image(image,padding, charToPad):
    padded_image=[]
    width=len(image[0])
    height=len(image)
    for j in range(height+padding*2):
        if j<=padding-1 or j>=height+padding:
            padded_image.append([charToPad]*(width+padding*2))
        else:
            new_line=[charToPad]*padding+image[j-padding]+[charToPad]*padding
            padded_image.append(new_line)
    return padded_image

def displayImage(im):
    for l in im:
        print("".join(l))
    print("AAAAAAAAAAAAAAAAA")
 
#Find the next pixel value 
def get_neighbourghCharacters(i,j,im, algorithm):
    characters = im[j-1][i-1]+im[j-1][i]+im[j-1][i+1]+im[j][i-1]+im[j][i]+im[j][i+1]+im[j+1][i-1]+im[j+1][i]+im[j+1][i+1]
    char_to_bin=characters.replace("#","1").replace(".","0")
    index_in_algo=int(char_to_bin,2)
    return algorithm[index_in_algo]
    
 
#One step of the algorithm
#Note that we do a padding of 2 at the beginning to be sure to have enough pixels
#We only do computations from 1 to new_width-1 and 1 to new_height-1 and crop that region out at the end 
def enhanceImageOneStep(im,i,enhancement_algorithm):
    input_image_padded=[]
    #To know what we pad with, it is easy if the algorithm says that 0 gives ".", but otherwise, it depends on the values!
    #Note that at i odd, the number of lighting pixels is infinite.
    if i==0:
        charToPadWith="."
    else:
        if enhancement_algorithm[0]==".":
            charToPadWith="."
        else:
            if i%2==0:
                charToPadWith=enhancement_algorithm[511]
            else:
                charToPadWith=enhancement_algorithm[0]

    input_image_padded=pad_image(im,2,charToPadWith)
    new_width=len(input_image_padded[0])
    new_height=len(input_image_padded)
    output_image=[["."]*new_width for i in range(new_height)]
    for j in range(1,new_height-1):
        for i in range(1,new_width-1):
            output_image[j][i]=get_neighbourghCharacters(i,j,input_image_padded,enhancement_algorithm)
    
    return [line[1:-1] for line in output_image[1:-1]] #Crop
 
#We keep this ugly code because we don't want library imports
def countNrLights(im):
    nr_lights=0
    for line in im:
       for light in line:
           if light=="#":
               nr_lights+=1
    return nr_lights
                
    
if __name__ == "__main__":
    #with open("test_input_20","r") as fp:
    with open("input_day_20","r") as fp:
        lines=fp.readlines()
        enhancement_algorithm=[x for x in lines[0].strip()]
        image=[[x for x in line.strip()] for line in lines[2:]]
  
#For our input, the number of lighting pixels at an odd number of steps is infinite
#Part 1
nr_steps=2
output_image=image.copy()
for i in range(nr_steps):
    output_image = enhanceImageOneStep(output_image,i,enhancement_algorithm)
print("Solution part 1:")
if nr_steps%2==1 and enhancement_algorithm[0]=="#":
    print("Infinity!")
else:
    print(countNrLights(output_image))


#Part 2
nr_steps=50   
output_image=image.copy()
for i in range(nr_steps):
    output_image = enhanceImageOneStep(output_image,i,enhancement_algorithm)
print("Solution part 2:")
if nr_steps%2==1 and enhancement_algorithm[0]=="#":
    print("Infinity!")
else:
    print(countNrLights(output_image))
     
        

                
    


