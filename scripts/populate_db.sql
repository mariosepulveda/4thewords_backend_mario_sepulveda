-- Crear la tabla si no existe
CREATE TABLE IF NOT EXISTS leyendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    provincia VARCHAR(255) NOT NULL,
    canton VARCHAR(255) NOT NULL,
    distrito VARCHAR(255) NOT NULL,
    imagen_url VARCHAR(255) NULL,
    categoria VARCHAR(100) NOT NULL

);



-- Insertar datos iniciales
INSERT INTO leyendas (nombre, descripcion, provincia, canton, distrito, imagen_url, categoria,fecha_creacion) VALUES
('La Llorona', 'Leyenda de una mujer que llora por sus hijos cerca de los ríos.', 'San José', 'San José', 'Carmen', 'https://ejemplo.com/llorona.jpg', 'Mitos urbanos','2024-03-01 00:00:00'),
('El Cadejos', 'Perro negro espectral que protege a los borrachos o castiga a los malvados.', 'Alajuela', 'Alajuela', 'San José', 'https://ejemplo.com/cadejos.jpg', 'Criaturas mágicas','2024-03-01 00:00:00'),
('La Segua', 'Mujer hermosa que se transforma en un espectro para castigar a los hombres infieles.', 'Cartago', 'Cartago', 'Oriental', 'https://ejemplo.com/segua.jpg', 'Fantasmas','2024-03-01 00:00:00'),
('El Duende', 'Pequeño ser travieso que esconde objetos y asusta a las personas en la noche.', 'Heredia', 'Heredia', 'San Francisco', 'https://ejemplo.com/duende.jpg', 'Seres míticos','2024-03-01 00:00:00'),
('La Tulevieja', 'Espíritu de una mujer con alas y pies de gallina que se lleva a los niños desobedientes.', 'Puntarenas', 'Puntarenas', 'Barranca', 'https://ejemplo.com/tulevieja.jpg', 'Brujas','2024-03-01 00:00:00'),
('La Carreta sin Bueyes', 'Carreta fantasma que se escucha en las noches, presagio de muerte.', 'Guanacaste', 'Liberia', 'Cañas Dulces', 'https://ejemplo.com/carreta.jpg', 'Fantasmas','2024-03-01 00:00:00'),
('El Padre sin Cabeza', 'Sacerdote decapitado que deambula por las iglesias en busca de redención.', 'Limón', 'Limón', 'Valle La Estrella', 'https://ejemplo.com/padresincabeza.jpg', 'Fantasmas','2024-03-01 00:00:00'),
('La Mona', 'Bruja que se convierte en un gran mono negro para asustar a la gente.', 'San José', 'Desamparados', 'San Rafael Abajo', 'https://ejemplo.com/mona.jpg', 'Brujas','2024-03-01 00:00:00'),
('El Gigante de Talamanca', 'Criatura mítica que protege los bosques y montañas de los invasores.', 'Limón', 'Talamanca', 'Bratsi', 'https://ejemplo.com/gigante.jpg', 'Criaturas mágicas','2024-03-01 00:00:00'),
('El Tesoro del Pirata Morgan', 'Se dice que el pirata Henry Morgan escondió un gran tesoro en las costas costarricenses.', 'Puntarenas', 'Quepos', 'Manuel Antonio', 'https://ejemplo.com/tesoro.jpg', 'Tesoros ocultos','2024-03-01 00:00:00');
  

