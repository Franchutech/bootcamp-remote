-- Verificar instalación
psql --version;

-- Conectarse como usuario postgres
sudo -u postgres psql;

-- Crear usuario personal
CREATE USER franchutech WITH PASSWORD 'SantanderWYF*pgSQL25';

-- Crear base de datos
CREATE DATABASE bootcamp_db OWNER franchutech;

-- Dar permisos
GRANT ALL PRIVILEGES ON DATABASE bootcamp_db TO franchutech;
