# Banking System API

Projeto educacional desenvolvido no curso Python com Flask da Rocketseat.

A aplicação implementa uma API para um sistema bancário com clientes Pessoa Física e Pessoa Jurídica. O projeto utiliza Flask, SQLite, organização baseada em MVC e testes unitários com pytest.

## Funcionalidades

- Criar usuários Pessoa Física
- Criar usuários Pessoa Jurídica
- Listar usuários por tipo
- Consultar extrato
- Realizar saques
- Aplicar limites diferentes de saque para Pessoa Física e Pessoa Jurídica
- Persistir os dados em SQLite
- Validar as controllers com testes unitários

## Regra de saque

Os clientes possuem limites diferentes:

```text
Pessoa Física: R$ 1.000,00
Pessoa Jurídica: R$ 5.000,00
```

O saque também depende do saldo disponível.

## Tecnologias

- Python 3.14.7
- Flask 3.1.3
- SQLite
- pytest 9.1.1

## Estrutura

```text
banking-system-api/
│
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── usuario_controller.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   ├── pessoa_fisica.py
│   │   ├── pessoa_juridica.py
│   │   └── usuario_model.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   └── usuario_view.py
│   │
│   └── __init__.py
│
├── database/
│   ├── init_db.py
│   └── schema.sql
│
├── tests/
│   └── test_usuario_controller.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

O arquivo `database/banking.db` é criado localmente e não é versionado.

## MVC

A aplicação separa as responsabilidades em três partes principais.

### Model

Os models representam os clientes, regras de saque e acesso ao banco SQLite.

```text
app/models/
```

### Controller

A controller recebe as operações solicitadas pela API, valida os dados e coordena o acesso aos models.

```text
app/controllers/
```

### View

As views definem as rotas Flask e retornam as respostas HTTP da API.

```text
app/views/
```

## Banco de dados

O desafio fornece o SQL utilizado para criar e popular o banco SQLite.

As tabelas utilizadas são:

```text
pessoa_fisica
pessoa_juridica
```

Para criar o banco:

```powershell
python .\database\init_db.py
```

O arquivo será criado em:

```text
database/banking.db
```

## Instalação

Clone o repositório:

```powershell
git clone https://github.com/waldirevora/banking-system-api.git
```

Entre na pasta:

```powershell
cd banking-system-api
```

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Crie o banco:

```powershell
python .\database\init_db.py
```

## Executar a API

```powershell
python .\app.py
```

A aplicação será disponibilizada em:

```text
http://127.0.0.1:5000
```

## Endpoints

### Listar Pessoas Físicas

```http
GET /usuarios/fisica
```

### Listar Pessoas Jurídicas

```http
GET /usuarios/juridica
```

### Criar Pessoa Física

```http
POST /usuarios/fisica
```

Exemplo:

```json
{
  "renda_mensal": 7000,
  "idade": 32,
  "nome_completo": "Cliente Teste",
  "celular": "9999-0000",
  "email": "teste@exemplo.com",
  "categoria": "Categoria A",
  "saldo": 2000
}
```

### Criar Pessoa Jurídica

```http
POST /usuarios/juridica
```

Exemplo:

```json
{
  "faturamento": 100000,
  "idade": 5,
  "nome_fantasia": "Empresa Teste",
  "celular": "1111-2222",
  "email_corporativo": "contato@empresa.com",
  "categoria": "Categoria A",
  "saldo": 10000
}
```

### Realizar saque

Pessoa Física:

```http
POST /usuarios/fisica/{id}/saque
```

Pessoa Jurídica:

```http
POST /usuarios/juridica/{id}/saque
```

Corpo da requisição:

```json
{
  "valor": 500
}
```

### Consultar extrato

Pessoa Física:

```http
GET /usuarios/fisica/{id}/extrato
```

Pessoa Jurídica:

```http
GET /usuarios/juridica/{id}/extrato
```

## Testes

Execute:

```powershell
python -m pytest -v
```

Na validação final do projeto:

```text
7 passed
```

Os testes cobrem:

- listagem de usuários
- tratamento de tipo inválido
- criação de usuário
- rejeição de dados incompletos
- limite de saque para Pessoa Física
- saque de Pessoa Jurídica
- consulta de extrato

## Repositório

GitHub:

https://github.com/waldirevora/banking-system-api

## Autor

Waldir Évora

Projeto desenvolvido para fins educacionais no curso Python com Flask da Rocketseat.