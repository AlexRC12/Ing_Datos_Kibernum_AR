--Actividad 2 Módulo 4 Alex Riquelme

--1. Esquema de la base de datos
--Diseña un esquema con al menos cuatro tablas, relacionadas entre sí:
--Una tabla para clientes
--Una tabla para productos
--Una tabla para pedidos
--Una tabla para el detalle de pedidos (relación muchos a muchos)

-- Tabla Clientes
CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,     
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT
);

-- Tabla Productos
CREATE TABLE productos (
    producto_id SERIAL PRIMARY KEY,   
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0)
);

-- Tabla Pedidos
CREATE TABLE pedidos (
    pedido_id SERIAL PRIMARY KEY,      
    cliente_id INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

-- Tabla Detalle_Pedidos (muchos a muchos entre pedidos y productos)
CREATE TABLE detalle_pedidos (
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario >= 0),
    PRIMARY KEY (pedido_id, producto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);


--2. Inserción de datos
--Inserta al menos 3 clientes, 3 productos, 2 pedidos y sus respectivos detalles.
--Los datos deben ser realistas y variados.
-- Insertar clientes
INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('Alex Riquelme', 'alex.riquelme@gmail.com', '+56912345678', 'Concepción'),
('Luis Gómez', 'luis.gomez@gmail.com', '+56987654321', 'Calle Falsa 456, Valparaíso'),
('Marta Díaz', 'marta.diaz@gmail.com', '+56912345679', 'Pasaje Las Rosas 789, Concepción');

-- Insertar productos
INSERT INTO productos (nombre, descripcion, precio) VALUES
('Café Premium', 'Café 100% Arábica, tueste medio', 4500.00),
('Té Verde', 'Té verde orgánico, 100g', 3500.00),
('Chocolate Oscuro', 'Chocolate con 70% cacao', 5200.00);

-- Insertar pedidos
INSERT INTO pedidos (cliente_id, fecha, estado) VALUES
(1, '2025-07-01 10:30:00', 'Pendiente'),
(2, '2025-07-02 15:45:00', 'Enviado');

-- Insertar detalles de pedidos
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 2, 4500.00),    
(1, 3, 1, 5200.00),   
(2, 2, 3, 3500.00);    

--3. Creación de índices
--Crea al menos 2 índices en columnas que consideres claves para mejorar consultas.
--Justifica en qué tipo de consulta esperas mejor rendimiento.

-- Índice en cliente_id en pedidos
CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);

-- Índice en producto_id en detalle_pedidos 
CREATE INDEX idx_detalle_producto ON detalle_pedidos(producto_id);

--4. Creación de vistas
--Crea al menos una vista compleja que una 3 o más tablas con JOIN.
--La vista debe facilitar una consulta común para el área de ventas o reportes.

CREATE VIEW reporte AS
SELECT
    p.pedido_id,
    p.fecha,
    c.cliente_id,
    c.nombre AS cliente_nombre,
    pr.producto_id,
    pr.nombre AS producto_nombre,
    dp.cantidad,
    dp.precio_unitario,
    (dp.cantidad * dp.precio_unitario) AS total_linea,
    p.estado
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN detalle_pedidos dp ON p.pedido_id = dp.pedido_id
JOIN productos pr ON dp.producto_id = pr.producto_id;


--5. Optimización y análisis de consulta
--Escribe una consulta que recupere información relevante desde la vista.
--Evalúa su rendimiento con EXPLAIN ANALYZE.
--Escribe tu interpretación de los resultados (¿se usó índice?, ¿hay "Seq Scan"?).
--R: Las tablas fueron leídas de forma secuencial (Seq Scan) ignorando los índices disponibles
EXPLAIN ANALYZE
SELECT
    cliente_nombre,
    estado,
    SUM(total_linea) AS total_venta
FROM reporte
GROUP BY cliente_nombre, estado
ORDER BY total_venta DESC;



