# 🤖 Automação Selenium Kaggle: Estrutura Profissional

Este projeto demonstra como estruturar uma automação Web robusta utilizando **Python** e **Selenium**, focada no site **Kaggle**. A arquitetura utiliza o padrão **Page Object Model (POM)** para garantir código limpo e fácil manutenção.

## 📂 Estrutura do Projeto

```text
automacao_selenium_kaggle/
├── src/
│   ├── common/         # Configurações, logs e utilitários
│   ├── pages/          # Page Objects (Abstração da interface)
│   └── services/       # Serviços (Análise de dados com Pandas)
├── logs/               # Registros diários de execução
├── data/               # Dados do usuário e downloads
├── main.py             # Orquestrador principal da automação
├── .env                # Variáveis de ambiente (Segredos)
├── .gitignore          # Arquivos ignorados pelo Git
└── requirements.txt    # Dependências (Selenium, webdriver-manager)
```

## 🛠️ Principais Decisões Arquiteturais

- **Page Object Model (POM)**: Isolamos a lógica de interação com o navegador em classes específicas na pasta `pages`. Isso evita repetição de código e facilita atualizações se o site mudar.
- **Análise com Pandas**: Após o download robusto (com verificação de arquivos temporários), os dados são processados para gerar insights automáticos.
- **Logger Estruturado**: Sistema de logs que salva arquivos diários e exibe no console, essencial para auditoria de automações.
- **Configuração via .env**: Gestão segura de credenciais através de variáveis de ambiente.
- **Main Centralizado**: O arquivo `main.py` gerencia o ciclo de vida do WebDriver e orquestra as chamadas às páginas.

## 🚀 Como Executar

1.  **Prepare o ambiente:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    pip install -r requirements.txt
    ```

2.  **Configure suas credenciais:**
    - Crie um arquivo `.env` baseado no modelo `.env.example`.

3.  **Rode a automação:**
    ```bash
    python main.py
    ```

---
📫 **LinkedIn**: https://www.linkedin.com/in/carlos-eduardo-8aba2a21b/