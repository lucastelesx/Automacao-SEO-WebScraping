# Automação de SEO Técnico & Web Scraping

Ferramenta modular de auditoria técnica de SEO desenvolvida em Python. Realiza requisições com resiliência de rede e valida tags e metadados essenciais de páginas web diretamente pelo terminal com visualização rica.

## Funcionalidades
- **Sessão Resiliente com Retry & Backoff**: Configuração de `requests.Session` com `urllib3.util.retry.Retry` para tolerância a falhas (códigos 429, 500, 502, 503, 504) e simulação de User-Agent.
- **Auditoria de Metadados Críticos**:
  - `title` e `meta[name='description']`
  - Canonical URL (`link[rel='canonical']`)
  - Hierarquia de cabeçalhos (`h1`, `h2`)
  - Diretivas de indexação (`meta[name='robots']`)
- **Processamento em Lote**: Leitura segura via context manager de arquivos contendo múltiplas URLs para auditoria (`urls_para_auditar.txt`).
- **Terminal com Syntax Highlighting**: Visualização com painéis, cores semânticas e syntax highlighting via biblioteca `Rich`.
- **Tratamento Defensivo de Exceções**: Isolamento de erros por domínio dentro do loop para evitar interrupção da esteira.

## Arquitetura do Projeto
```text
.
├── seo_scraper.py         # Ponto de entrada, gerenciamento de sessões HTTP e loop de auditoria
├── utils_seo.py           # Validações de seletores CSS, tipos de tags e extração de atributos
├── utils_view.py          # Formatação visual rica (painéis, logs coloridos e renderização HTML)
├── urls_para_auditar.txt  # Lista de URLs de entrada para a auditoria
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação da ferramenta
```

## Instalação e Execução

1. Clone o repositório:
```bash
git clone git@github.com:lucastelesx/automacaoSEOTecnico.git
cd automacaoSEOTecnico
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as URLs desejadas em `urls_para_auditar.txt` e execute:
```bash
python seo_scraper.py
```
