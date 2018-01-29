import cv2
import os
import glob

img=cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)

#resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #Metodo para modificar el tamaño de una imagen
#cv2.imshow("Image Shows", resized_image) # Metodo para presentar imagenes en una ventana
#cv2.imwrite("Galaxy_resized.jpg", resized_image) # Metodo para guardar / escribir una imagen
#cv2.waitKey(0) # waitKey(0) cierra la ventana al oprimir cualquier tecla / waitKey(n) espera n milisegundo para cerrar ventana
#cv2.destroyAllWindows() # Metodo que permite cerrar la ventana al oprimir cualquier boton -- combina cuando queremos cerrar la imagen antes que culmine el timer

images=glob.glob("*.jpg")
print (images)
for image in images:
    img=cv2.imread(image,0)
    resized=cv2.resize(img,(100,100))
    cv2.imshow("Hey", resized)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,resized)
    print ("resized_"+image)
