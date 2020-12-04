def load_image(obr):
    image={"type":"",
       "comment":"",
       "size":[],
       "pixels":[]}
    
    file=open(obr,"r+")
    image_str=file.read()
    image_str=image_str.split("\n")

    #print (image)
    image["type"]=image_str.pop(0)
    image["comment"]=image_str.pop(0)

    size=image_str.pop(0)
    #print (size)
    size=size.split(" ")
    #print (size)
    image["size"]=[int(size[0]),int(size[1])]
    #print (image["size"])

    image["pixels"]=image_str
    #print (image)
    file.close()
    return image
def generate_square(size, colour=True):
    iamge = {}
    image["type"] = "P1"
    image["size"] = [size, size]
    image["comment"] = ''
    image["pixels"] = []
    for row in range(size):
        line = []
        for col in range(size):
            if colour:
                line.append(0)
            else:
                line.append(1)
        image["pixels"].append(line)
    # przypisz rozmiar [n,n]
    #wygeneruj kwadrat
    # dla n wierszy
    #dodaj n 0/1 (w zaleznosci od koloru) od wiersza (listy)
    #zapisz wiersz
    return image

def negative(image):
    # 0 -> 1
    # 1 -> 0
    for row in range(image[size][1]):
        for col in range(image[size][0]):
            if image["pixels"][row][col] == 0:
                image["pixels"][row][col] = 1
            else:
                image["pixels"][row][col] = 0
    return image

def generate_chessboard(size):
    image = {}
    image["type"] = "P1"
    image["size"] = [size, size]
    image["comment"] = ''
    image["pixels"] = [[1,0,0,0,0,0,0,0,0]]
    for row in range(size):
        if image["pixels"][-1][0] == 0:
            line = [1]
            for col in range(size):
                if line[-1] == 1:
                    line.append(0)
                else:
                    line.append(1)
            image["pixels"].append(line)
        else:
            line = [0]
            for col in range(size):
                if line[-1] == 1:
                    line.append(0)
                else:
                    line.append(1)
            image["pixels"].append(line)
    image["pixels"].pop(0)
    print (image["pixels"])
    return image
# nie wiedziałem jak zrobić by sprawdzał pierwsza liczbe z slownika

def generate_diagonal(size):
    pass

def mirror_y(image):
    pass



def save_image(image,obr):
    file=open(obr,"w+")
    file.write(image["type"]+"\n")
    file.write(image["comment"]+"\n")
    file.write(str(image["size"][0])+" "+str(image["size"][1])+"\n")
    razy=int(image["size"][1])
    for i in range (razy):
        # file.write(str(image["pixels"][i])+"\n")
        for o in range (razy):
            file.write(str(image["pixels"][i][o]))
        file.write("\n")
    file.close()
    

image=load_image("obr.pgm")
#generate_square(3, True)
generate_chessboard(10)
save_image(image,"orb.pgm")
