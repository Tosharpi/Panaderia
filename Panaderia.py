menu = {

    "pan-Salados": {
        "producto": [
            {"nombre": "pan de trigo", "valor": 2500},
            {"nombre": "pan de centeno", "valor": 2000},
            {"nombre": "pan de espelta", "valor": 7500},
            {"nombre": "pan de maiz", "valor": 1500},
            {"nombre": "pan de germinado", "valor": 2500},
            {"nombre": "Baguettes", "valor": 2500},
            {"nombre": "Pan de pueblo", "valor": 2000},
            {"nombre": "Pretzels", "valor": 7500},
            {"nombre": "pan de ajo", "valor": 1500},
            {"nombre": "panecillo", "valor": 2500},
        ]
    },
    "pan-Dulce": {
        "producto": [
            {"nombre": "pan de dulce1", "valor": 2500},
            {"nombre": "rol de canela", "valor": 2600},
            {"nombre": "rosca de reyes", "valor": 2700},
            {"nombre": "panque", "valor": 2800},
            {"nombre": "tarta", "valor": 2900},
            {"nombre": "donas", "valor": 2900},
            {"nombre": "empanadas dulces", "valor": 2900},
            {"nombre": "croissant", "valor": 2900},
            {"nombre": "pasteles", "valor": 2900},
            {"nombre": "donas glaseadas", "valor": 2900},
        ]}

},  
promociones=[
        {"nombre promo": "promocion del 2x1 en pan de centeno", "valor": 2000},
        {"nombre promo": "promocion del 50% en pan de maiz", "valor": 1500},
        {"nombre promo": "promocion del 25% en pan de espelta", "valor": 7500},
    ]

#mostrar promociones
print('¿desea saber las promociones del dia? si=0 y no=1')
quierePromos=int(input())
print(quierePromos)


if quierePromos == 0:
    for promocion in promociones:
        print("Promoción:")
        for key, value in promocion.items():
            print(f"{key}: {value}")
        print()
else:
    print('ok')

#modulo para mostrar todas las categorias de mi lista deproducida
print("seleccione la categoria")
listaCategorias = menu.keys()

listaCategorias = list(listaCategorias)

for i, val in enumerate(listaCategorias):
    print(f"{i}. {val}")
opcionCategoria = int(input())
seleccionCategoria = menu.get(listaCategorias[opcionCategoria])
#print(seleccionCategoria)
#print(seleccionCategoria)
productoMostrar = seleccionCategoria.get("producto")


#mostrar productos

print("Productos disponibles en la categoría seleccionada:")
for i, producto in enumerate(productoMostrar):

    productoNom=producto["nombre"]
    productoValor=producto["valor"]
    print(i, productoNom, productoValor)

#seleccionar el producto
print('ingrese el codigo del producto')
opcionProducto = int(input())

if opcionProducto < 0 or opcionProducto >= len(productoMostrar):
    print('codigo del producto no valida')
else :

    productoSeleccionado = productoMostrar[opcionProducto]
    nombreProducto=productoSeleccionado["nombre"]
    precioProducto=productoSeleccionado["valor"]
print(f"ha seleccionado el producto {nombreProducto}, con un valor de {precioProducto}")

#cantidad
cantidadDelProducto=int(input('cuantas unidades desea llevar'))
precioProductoFinal=precioProducto*cantidadDelProducto
print(f"la cantidad seleccionada es {cantidadDelProducto} y la factura tendra un valor de {precioProductoFinal}")

#pago
saldo=int(input("ingrese el dinero para pagar: "))
if saldo <precioProductoFinal:
    print('dinero insuficiente')
else:

    vueltas=saldo-precioProductoFinal
    print('compra realizada exitosamente')
if vueltas>0:
    print('sus vueltas son: ', vueltas)
        
        




