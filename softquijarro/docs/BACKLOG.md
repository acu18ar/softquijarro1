# Product backlog — SoftQuijarro S.R.L.

> Generado desde `.github/backlog.json`. En GitHub cada historia es una **Issue**
> (pestaña *Issues*), agrupada por **Sprint** (milestone) y etiquetada por módulo.

## Clientes — carpeta `clientes/`

### C0 · Registrarme como responsable de Clientes  _(Sprint 1)_
**Como** integrante del equipo, **quiero** que el tablero muestre mi nombre como responsable de Clientes, **para** que el cliente sepa a quién preguntar.

- [ ] En clientes/apps.py, `responsable` tiene mi nombre
- [ ] El tablero muestra mi nombre en la tarjeta de Clientes
- [ ] Es mi primer pull request y está aprobado y fusionado (merge)

### C1 · Agregar teléfono y correo al cliente  _(Sprint 1)_
**Como** vendedor de la ferretería, **quiero** guardar el teléfono y el correo de cada cliente, **para** poder avisarle cuando llega su pedido.

- [ ] Los campos son opcionales (blank=True)
- [ ] La migración está incluida en el pull request
- [ ] Se ven en la lista de clientes y en el admin
- [ ] Los datos de prueba incluyen teléfonos de ejemplo

### C2 · Registrar un cliente desde el sistema  _(Sprint 2)_
**Como** vendedor, **quiero** registrar un cliente nuevo sin entrar al admin, **para** atenderlo rápido en el mostrador.

- [ ] Botón «Nuevo cliente» en la lista
- [ ] Nombre y NIT/CI son obligatorios; el formulario muestra los errores
- [ ] Al guardar vuelve a la lista con un mensaje de éxito

### C3 · Buscar cliente por nombre o NIT  _(Sprint 2)_
**Como** vendedor, **quiero** buscar un cliente escribiendo parte de su nombre o su NIT, **para** encontrarlo sin recorrer toda la lista.

- [ ] Caja de búsqueda sobre la lista
- [ ] Busca por nombre (sin importar mayúsculas) y por NIT
- [ ] Si no hay resultados lo dice

### C4 · No permitir NIT/CI repetido  _(Sprint 2)_
**Como** contador de la ferretería, **quiero** que no existan dos clientes con el mismo NIT/CI, **para** que las facturas no se mezclen.

- [ ] Al registrar un NIT existente aparece un mensaje claro
- [ ] Hay una prueba automática en clientes/tests.py que lo comprueba

### C5 · Editar los datos de un cliente  _(Sprint 3)_
**Como** vendedor, **quiero** corregir los datos de un cliente, **para** mantener la información al día.

- [ ] Cada fila de la lista tiene un botón «Editar»
- [ ] Se aplican las mismas validaciones que al registrar

## Productos — carpeta `productos/`

### P0 · Registrarme como responsable de Productos  _(Sprint 1)_
**Como** integrante del equipo, **quiero** que el tablero muestre mi nombre como responsable de Productos, **para** que el cliente sepa a quién preguntar.

- [ ] En productos/apps.py, `responsable` tiene mi nombre
- [ ] El tablero muestra mi nombre en la tarjeta de Productos
- [ ] Es mi primer pull request y está aprobado y fusionado (merge)

### P1 · Agregar código y stock mínimo al producto  _(Sprint 1)_
**Como** encargado de almacén, **quiero** que cada producto tenga un código y un stock mínimo, **para** identificarlo y saber cuándo reponerlo.

- [ ] `codigo` es opcional; `stock_minimo` tiene default 5
- [ ] La migración está incluida en el pull request
- [ ] Se ven en la lista y en el admin
- [ ] Los datos de prueba incluyen códigos

### P2 · Registrar y editar productos desde el sistema  _(Sprint 2)_
**Como** encargado de almacén, **quiero** registrar y editar productos sin entrar al admin, **para** mantener el catálogo al día.

- [ ] Botón «Nuevo producto» y botón «Editar» en cada fila
- [ ] El precio debe ser mayor a 0 (con mensaje de error)
- [ ] Mensaje de éxito al guardar

### P3 · Aviso de stock bajo  _(Sprint 2)_
**Como** encargado de almacén, **quiero** ver resaltados los productos con stock bajo, **para** pedirlos al proveedor a tiempo.

- [ ] Fila en rojo cuando stock ≤ stock mínimo
- [ ] Filtro «solo stock bajo»
- [ ] Prueba automática del filtro

### P4 · Buscar producto por nombre o código  _(Sprint 3)_
**Como** vendedor, **quiero** buscar un producto por nombre o código, **para** responder rápido si hay stock.

- [ ] Caja de búsqueda sobre la lista
- [ ] Busca sin importar mayúsculas

## Facturación — carpeta `facturacion/`

### F0 · Registrarme como responsable de Facturación  _(Sprint 1)_
**Como** integrante del equipo, **quiero** que el tablero muestre mi nombre como responsable de Facturación, **para** que el cliente sepa a quién preguntar.

- [ ] En facturacion/apps.py, `responsable` tiene mi nombre
- [ ] El tablero muestra mi nombre en la tarjeta de Facturación
- [ ] Es mi primer pull request y está aprobado y fusionado (merge)

### F1 · Ver el detalle de una factura  _(Sprint 1)_
**Como** vendedor, **quiero** abrir una factura y ver sus líneas, **para** responder consultas del cliente.

- [ ] Cada factura de la lista lleva a /facturacion/<número>/
- [ ] Muestra cliente, NIT, fecha, cada producto con cantidad, precio y subtotal, y el total

### F2 · Emitir una factura  _(Sprint 2)_
**Como** vendedor, **quiero** emitir una factura eligiendo cliente, productos y cantidades, **para** registrar la venta.

- [ ] Botón «Nueva factura»
- [ ] Se elige el cliente y al menos un producto con su cantidad
- [ ] El precio unitario se toma del producto
- [ ] El total se calcula solo y se guarda
- [ ] Al terminar muestra el detalle de la factura emitida

### F3 · Descontar stock al facturar  _(Sprint 3)_
**Como** encargado de almacén, **quiero** que cada venta descuente el stock, **para** que el inventario sea real.

- [ ] Al emitir, el stock de cada producto baja en la cantidad vendida
- [ ] No se puede vender más de lo que hay (mensaje claro, no se guarda nada)
- [ ] Prueba automática en facturacion/tests.py

## Proveedores — carpeta `proveedores/`

### V0 · Registrarme como responsable de Proveedores  _(Sprint 1)_
**Como** integrante del equipo, **quiero** que el tablero muestre mi nombre como responsable de Proveedores, **para** que el cliente sepa a quién preguntar.

- [ ] En proveedores/apps.py, `responsable` tiene mi nombre
- [ ] El tablero muestra mi nombre en la tarjeta de Proveedores
- [ ] Es mi primer pull request y está aprobado y fusionado (merge)

### V1 · Datos del proveedor y productos que surte  _(Sprint 1)_
**Como** encargado de compras, **quiero** guardar NIT y correo del proveedor y qué productos surte, **para** saber a quién pedir cada cosa.

- [ ] Campos `nit` y `correo` opcionales
- [ ] Relación muchos-a-muchos con productos.Producto definida en proveedores/models.py
- [ ] La migración está incluida
- [ ] Los datos de prueba asignan productos a cada proveedor

### V2 · Registrar y editar proveedores desde el sistema  _(Sprint 2)_
**Como** encargado de compras, **quiero** registrar y editar proveedores eligiendo los productos que surten, **para** no depender del admin.

- [ ] Botón «Nuevo proveedor» y «Editar»
- [ ] Se pueden marcar varios productos
- [ ] Mensaje de éxito al guardar

### V3 · Ficha del proveedor  _(Sprint 3)_
**Como** encargado de compras, **quiero** ver la ficha de un proveedor con sus productos y el stock actual, **para** decidir qué pedirle.

- [ ] Página /proveedores/<id>/
- [ ] Lista los productos que surte con su stock actual

## Reportes — carpeta `reportes/`

### R0 · Registrarme como responsable de Reportes  _(Sprint 1)_
**Como** integrante del equipo, **quiero** que el tablero muestre mi nombre como responsable de Reportes, **para** que el cliente sepa a quién preguntar.

- [ ] En reportes/apps.py, `responsable` tiene mi nombre
- [ ] El tablero muestra mi nombre en la tarjeta de Reportes
- [ ] Es mi primer pull request y está aprobado y fusionado (merge)

### R1 · Ventas de hoy y de los últimos 7 días  _(Sprint 1)_
**Como** dueño de la ferretería, **quiero** ver cuánto se vendió hoy y en la última semana, **para** saber cómo va el negocio.

- [ ] Cantidad de facturas y monto de hoy
- [ ] Cantidad de facturas y monto de los últimos 7 días

### R2 · Top 5 productos más vendidos  _(Sprint 2)_
**Como** dueño, **quiero** ver los 5 productos que más se venden, **para** no quedarme sin ellos.

- [ ] Tabla con producto, unidades vendidas e importe
- [ ] Ordenada de mayor a menor
- [ ] Prueba automática con datos conocidos

### R3 · Top 5 clientes frecuentes  _(Sprint 2)_
**Como** dueño, **quiero** ver los 5 clientes que más compran, **para** ofrecerles descuentos.

- [ ] Tabla con cliente, cantidad de facturas y monto total
- [ ] Ordenada por monto

### R4 · Filtrar reportes por fechas  _(Sprint 3)_
**Como** dueño, **quiero** elegir un rango de fechas, **para** comparar semanas.

- [ ] Campos «desde» y «hasta»
- [ ] Los reportes R2 y R3 respetan el rango
