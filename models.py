from django.db import models

class CategoriaAlmacen(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.TextField()
    temperatura_ideal = models.CharField(max_length=50)
    tipo_almacenamiento = models.CharField(max_length=50)
    es_peligroso = models.BooleanField()

    def __str__(self):
        return self.nombre_categoria


class ProveedorAlmacen(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    contacto_persona = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion_proveedor = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_proveedor


class EmpleadoAlmacen(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    cargo = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    licencia_manejo_montacargas = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ProductoAlmacen(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    codigo_sku = models.CharField(max_length=50)
    stock_actual = models.IntegerField()
    ubicacion_almacen = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaAlmacen, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.CASCADE)
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2)
    volumen_m3 = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ultimo_movimiento = models.DateTimeField()

    def __str__(self):
        return self.nombre_producto


class EntradaProducto(models.Model):
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    cantidad_entrada = models.IntegerField()
    fecha_entrada = models.DateTimeField()
    proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.CASCADE)
    num_factura_compra = models.CharField(max_length=50)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    empleado_recepcion = models.ForeignKey(EmpleadoAlmacen, on_delete=models.CASCADE)
    observaciones = models.TextField()

    def __str__(self):
        return f"Entrada {self.id} - {self.producto.nombre_producto}"


class SalidaProducto(models.Model):
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    cantidad_salida = models.IntegerField()
    fecha_salida = models.DateTimeField()
    destino = models.CharField(max_length=100)
    id_cliente_salida = models.IntegerField()
    num_pedido_salida = models.CharField(max_length=50)
    empleado_despacho = models.ForeignKey(EmpleadoAlmacen, on_delete=models.CASCADE)
    motivo_salida = models.TextField()

    def __str__(self):
        return f"Salida {self.id} - {self.producto.nombre_producto}"


class InventarioFisico(models.Model):
    fecha_inventario = models.DateField()
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    stock_sistema = models.IntegerField()
    stock_fisico = models.IntegerField()
    diferencia = models.IntegerField()
    empleado_realizo = models.ForeignKey(EmpleadoAlmacen, on_delete=models.CASCADE)
    comentarios = models.TextField()
    ultima_actualizacion = models.DateTimeField()

    def __str__(self):
        return f"Inventario {self.id} - {self.producto.nombre_producto}"
