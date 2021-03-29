from PIL import Image
location=input("¿Donde esta la imagen que quieres convertir?")
image1 = Image.open(location)
im1 = image1.convert('RGB')
location=location.split(".")[0]+".pdf"
im1.save(location)
print("la imagen fue convertida con exito.")
