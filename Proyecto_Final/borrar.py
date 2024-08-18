# Simulación de datos

# Producto
producto_id = 1
producto_nombre = "Vacuna Rabia"
producto_tipo = "Vacuna"
producto_precio = 50.0

# Proveedor
proveedor_id = 1
proveedor_nombre = "Proveedor A"
proveedor_contacto = "123456789"
proveedor_direccion = "Calle Falsa 123"
proveedor_productos = []

# Agregar producto al proveedor
proveedor_productos.append({
    'id': producto_id,
    'nombre': producto_nombre,
    'tipo': producto_tipo,
    'precio': producto_precio
})

# Pedido
pedido_id = 1
pedido_fecha = "2024-08-12"
pedido_cantidad = 10
empleado_id = 1
detalles_pedido = []

# Agregar detalles del pedido
detalles_pedido.append({
    'producto_id': producto_id,
    'nombre': producto_nombre,
    'cantidad': pedido_cantidad,
    'precio': producto_precio
})

# Calcular total del pedido
total_pedido = sum(item['cantidad'] * item['precio'] for item in detalles_pedido)

# Empleado
empleado_id = 1
empleado_nombre = "Juan Pérez"
empleado_email = "juan@example.com"
empleado_puesto = "Veterinario"
empleado_contraseña = "password123"

# Factura
factura_id = 1
factura_fecha = "2024-08-12"
factura_total = total_pedido
factura_pedido_id = pedido_id

# Mostrar resultados simulados

print("=== Producto ===")
print(f"ID: {producto_id}")
print(f"Nombre: {producto_nombre}")
print(f"Tipo: {producto_tipo}")
print(f"Precio: {producto_precio}")

print("\n=== Proveedor ===")
print(f"ID: {proveedor_id}")
print(f"Nombre: {proveedor_nombre}")
print(f"Contacto: {proveedor_contacto}")
print(f"Dirección: {proveedor_direccion}")
print(f"Productos: {proveedor_productos}")

print("\n=== Pedido ===")
print(f"ID: {pedido_id}")
print(f"Fecha: {pedido_fecha}")
print(f"Cantidad: {pedido_cantidad}")
print(f"Empleado ID: {empleado_id}")
print(f"Detalles del Pedido: {detalles_pedido}")
print(f"Total: {total_pedido}")

print("\n=== Empleado ===")
print(f"ID: {empleado_id}")
print(f"Nombre: {empleado_nombre}")
print(f"Email: {empleado_email}")
print(f"Puesto: {empleado_puesto}")

print("\n=== Factura ===")
print(f"ID: {factura_id}")
print(f"Fecha: {factura_fecha}")
print(f"Total: {factura_total}")
print(f"Pedido ID: {factura_pedido_id}")
