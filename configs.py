"""
Configurações centrais do Data-Zada
Contém versão, nome e todas as constantes do projeto
"""

# Informações do Projeto
PROJECT_NAME = "Data-Zada"
PROJECT_VERSION = "1.0.0"
PROJECT_DESCRIPTION = "Data Infrastructure as Code"

# Paths do Projeto
INFRASTRUCTURE_DIR = "infrastructure"
SPECS_DIR = "infrastructure/specs"
DATABASES_SPECS_DIR = "infrastructure/specs/databases"
TABLES_SPECS_DIR = "infrastructure/specs/tables"
DOCKER_DIR = "infrastructure/docker"
CONFIG_DIR = "config"
LOGS_DIR = "logs"

# Configurações do Docker
DOCKER_COMPOSE_FILE = "infrastructure/docker/docker-compose.yml"
CONTAINER_NAME = "data-zada-postgres"
DEFAULT_POSTGRES_PORT = 5432
DEFAULT_POSTGRES_USER = "postgres"
DEFAULT_POSTGRES_PASSWORD = "postgres"

# Configurações de Database
DEFAULT_ENCODING = "UTF8"
DEFAULT_LOCALE = "pt_BR.UTF-8"
DEFAULT_TEMPLATE = "template0"

# Extensões PostgreSQL Comuns
COMMON_EXTENSIONS = [
    "pg_trgm",
    "uuid-ossp",
    "pgcrypto",
    "unaccent"
]

# Tipos de Dados PostgreSQL Suportados
SUPPORTED_DATA_TYPES = [
    "integer",
    "bigint",
    "smallint",
    "serial",
    "bigserial",
    "numeric",
    "decimal",
    "real",
    "double precision",
    "varchar",
    "char",
    "text",
    "boolean",
    "date",
    "timestamp",
    "timestamptz",
    "time",
    "timetz",
    "interval",
    "uuid",
    "json",
    "jsonb",
    "bytea",
    "array"
]

# Tipos de Índices Suportados
SUPPORTED_INDEX_TYPES = [
    "btree",
    "hash",
    "gist",
    "gin",
    "brin"
]

# Tipos de Constraints Suportados
SUPPORTED_CONSTRAINT_TYPES = [
    "check",
    "unique",
    "primary_key",
    "foreign_key",
    "not_null"
]

# Configurações de Logging
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FILE_NAME = "data-zada.log"

# Mensagens do Sistema
MSG_SUCCESS = "Operação concluída com sucesso"
MSG_ERROR = "Erro na operação"
MSG_WARNING = "Atenção"
MSG_INFO = "Informação"

# Códigos de Saída
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_VALIDATION_ERROR = 2
EXIT_DOCKER_ERROR = 3
EXIT_DATABASE_ERROR = 4