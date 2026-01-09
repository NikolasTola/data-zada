# Data-Zada

## Objetivo do Projeto

**Data-Zada** é uma solução completa de **Infrastructure as Code (IaC)** para provisionamento automatizado de ambientes de dados. O sistema permite que desenvolvedores e engenheiros de dados definam toda a infraestrutura necessária para trabalhar com dados através de arquivos de especificação, e com um único comando, o ambiente completo é criado, configurado e disponibilizado para uso.

A filosofia do projeto é: **"Defina uma vez, execute em qualquer lugar"**. Toda a complexidade de configuração, instalação e gerenciamento de infraestrutura de dados é abstraída em arquivos declarativos simples.

### Visão Geral

O Data-Zada é um framework extensível que, na sua primeira fase, foca em provisionamento de bancos de dados transacionais, mas está arquitetado para evoluir e suportar um ecossistema completo de dados, incluindo:

**Fase 1 (Atual): Bancos de Dados Transacionais**
- Criação automática de múltiplos databases
- Gestão de schemas e tabelas
- Configuração de extensões PostgreSQL
- Persistência de dados
- Geração de conexões por database

**Fases Futuras:**
- Data warehouses e data lakes
- Pipelines de ETL/ELT
- Ferramentas de BI e visualização
- APIs de dados automatizadas
- Catálogos de dados
- Governança e qualidade de dados
- Ambientes de machine learning

### Principais Funcionalidades (Fase 1)

- Provisionamento de múltiplos databases independentes via código
- Definição declarativa de databases e tabelas em arquivos YAML
- Organização automática de tabelas por database
- Criação seletiva de databases e tabelas (todos ou específicos)
- Configuração de extensões PostgreSQL por database
- Persistência garantida de dados entre execuções
- Geração automática de strings de conexão por database
- Validação de dependências e ambiente
- Compatibilidade multiplataforma (Windows e Linux)
- Arquitetura modular preparada para expansão
- CLI intuitivo com comando `zada`

---

## Casos de Uso

### Desenvolvimento Multi-Ambiente
- Configure rapidamente databases separados para dev, staging e produção
- Mantenha estruturas idênticas entre ambientes
- Elimine a necessidade de instalações manuais de bancos de dados
- Isole dados de diferentes ambientes no mesmo servidor

### Microserviços
- Crie databases isolados para cada microserviço
- Mantenha independência de dados entre serviços
- Facilite deploys independentes de cada serviço
- Garanta consistência de estrutura entre serviços

### Testes
- Crie databases limpos e isolados para cada suite de testes
- Reproduza ambientes de produção em ambiente de teste
- Automatize a criação de fixtures e dados de teste
- Execute testes paralelos com databases independentes

### Prototipagem
- Defina estruturas de dados rapidamente sem escrever SQL manual
- Itere sobre schemas de forma ágil
- Teste diferentes modelagens de dados facilmente
- Experimente com extensões PostgreSQL sem risco

### DevOps e CI/CD
- Integre a criação de ambientes em pipelines de CI/CD
- Garanta consistência entre ambientes (dev, staging, prod)
- Versione toda a infraestrutura de dados junto com o código da aplicação
- Automatize provisionamento em containers

### Documentação Viva
- Os arquivos YAML servem como documentação executável da estrutura de dados
- Mantenha a documentação sempre sincronizada com a realidade
- Facilite o onboarding de novos desenvolvedores
- Visualize dependências entre databases e tabelas

---

## Tecnologias Utilizadas

### PostgreSQL
**Banco de Dados Transacional**

PostgreSQL foi escolhido como banco de dados padrão para a primeira fase do projeto pelos seguintes motivos:

**Vantagens Técnicas:**
- Totalmente gratuito e open-source sem limitações
- ACID compliant, garantindo confiabilidade para dados críticos
- Suporte nativo excelente para Windows e Linux
- Recursos avançados: tipos JSON, arrays, tipos customizados, full-text search
- Extensibilidade através de extensões (PostGIS, pg_trgm, uuid-ossp, etc.)
- Performance robusta para cargas transacionais
- Suporte a múltiplos databases em uma única instância

**Vantagens Operacionais:**
- Imagem Docker oficial estável e mantida
- Comunidade ativa com vasta documentação
- Ferramentas maduras de backup e replicação
- Preparado para escalabilidade horizontal e vertical

**Alternativas Consideradas:**
- **MySQL**: Menos recursos avançados, preocupações com licenciamento Oracle
- **SQL Server**: Versão gratuita tem limitações significativas, suporte Linux inferior
- **SQLite**: Não adequado para ambientes multi-usuário ou produção

### Docker & Docker Compose
**Containerização e Orquestração**

Docker é a base da portabilidade e consistência do projeto:

**Benefícios:**
- **Isolamento completo**: Ambiente consistente independente da máquina host
- **Portabilidade total**: Comportamento idêntico em diferentes sistemas operacionais
- **Sem instalação manual**: Elimina complexidade de instalação de PostgreSQL
- **Volumes persistentes**: Garantem que dados não sejam perdidos entre execuções
- **Orquestração simples**: Docker Compose gerencia configurações complexas declarativamente
- **Reprodutibilidade**: Mesma versão e configuração em todos os ambientes
- **Gratuito e open-source**: Sem custos de licenciamento

### YAML
**Formato de Especificação**

YAML foi escolhido como formato padrão para definir especificações de recursos:

**Vantagens:**
- **Legibilidade superior**: Sintaxe limpa e intuitiva para humanos
- **Suporte a comentários**: Permite documentar especificações inline
- **Padrão de mercado**: Usado por Kubernetes, Ansible, Docker Compose, GitHub Actions
- **Menos verboso**: Significativamente mais conciso que JSON ou XML
- **Hierarquia clara**: Estruturas aninhadas são naturalmente visíveis através de indentação
- **Validação robusta**: Ferramentas maduras de validação e schema

**Alternativas Consideradas:**
- **JSON**: Menos legível, sem suporte a comentários, mais verboso
- **TOML**: Menos conhecido, estruturas aninhadas complexas ficam verbosas
- **XML**: Extremamente verboso, sintaxe pesada

### Python
**Linguagem de Implementação**

Python é a linguagem base do projeto por razões técnicas e práticas:

**Vantagens Técnicas:**
- Sintaxe limpa e expressiva, ideal para IaC
- Ecossistema rico de bibliotecas para todas as necessidades do projeto
- Tipagem opcional com type hints para código robusto
- Excepcional para automação e scripting

**Vantagens Operacionais:**
- Multiplataforma nativo (Windows, Linux, macOS)
- Comunidade massiva e ativa
- Curva de aprendizado suave para contribuidores
- Ferramentas de teste e qualidade maduras
- Totalmente gratuito e open-source

### Stack de Bibliotecas Python

#### SQLAlchemy
**ORM e Abstração de Banco de Dados**
- Permite criar schemas de forma programática
- Gera DDL (Data Definition Language) correto automaticamente
- Abstrai diferenças entre bancos de dados
- Suporte a migrações e versionamento de schema

#### Pydantic
**Validação de Dados e Schemas**
- Validação automática de arquivos YAML contra schemas definidos
- Garante integridade dos dados antes de executar operações
- Mensagens de erro claras e úteis
- Type safety em tempo de desenvolvimento

#### Click
**Framework para CLI (Command Line Interface)**
- Criação de interfaces de linha de comando profissionais
- Documentação automática de comandos
- Validação de argumentos e opções
- Suporte a comandos aninhados e grupos

#### PyYAML
**Parser de Arquivos YAML**
- Biblioteca padrão e confiável da comunidade Python
- Suporte completo à especificação YAML
- Performance adequada para arquivos de configuração

#### psycopg2
**Driver PostgreSQL**
- Conexão nativa e otimizada com PostgreSQL
- Suporte completo a recursos do PostgreSQL
- Performance superior a drivers genéricos
- Amplamente testado e estável

---

## Estrutura do Projeto

```
data-zada/
|
+-- infrastructure/                 # Recursos de infraestrutura
|   |
|   +-- docker/                     # Configurações de containers
|   |   +-- docker-compose.yml      # Definição do PostgreSQL
|   |   +-- .env.example            # Template de variáveis de ambiente
|   |
|   +-- specs/                      # Especificações de recursos
|       |
|       +-- databases/              # Especificações de databases
|       |   +-- app_producao.yaml
|       |   +-- app_desenvolvimento.yaml
|       |   +-- analytics.yaml
|       |
|       +-- tables/                 # Especificações de tabelas
|           |
|           +-- app_producao/       # Tabelas do database app_producao
|           |   +-- usuarios.yaml
|           |   +-- produtos.yaml
|           |   +-- pedidos.yaml
|           |
|           +-- app_desenvolvimento/ # Tabelas do database app_desenvolvimento
|           |   +-- usuarios.yaml
|           |   +-- produtos.yaml
|           |
|           +-- analytics/          # Tabelas do database analytics
|               +-- vendas_diarias.yaml
|               +-- metricas.yaml
|
+-- src/                            # Código fonte do sistema
|   |
|   +-- core/                       # Núcleo do sistema
|   |   +-- __init__.py
|   |   +-- config.py               # Gerenciamento de configurações
|   |   +-- constants.py            # Constantes do sistema
|   |
|   +-- database/                   # Módulo de banco de dados
|   |   +-- __init__.py
|   |   +-- connection.py           # Gerenciamento de conexões
|   |   +-- validator.py            # Validação de especificações
|   |   +-- generator.py            # Geração de DDL
|   |   +-- executor.py             # Execução no banco
|   |
|   +-- infrastructure/             # Módulo de infraestrutura
|   |   +-- __init__.py
|   |   +-- docker_manager.py       # Gerenciamento Docker
|   |   +-- dependency_checker.py   # Verificação de dependências
|   |
|   +-- cli/                        # Interface de linha de comando
|   |   +-- __init__.py
|   |   +-- commands.py             # Comandos CLI
|   |   +-- utils.py                # Utilitários CLI
|   |
|   +-- utils/                      # Utilitários gerais
|       +-- __init__.py
|       +-- logger.py               # Sistema de logs
|       +-- file_handler.py         # Manipulação de arquivos
|
+-- config/                         # Arquivos de configuração
|   +-- database.yaml               # Configurações do banco
|   +-- settings.yaml               # Configurações gerais
|
+-- logs/                           # Logs de execução
|   +-- .gitkeep
|
+-- tests/                          # Testes automatizados
|   +-- __init__.py
|   +-- test_validator.py
|   +-- test_generator.py
|
+-- configs.py                      # Versão, nome e constantes do projeto
+-- main.py                         # Ponto de entrada principal
+-- setup.py                        # Configuração de instalação
+-- requirements.txt                # Dependências Python
+-- .env.example                    # Exemplo de variáveis de ambiente
+-- .gitignore                      # Arquivos ignorados pelo Git
+-- README.md                       # Este arquivo
```

### Descrição dos Diretórios

**infrastructure/**
Contém todos os recursos de infraestrutura do projeto. Separado em:
- `docker/`: Configurações de containers e orquestração
- `specs/databases/`: Especificações declarativas de databases
- `specs/tables/`: Especificações de tabelas organizadas por database

**src/**
Código fonte Python organizado em módulos:
- `core/`: Funcionalidades centrais e configurações
- `database/`: Lógica específica de banco de dados
- `infrastructure/`: Gerenciamento de infraestrutura (Docker, dependências)
- `cli/`: Interface de linha de comando
- `utils/`: Utilitários reutilizáveis

**config/**
Arquivos de configuração em YAML para diferentes aspectos do sistema.

**logs/**
Histórico de execuções e logs do sistema.

**tests/**
Testes automatizados para garantir qualidade do código.

**configs.py**
Arquivo central com versão, nome e todas as constantes do projeto.

---

## Instalação

### Pré-requisitos

- **Python 3.8+**: Linguagem base do projeto
- **Docker**: Para containerização do PostgreSQL
- **Git**: Para controle de versão (recomendado)

### Passos de Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd data-zada
```

2. **Crie ambiente virtual Python:**
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale o Data-Zada:**
```bash
# Instala em modo desenvolvimento (recomendado)
pip install -e .

# Isso cria o comando 'zada' disponível globalmente
```

4. **Configure variáveis de ambiente:**
```bash
cp .env.example .env
# Edite .env com suas configurações
```

5. **Verifique a instalação:**
```bash
zada --help
```

---

## Comandos Disponíveis

### Comando Principal

```bash
# Executa o processo completo: valida, configura e cria tudo
zada setup
```

### Gerenciamento de Databases

```bash
# Criar todos os databases definidos
zada database create

# Criar um database específico
zada database create --name app_producao

# Listar databases definidos nas specs
zada database list

# Ver informações de um database
zada database info --name app_producao

# Deletar um database (cuidado!)
zada database delete --name app_producao
```

### Gerenciamento de Tabelas

```bash
# Criar todas as tabelas de todos os databases
zada apply

# Criar todas as tabelas de um database específico
zada apply --database app_producao

# Criar apenas uma tabela específica
zada apply --database app_producao --table usuarios

# Listar todas as tabelas definidas
zada table list

# Listar tabelas de um database específico
zada table list --database app_producao
```

### Informações e Conexão

```bash
# Ver string de conexão de todos os databases
zada connection-string

# Ver string de conexão de um database específico
zada connection-string --database app_producao

# Verificar status do ambiente
zada status

# Verificar status de um database específico
zada status --database app_producao

# Informações sobre o projeto
zada info
```

### Validação

```bash
# Validar todas as specs sem executar
zada validate

# Validar specs de um database específico
zada validate --database app_producao

# Validar apenas uma tabela
zada validate --database app_producao --table usuarios
```

### Operações Destrutivas

```bash
# Remover containers (preserva dados em volumes)
zada destroy

# Remover containers E volumes (PERDA DE DADOS)
zada destroy --volumes

# Remover apenas um database
zada database delete --name app_producao
```

### Opções Globais

```bash
# Modo verboso (logs detalhados)
zada --verbose <comando>

# Modo silencioso (apenas erros)
zada --quiet <comando>

# Simular execução (dry-run)
zada --dry-run <comando>

# Pular verificação do Docker
zada --skip-docker-check <comando>

# Ajuda
zada --help
zada <comando> --help
```

---

## Especificações

### Especificação de Database

```yaml
# infrastructure/specs/databases/app_producao.yaml

database:
  name: app_producao
  description: Database principal da aplicação em produção
  owner: postgres
  encoding: UTF8
  locale: pt_BR.UTF-8
  template: template0
  
connection:
  host: localhost
  port: 5432
  user: postgres
  password: ${DB_PASSWORD}  # Variável de ambiente
  
settings:
  max_connections: 100
  shared_buffers: 256MB
  work_mem: 4MB
  maintenance_work_mem: 64MB
  timezone: America/Sao_Paulo
  
extensions:
  - pg_trgm          # Busca de texto com trigrams
  - uuid-ossp        # Geração de UUIDs
  - pgcrypto         # Funções de criptografia
  - unaccent         # Remoção de acentos
  
backup:
  enabled: true
  schedule: daily
  retention_days: 30
  
metadata:
  team: backend
  environment: production
  cost_center: engineering
```

### Especificação de Tabela

```yaml
# infrastructure/specs/tables/app_producao/usuarios.yaml

table:
  name: usuarios
  database: app_producao      # Referência ao database
  schema: public
  description: Tabela de usuários do sistema
  
columns:
  - name: id
    type: integer
    primary_key: true
    auto_increment: true
    description: Identificador único do usuário
    
  - name: uuid
    type: uuid
    nullable: false
    unique: true
    default: uuid_generate_v4()
    description: Identificador público do usuário
    
  - name: email
    type: varchar
    length: 255
    nullable: false
    unique: true
    description: Email do usuário (usado para login)
    
  - name: nome
    type: varchar
    length: 100
    nullable: false
    description: Nome completo do usuário
    
  - name: data_nascimento
    type: date
    nullable: true
    description: Data de nascimento do usuário
    
  - name: cpf
    type: varchar
    length: 11
    nullable: true
    unique: true
    description: CPF do usuário (apenas números)
    
  - name: senha_hash
    type: varchar
    length: 255
    nullable: false
    description: Hash da senha do usuário
    
  - name: ativo
    type: boolean
    default: true
    nullable: false
    description: Indica se o usuário está ativo no sistema
    
  - name: email_verificado
    type: boolean
    default: false
    nullable: false
    description: Indica se o email foi verificado
    
  - name: data_cadastro
    type: timestamp
    default: now()
    nullable: false
    description: Data e hora do cadastro
    
  - name: data_atualizacao
    type: timestamp
    default: now()
    nullable: false
    description: Data e hora da última atualização

indexes:
  - name: idx_usuarios_email
    columns: [email]
    type: btree
    unique: true
    description: Índice único para busca rápida por email
    
  - name: idx_usuarios_cpf
    columns: [cpf]
    type: btree
    unique: true
    description: Índice único para busca rápida por CPF
    
  - name: idx_usuarios_uuid
    columns: [uuid]
    type: btree
    unique: true
    description: Índice único para busca por UUID
    
  - name: idx_usuarios_data_cadastro
    columns: [data_cadastro]
    type: btree
    description: Índice para ordenação por data de cadastro
    
  - name: idx_usuarios_ativo
    columns: [ativo]
    type: btree
    description: Índice para filtrar usuários ativos

constraints:
  - name: chk_email_formato
    type: check
    condition: "email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}$'"
    description: Valida formato básico de email
    
  - name: chk_cpf_tamanho
    type: check
    condition: "cpf IS NULL OR length(cpf) = 11"
    description: Garante que CPF tem 11 dígitos quando preenchido
    
  - name: chk_data_nascimento_valida
    type: check
    condition: "data_nascimento IS NULL OR data_nascimento < CURRENT_DATE"
    description: Garante que data de nascimento está no passado

foreign_keys:
  - name: fk_usuarios_perfil
    columns: [perfil_id]
    references:
      table: perfis
      columns: [id]
    on_delete: restrict
    on_update: cascade

metadata:
  owner: backend_team
  sensitivity: high
  pii: true
```

---

## Fluxo de Trabalho

### 1. Criando um Novo Database

```bash
# 1. Criar arquivo de especificação
# Crie: infrastructure/specs/databases/meu_projeto.yaml

# 2. Definir configurações do database no YAML

# 3. Validar especificação
zada validate --database meu_projeto

# 4. Criar o database
zada database create --name meu_projeto

# 5. Verificar se foi criado
zada status --database meu_projeto
```

### 2. Criando Tabelas

```bash
# 1. Criar pasta para as tabelas do database
mkdir -p infrastructure/specs/tables/meu_projeto

# 2. Criar arquivo de especificação da tabela
# Crie: infrastructure/specs/tables/meu_projeto/usuarios.yaml

# 3. Definir estrutura da tabela no YAML
# Importante: especificar database: meu_projeto no YAML

# 4. Validar especificação
zada validate --database meu_projeto --table usuarios

# 5. Criar a tabela
zada apply --database meu_projeto --table usuarios

# 6. Verificar criação
zada table list --database meu_projeto
```

### 3. Setup Completo de um Projeto

```bash
# Criar todas as specs YAML necessárias, então:

# 1. Criar todos os databases
zada database create

# 2. Criar todas as tabelas
zada apply

# 3. Obter strings de conexão
zada connection-string

# 4. Verificar status geral
zada status
```

---

## String de Conexão

Após criar um database, o sistema fornece a string de conexão no formato padrão PostgreSQL:

```
postgresql://postgres:senha_segura@localhost:5432/app_producao
```

### Obtendo Strings de Conexão

```bash
# Todas as strings de conexão
zada connection-string

# Output:
# app_producao: postgresql://postgres:senha@localhost:5432/app_producao
# app_desenvolvimento: postgresql://postgres:senha@localhost:5432/app_desenvolvimento
# analytics: postgresql://postgres:senha@localhost:5432/analytics

# String de um database específico
zada connection-string --database app_producao

# Output:
# postgresql://postgres:senha@localhost:5432/app_producao
```

### Usando em Aplicações

**Python com SQLAlchemy:**
```python
from sqlalchemy import create_engine

connection_string = "postgresql://postgres:senha@localhost:5432/app_producao"
engine = create_engine(connection_string)
```

**Python com psycopg2:**
```python
import psycopg2

conn = psycopg2.connect("postgresql://postgres:senha@localhost:5432/app_producao")
```

**Node.js com pg:**
```javascript
const { Pool } = require('pg');
const pool = new Pool({
  connectionString: 'postgresql://postgres:senha@localhost:5432/app_producao'
});
```

---

## Validações do Sistema

O Data-Zada implementa validações robustas em múltiplas camadas:

### Validações de Database

- Nome do database é válido (sem caracteres especiais)
- Encoding especificado é suportado pelo PostgreSQL
- Extensões solicitadas existem e podem ser instaladas
- Porta especificada está disponível
- Credenciais são válidas

### Validações de Tabela

- Nome da tabela referencia um database existente
- Pasta da tabela corresponde ao database especificado
- Tipos de dados são válidos para PostgreSQL
- Constraints têm sintaxe SQL correta
- Foreign keys referenciam tabelas existentes
- Índices não são duplicados
- Primary key está definida

### Validações de Organização

- Arquivo YAML está na pasta correta: `tables/{database}/{tabela}.yaml`
- Campo `database` no YAML corresponde à pasta
- Não há tabelas duplicadas no mesmo database
- Specs YAML têm sintaxe válida

### Exemplo de Erro de Validação

```bash
zada validate --database app_producao --table usuarios

# Output:
ERRO: Validação falhou para usuarios.yaml

1. Campo 'database' não corresponde à pasta
   - Esperado: app_producao
   - Encontrado: app_desenvolvimento
   
2. Tipo de dados inválido na coluna 'cpf'
   - Tipo: varchar2
   - Tipos válidos: varchar, char, text, integer, bigint, ...

3. Foreign key referencia tabela inexistente
   - Tabela: perfis
   - Database: app_producao
   - Status: Não encontrada
```

---

## Persistência de Dados

Os dados são armazenados em **volumes Docker persistentes**, garantindo:

- Dados persistem entre reinicializações do container
- Dados sobrevivem a recriações do ambiente (exceto se usar --volumes)
- Cada database tem seu próprio volume isolado
- Backup pode ser feito através de dump do PostgreSQL ou cópia do volume
- Isolamento completo entre diferentes databases

### Gerenciamento de Volumes

```bash
# Listar volumes Docker
docker volume ls

# Inspecionar volume específico de um database
docker volume inspect data-zada_app_producao

# Backup de um database
docker exec data-zada-postgres pg_dump -U postgres app_producao > backup_app_producao.sql

# Restauração de um database
docker exec -i data-zada-postgres psql -U postgres app_producao < backup_app_producao.sql

# Backup de todos os databases
docker exec data-zada-postgres pg_dumpall -U postgres > backup_all.sql
```

---

## Controle de Versão

A estrutura de databases e tabelas é versionada através dos arquivos YAML no Git, seguindo o princípio de "Infrastructure as Code":

### Fluxo de Trabalho com Git

1. **Criar nova feature**: Edite specs YAML
2. **Validar localmente**: `zada validate`
3. **Commit das mudanças**: `git add . && git commit -m "Add tabela pedidos"`
4. **Push para repositório**: `git push origin main`
5. **Deploy em outro ambiente**: Clone o repo e execute `zada setup`

### Organizando Branches

```bash
# Branch para desenvolvimento
git checkout -b feature/add-analytics-database

# Adicionar specs do novo database
# Commit e push

# Após aprovação, merge para main
git checkout main
git merge feature/add-analytics-database
```

### Importante sobre Fase 1

Na primeira fase do projeto, o sistema **apenas cria databases e tabelas novas**. Modificações em estruturas existentes (ALTER TABLE, ALTER DATABASE) não são suportadas automaticamente e requerem:

- Intervenção manual via SQL
- Ou aguardar implementação em fases futuras (sistema de migrações)

### Boas Práticas

- Sempre versione specs junto com código da aplicação
- Use branches para testar mudanças estruturais
- Documente motivos de mudanças nos commits
- Mantenha histórico de specs antigas para referência
- Use tags do Git para marcar releases importantes
- Nunca versione arquivos `.env` com credenciais

---

## Arquitetura Técnica

### Princípios de Design

O projeto segue princípios sólidos de engenharia de software:

**Modularidade**
- Cada módulo tem responsabilidade única e bem definida
- Acoplamento baixo entre módulos
- Coesão alta dentro de cada módulo

**Extensibilidade**
- Arquitetura preparada para adicionar novos tipos de recursos
- Padrões de design que facilitam extensão sem modificação
- Plugins e hooks para customização

**Testabilidade**
- Código organizado para facilitar testes unitários
- Injeção de dependências onde apropriado
- Separação clara entre lógica e infraestrutura

**Manutenibilidade**
- Código limpo seguindo PEP 8
- Documentação inline onde necessário
- Nomes descritivos e convenções consistentes

### Fluxo de Execução

```
1. Usuário executa: zada database create --name meu_db

2. CLI (commands.py) recebe o comando

3. configs.py fornece constantes e configurações

4. dependency_checker verifica se Docker está instalado

5. docker_manager verifica se containers estão rodando

6. file_handler lê spec YAML de infrastructure/specs/databases/meu_db.yaml

7. validator valida spec contra schema Pydantic

8. connection estabelece conexão com PostgreSQL (database postgres)

9. executor executa CREATE DATABASE meu_db

10. executor instala extensões especificadas

11. logger registra todas as operações

12. CLI exibe resultado e connection string


Então o usuário executa: zada apply --database meu_db

1. file_handler lê todos os YAMLs de infrastructure/specs/tables/meu_db/

2. validator valida cada spec de tabela

3. validator verifica se database: meu_db corresponde à pasta

4. generator converte specs em DDL SQLAlchemy

5. connection estabelece conexão com meu_db

6. executor aplica DDL no database correto

7. executor cria índices e constraints

8. logger registra operações

9. CLI exibe resumo de tabelas criadas
```

### Tratamento de Erros

O sistema implementa tratamento robusto de erros em múltiplas camadas:

- **Validação**: Erros em specs YAML são detectados antes de execução
- **Conexão**: Falhas de conexão são tratadas com retry e timeout
- **Execução**: Erros SQL são capturados e logados com contexto
- **Rollback**: Operações são atômicas quando possível
- **Logs**: Todos os erros são registrados para diagnóstico

---

## Segurança

### Boas Práticas Implementadas

- Senhas e credenciais em variáveis de ambiente (nunca em código)
- Arquivo .env no .gitignore (nunca versionado)
- Validação de entrada para prevenir SQL injection
- Uso de prepared statements via SQLAlchemy
- Logs não expõem informações sensíveis
- Conexões são fechadas adequadamente após uso

### Recomendações

- Use senhas fortes para banco de dados
- Mude credenciais padrão em produção
- Restrinja acesso de rede ao PostgreSQL
- Considere criptografia de dados em repouso
- Implemente backup regular dos dados
- Use diferentes credenciais para cada ambiente
- Não compartilhe arquivos .env

---

## Performance

### Otimizações Implementadas

- Conexões com pool para reutilização
- Validação em memória antes de execução
- Operações em batch quando possível
- Índices sugeridos automaticamente para chaves
- Caching de especificações validadas
- Execução paralela quando seguro

### Monitoramento

O sistema registra métricas importantes:
- Tempo de execução de cada operação
- Tamanho dos volumes de dados
- Status de saúde dos containers
- Erros e warnings
- Número de conexões ativas

### Recomendações para Produção

- Configure adequadamente shared_buffers e work_mem
- Monitore uso de disco dos volumes
- Configure max_connections baseado na carga
- Implemente connection pooling na aplicação
- Use índices apropriados para suas queries
- Analise planos de execução de queries lentas

---

## Troubleshooting

### Docker não está instalado

```
ERRO: Docker não encontrado no sistema.

Solução:
- Windows: Instale Docker Desktop de https://www.docker.com/products/docker-desktop
- Linux Ubuntu/Debian: sudo apt-get install docker.io docker-compose
- Linux Fedora/RHEL: sudo dnf install docker docker-compose
- macOS: Instale Docker Desktop de https://www.docker.com/products/docker-desktop

Após instalar, verifique: docker --version
```

### Porta 5432 já está em uso

```
ERRO: Porta 5432 já está em uso por outro processo.

Solução:
1. Identifique o processo: 
   - Linux/macOS: sudo lsof -i :5432
   - Windows: netstat -ano | findstr :5432

2. Opções:
   a) Pare o processo que está usando a porta
   b) Mude a porta no infrastructure/docker/docker-compose.yml
      ports:
        - "5433:5432"  # Use porta 5433 no host
```

### Erro de permissão em volumes

```
ERRO: Permission denied ao criar volumes Docker.

Solução Linux:
1. Adicione seu usuário ao grupo docker:
   sudo usermod -aG docker $USER

2. Faça logout e login novamente

3. Ou execute com sudo (não recomendado):
   sudo zada setup
```

### Spec YAML inválido

```
ERRO: Arquivo usuarios.yaml possui erros de sintaxe.

Solução:
1. Verifique indentação (use espaços, não tabs)
2. Execute validação: zada validate --database meu_db --table usuarios
3. Corrija os erros apontados
4. Verifique se todas as chaves obrigatórias estão presentes

Ferramenta útil: https://www.yamllint.com/
```

### Database já existe

```
ERRO: Database 'app_producao' já existe.

Solução:
1. Se quer recriar, delete primeiro:
   zada database delete --name app_producao

2. Ou use o database existente:
   zada apply --database app_producao

3. Para forçar recriação (PERDA DE DADOS):
   zada database delete --name app_producao
   zada database create --name app_producao
```

### Tabela já existe

```
ERRO: Tabela 'usuarios' já existe no database 'app_producao'.

Solução:
1. Fase 1 não suporta ALTER TABLE
2. Opções:
   a) Delete a tabela manualmente: DROP TABLE usuarios;
   b) Use um nome diferente para a tabela
   c) Delete e recrie o database inteiro (PERDA DE DADOS)

Comando manual:
docker exec -it data-zada-postgres psql -U postgres app_producao -c "DROP TABLE usuarios;"
```

### Container não inicia

```
ERRO: Container PostgreSQL não está iniciando.

Solução:
1. Verifique logs do Docker:
   docker logs data-zada-postgres

2. Verifique se há problemas com volumes:
   docker volume ls
   docker volume inspect data-zada_postgres_data

3. Tente recriar o container:
   docker-compose -f infrastructure/docker/docker-compose.yml down
   docker-compose -f infrastructure/docker/docker-compose.yml up -d

4. Verifique recursos do sistema (memória, disco)
```

### Falha de conexão

```
ERRO: Não foi possível conectar ao PostgreSQL.

Solução:
1. Verifique se o container está rodando:
   docker ps

2. Verifique se o PostgreSQL está aceitando conexões:
   docker exec data-zada-postgres pg_isready

3. Verifique credenciais no .env

4. Aguarde alguns segundos (PostgreSQL pode estar inicializando)

5. Tente conectar manualmente:
   docker exec -it data-zada-postgres psql -U postgres
```

### Extensão não pode ser instalada

```
ERRO: Extensão 'postgis' não está disponível.

Solução:
1. Nem todas as extensões estão disponíveis por padrão
2. Para PostGIS, use imagem específica:
   Edite docker-compose.yml:
   image: postgis/postgis:15-3.3

3. Recrie o container:
   docker-compose down
   docker-compose up -d

4. Extensões comuns disponíveis por padrão:
   - pg_trgm
   - uuid-ossp
   - pgcrypto
   - unaccent
```

### Comando 'zada' não encontrado

```
ERRO: Command 'zada' not found.

Solução:
1. Certifique-se de ter instalado o projeto:
   pip install -e .

2. Verifique se está no ambiente virtual correto:
   which python
   which zada

3. Ative o ambiente virtual:
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

4. Reinstale se necessário:
   pip uninstall data-zada
   pip install -e .
```

---

## Exemplos Práticos

### Exemplo 1: Aplicação de E-commerce

```bash
# 1. Criar database de produção
# infrastructure/specs/databases/ecommerce_prod.yaml

# 2. Criar tabelas
mkdir -p infrastructure/specs/tables/ecommerce_prod

# Criar specs para:
# - usuarios.yaml
# - produtos.yaml
# - pedidos.yaml
# - itens_pedido.yaml
# - pagamentos.yaml

# 3. Provisionar tudo
zada database create --name ecommerce_prod
zada apply --database ecommerce_prod

# 4. Obter connection string
zada connection-string --database ecommerce_prod
```

### Exemplo 2: Múltiplos Ambientes

```bash
# Criar databases para diferentes ambientes
infrastructure/specs/databases/
  - app_dev.yaml
  - app_staging.yaml
  - app_prod.yaml

# Provisionar todos
zada database create

# Aplicar mesma estrutura em todos
zada apply

# Resultado: 3 databases isolados com estrutura idêntica
```

### Exemplo 3: Microserviços

```bash
# Databases separados por microserviço
infrastructure/specs/databases/
  - auth_service.yaml
  - user_service.yaml
  - payment_service.yaml
  - notification_service.yaml

# Cada um com suas tabelas
infrastructure/specs/tables/
  - auth_service/
      - sessions.yaml
      - tokens.yaml
  - user_service/
      - users.yaml
      - profiles.yaml
  - payment_service/
      - transactions.yaml
      - invoices.yaml

# Provisionar arquitetura completa
zada setup
```

---

## Glossário

**IaC (Infrastructure as Code)**
Prática de gerenciar infraestrutura através de código versionável e declarativo.

**DDL (Data Definition Language)**
Linguagem para definição de estruturas de banco de dados (CREATE, ALTER, DROP).

**DML (Data Manipulation Language)**
Linguagem para manipulação de dados (INSERT, UPDATE, DELETE, SELECT).

**ACID**
Propriedades de transações: Atomicidade, Consistência, Isolamento, Durabilidade.

**ORM (Object-Relational Mapping)**
Técnica de mapear objetos de programação para tabelas relacionais.

**Volume Docker**
Armazenamento persistente para containers Docker que sobrevive a recriações do container.

**Schema**
Namespace lógico que agrupa objetos de banco de dados dentro de um database.

**Spec (Specification)**
Arquivo YAML que define estrutura de um recurso de forma declarativa.

**Extension (Extensão)**
Módulo adicional do PostgreSQL que adiciona funcionalidades (ex: PostGIS para dados geográficos).

**Constraint (Restrição)**
Regra que limita os valores que podem ser inseridos em uma coluna (ex: CHECK, UNIQUE, NOT NULL).

**Foreign Key (Chave Estrangeira)**
Constraint que estabelece relacionamento entre tabelas, garantindo integridade referencial.

**Index (Índice)**
Estrutura de dados que melhora a velocidade de operações de consulta em uma tabela.

**Primary Key (Chave Primária)**
Coluna ou conjunto de colunas que identifica unicamente cada linha em uma tabela.

**Connection String**
String formatada contendo informações necessárias para conectar a um banco de dados.

**CLI (Command Line Interface)**
Interface de linha de comando para interagir com o sistema através de texto.

**Dry-run**
Simulação de execução sem aplicar mudanças reais, útil para verificar o que seria feito.

**Rollback**
Reverter uma transação ou operação, desfazendo mudanças realizadas.

---

## FAQ (Perguntas Frequentes)

**P: Posso usar o Data-Zada em produção?**
R: A Fase 1 é adequada para ambientes de desenvolvimento e teste. Para produção, considere:
- Implementar sistema de migrações
- Adicionar monitoramento robusto
- Configurar backups automatizados
- Implementar alta disponibilidade

**P: Como faço para alterar a estrutura de uma tabela existente?**
R: Na Fase 1, alterações em tabelas existentes requerem SQL manual. Use:
```bash
docker exec -it data-zada-postgres psql -U postgres database_name
# Execute seus comandos ALTER TABLE
```

**P: Posso usar outro banco de dados além do PostgreSQL?**
R: Atualmente apenas PostgreSQL é suportado. Suporte para MySQL e outros está planejado para fases futuras.

**P: Como faço backup dos meus dados?**
R: Use pg_dump para backup lógico ou copie os volumes Docker para backup físico. Veja seção "Persistência de Dados".

**P: Posso rodar múltiplas instâncias do PostgreSQL?**
R: Sim, mas cada uma precisa usar portas diferentes. Modifique o docker-compose.yml de acordo.

**P: O Data-Zada suporta replicação?**
R: Não nativamente na Fase 1. Configure replicação manualmente no PostgreSQL se necessário.

**P: Como compartilho specs com minha equipe?**
R: Versione os arquivos YAML no Git. Toda a equipe usa o mesmo repositório e executa `zada setup`.

**P: Posso usar variáveis de ambiente nas specs?**
R: Sim, use a sintaxe `${VARIAVEL}` nos arquivos YAML. Defina as variáveis no arquivo .env.

**P: Como testo minhas specs antes de aplicar?**
R: Use `zada validate` ou `zada --dry-run apply` para simular sem executar.

**P: O que acontece se eu executar 'apply' duas vezes?**
R: Tabelas que já existem não são recriadas. Você verá uma mensagem informando que já existem.

**P: Posso usar o Data-Zada com Docker Swarm ou Kubernetes?**
R: Atualmente usa Docker Compose. Para orquestradores, você precisará adaptar os manifestos.

**P: Como contribuo para o projeto?**
R: O projeto aceita contribuições! Veja o repositório no GitHub para guidelines.

---

## Suporte e Comunidade

### Obtendo Ajuda

- **GitHub Issues**: Reporte bugs ou solicite features
- **Documentação**: Consulte este README e a wiki do projeto
- **Logs**: Sempre verifique os logs em `logs/` para diagnóstico

### Reportando Bugs

Ao reportar um bug, inclua:
1. Versão do Data-Zada (`zada info`)
2. Sistema operacional
3. Versão do Python e Docker
4. Comando executado
5. Mensagem de erro completa
6. Logs relevantes

### Solicitando Features

Ao solicitar uma nova funcionalidade:
1. Descreva o caso de uso
2. Explique o benefício
3. Sugira uma implementação (opcional)
4. Indique se você pode contribuir com código

---

## Versionamento

O Data-Zada segue [Semantic Versioning](https://semver.org/):

- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Novas funcionalidades compatíveis
- **PATCH**: Correções de bugs

Versão atual: **1.0.0**

### Changelog

**1.0.0 (Fase 1)**
- Provisionamento de múltiplos databases
- Criação de tabelas via YAML
- Validação de specs
- CLI com comando `zada`
- Suporte a extensões PostgreSQL
- Persistência via volumes Docker
- Compatibilidade Windows e Linux