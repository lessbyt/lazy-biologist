from google.cloud import vision
from google.cloud.vision import ImageAnnotatorClient
from shutil import copyfile
import os
import io

##Autenticarse con la API
client = vision.ImageAnnotatorClient()


##Leer path de imagenes PYTHON3
img_path = str(input("Cual es la ruta(path) absoluta de las imagenes a procesar?"+"\n"))
##Validar que existe el path
assert os.path.exists(img_path), "No fue posible encontrar la ruta, "+str(img_path)

##Leer el path donde se guardaran los resultados
result_path = str(input("Cual es la ruta(path) donde deberan guardarse los resultados?"+"\n"))
##Validar que existe el path
assert os.path.exists(result_path), "No fue posible encontrar la ruta, "+str(result_path)


##Calcular numero de imagenes a procesar
total=len([name for name in os.listdir(img_path) if os.path.isfile(os.path.join(img_path, name))])


##Procesamiento de imagenes
##Cargar imagenes en memoria para poder revisar en orden secuencial, se establece una variable para ir recorriendo el arreglo
#images=sorted(os.listdir(img_path))
img_num=0

##Se inicia un ciclo para recorrer el total de imagenes
for i in range(total):
    ##Esto cuando se van eliminando del origen
    images=sorted(os.listdir(img_path))

    ##Se carga el nombre de la imagen
    pic_name=images[img_num]
    ##Se carga la imagen
    pic = os.path.abspath(img_path+pic_name)
    with io.open(pic, 'rb') as pic_file:
        pic_content = pic_file.read()
        
    ##Se carga la imagen para la API
    imagen = vision.Image(content=pic_content)
    
    ##Se hace la consulta y se guarda la respuesta en una variable
    ##La appi cuenta con varias opciones, en este caso nos interesa identificar los objetos
    ##OBJECT_LOCALIZATION, LANDMARK_DETECTION, FACE_DETECTION,LOGO_DETECTION,LABEL_DETECTION, DOCUMENT_TEXT_DETECTION, SAFE_SEARCH_DETECTION, IMAGE_PROPERTIES,CROP_HINTS 
    
    response = client.object_localization(image=imagen)
    
    ##Se crea un directorio para almacenar las imagenes que google no pueda reconocer
    if not os.path.exists(result_path+"NPI"):
        os.mkdir(result_path+"NPI")
    if not os.path.exists(result_path+"Otro"):
        os.mkdir(result_path+"Otro")
    copyfile(img_path+pic_name,result_path+'/NPI/'+pic_name)
    
    ##Imprimir resultados
    print('Resultados para la imagen: '+pic_name)
    print('=' * 30)
    
    ##En este caso solo se tomara el primer resultado para cada imagen
    s=1
    
    ##Se analizan los resultados
    for label in response.localized_object_annotations:
        print(label.name, '(%.2f%%)' % (label.score*100.))
        if s==1:
            ##La imagen si se encontro por lo que se borra del directorio NPI
            os.remove(result_path+'/NPI/'+pic_name)
            ##Unicamente se consideran imagenes con resultados mayores al 70%
            if label.score > 0.7:
                ##Se revisa si existe un directorio con esa etiqueta
                if not os.path.exists(result_path+label.name):
                    os.mkdir(result_path+label.name)
                
                ##Se copia la imagen a la carpeta correspondiente
                copyfile(img_path+pic_name,result_path+label.name+'/'+pic_name)
                s=s+1
                
            else:
                ##Imagenes con resultados menores al 70% se guardan en Otro
                copyfile(img_path+pic_name,result_path+'/Otro/'+pic_name)
                s=s+1
    
    ##Se suma el contador para revisar la siguiente imagen
    #img_num=img_num+1
    os.remove(img_path+pic_name)           
            
    
    