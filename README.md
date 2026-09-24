# Net-Analyzer (Network Traffic Analyzer)

Aplicação desenvolvida em Python para captura e análise de tráfego de rede em tempo real.

## Funcionalidades

- Captura de pacotes de rede
- Detecção automática da interface ativa
- Armazenamento dos dados em SQLite
- Estatísticas de protocolos (TCP, UDP, ICMP e Outros)
- Exibição dos IPs de origem e destino mais frequentes
- Dashboard Web utilizando Flask
- Controle da captura através de botões

## Tecnologias Utilizadas

- Python 3.11
- Scapy
- Flask
- SQLAlchemy
- SQLite
- Docker 

## Estrutura do Projeto

```text
net-analyzer/
│
├── app/
│   ├── __init__.py
│   ├── capture.py
│   ├── database.py
│   ├── models.py
│   ├── stats.py
│   └── main.py
│
├── web/
│   ├── dashboard.py
│   └── templates/
│       └── index.html
│
├── db/
│   └── packets.db
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Pré-requisitos
 
Antes de executar a aplicação, certifique-se de possuir:
 
- Python 3.11 ou superior
- Pip
- Git
- Docker (opcional)
- Docker Compose (opcional)
 
Verificar a versão do Python:
 
```bash
python --version
```
 
---
 
## Instalação
 
### 1. Clonar o Repositório
 
```bash
git clone https://github.com/tkenji10-spc/ml_challenge.git
```
 
```bash
cd ml_challenge
```
 
---
 
### 2. Criar Ambiente Virtual
 
#### Windows
 
```powershell
python -m venv venv
```
 
#### macOS/Linux
 
```bash
python3 -m venv venv
```
 
---
 
### 3. Ativar Ambiente Virtual
 
#### Windows
 
```powershell
venv\Scripts\activate
```
 
#### macOS/Linux
 
```bash
source venv/bin/activate
```
 
---
 
### 4. Instalar Dependências
 
```bash
pip install -r requirements.txt
```
 
---
 
## Executando a Aplicação
 
### Windows
 
> Importante: Execute o Prompt de Comando ou PowerShell como Administrador.
 
```powershell
python web/dashboard.py
```
 
### macOS
 
```bash
sudo -E $(which python) web/dashboard.py
```
 
---
 
## Acessando o Dashboard
 
Abra o navegador e acesse:
 
```text
http://localhost:5001
```
 
---
 
## Como Utilizar
 
### Iniciar Captura
 
1. Clique em **Iniciar Captura**
2. O sistema limpará automaticamente os dados da captura anterior
3. A captura será iniciada utilizando a interface de rede ativa
 
### Gerar Tráfego
 
Após iniciar a captura:
 
- Navegue na internet
- Abra sites como Google, YouTube ou Microsoft
- Execute comandos como:
 
```bash
ping 8.8.8.8
```
 
### Consultar Estatísticas
 
O dashboard exibirá:
 
- Total de pacotes capturados
- Protocolos identificados
- Top 5 IPs de origem
- Top 5 IPs de destino
 
### Parar Captura
 
Clique em:
 
```text
Parar Captura
```
 
Os dados permanecerão disponíveis para consulta até o início de uma nova captura.
 
---
 
## Estatísticas Disponíveis
 
### Protocolos
 
- TCP
- UDP
- ICMP
- OTHER
 
### Informações Exibidas
 
- Total de pacotes
- Quantidade por protocolo
- Top 5 IPs de origem
- Top 5 IPs de destino
 
---
 
## Banco de Dados
 
O sistema utiliza SQLite para armazenamento local.
 
Arquivo de banco de dados:
 
```text
db/packets.db
```
 
Observação:
 
Ao iniciar uma nova captura, os registros anteriores são removidos automaticamente para evitar crescimento excessivo do banco de dados.
 
---
 
## Execução com Docker
 
### Construir a Imagem
 
```bash
docker compose build
```
 
### Iniciar os Containers
 
```bash
docker compose up
```
 
### Executar em Segundo Plano
 
```bash
docker compose up -d
```
 
### Encerrar os Containers
 
```bash
docker compose down
```
 
---
 
## Possíveis Problemas
 
### Permissão Negada Durante a Captura
 
#### Windows
 
Execute o terminal como Administrador.
 
#### macOS
 
Execute:
 
```bash
sudo -E $(which python) web/dashboard.py
```
 
---
 
### Porta 5001 em Uso
 
Altere a porta em:
 
```python
web/dashboard.py
```
 
Exemplo:
 
```python
app.run(
host="0.0.0.0",
port=5002,
debug=False
)
```
 
---
 
### Dependências Não Instaladas
 
Execute novamente:
 
```bash
pip install -r requirements.txt
```
 
 
---
 
## Autor
 
**Thiago Kenji Hashizume de Gregorio**
 
