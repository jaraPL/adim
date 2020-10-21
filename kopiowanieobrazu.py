def load_image(obr):
    image={"type":"",
       "comment":"",
       "size":[],
       "pixels":[]}
    
    file=open(obr,"r+")
    image_str=file.read()
    image_str=image_str.split("\n")

    print (image)
    image["type"]=image_str.pop(0)
    image["comment"]=image_str.pop(0)
    
    size=image_str.pop(0)
    print (size)
    size=size.split(" ")
    print (size)
    image["size"]=[int(size[0]),int(size[1])]
    print (image["size"])
    
    image["pixels"]=image_str
    print (image)
    file.close()
    return image


def save_image(image,obr):
    file=open(obr,"w+")
    file.write(image["type"]+"\n")
    file.write(image["comment"]+"\n")
    file.write(str(image["size"][0])+" "+str(image["size"][1])+"\n")
    razy=int(image["size"][1])
    r=0
    for i in range (razy):
        file.write(str(image["pixels"][r])+"\n")
        r=r+1
    file.close()
    

image=load_image("obr.pgm")

save_image(image,"orb.pgm")
