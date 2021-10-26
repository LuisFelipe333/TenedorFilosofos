from imgurpython import ImgurClient

import os
import urllib.request
import timeit   
from concurrent.futures import ThreadPoolExecutor

secret_client = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_client = "bfa0e227a1c5643"

client = ImgurClient(id_client, secret_client)

def descarga_url_img(link):
    #print(link)
    nombre_img = link.split("/")[3]
    formato_img = nombre_img.split(".")[1]
    nombre_img = nombre_img.split(".")[0]
    url_local = "C:/Users/user/Documents/imagenes/{}.{}"
    urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

def main():
    id_album = "bUaCfoz"
    imagenes = client.get_album_images(id_album)
    links=[]
    for imagen in imagenes:    
        links.append(imagen.link)
    #print(links)

    with ThreadPoolExecutor(10) as executor:
        executor.map(descarga_url_img,links)

if __name__ == '__main__':
    print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))
