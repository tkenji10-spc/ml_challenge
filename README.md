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


net-analyzer/
│
├── app/
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
├── requirements.txt
└── README.md