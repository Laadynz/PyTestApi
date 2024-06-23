import requests as requests 

codigo = input('Ingrese el codigo del producto: ')

url = 'http://localhost/apiphp/productos.php?codigo='+codigo
response = requests.get(url)
print(response.json())