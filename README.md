# Projeto de WebScrapping
---
## Objetivo do projeto
  Automatizar a coleta, organização e análise de dados públicos disponíveis no site da Codevasf (Companhia de Desenvolvimento dos Vales do São Francisco e do Parnaíba), visando construir um painel de transparência para apoiar auditorias e investigações conduzidas pelo TCU, evitando desvios de gastos públicos.
### 📁 Organização das pastas do projeto.
   ```
Codevasf/
      ├── Códigos/
      │     ├── Extração_Doações/
      │     │   └── WebScrapingDoacoes_v3.2.4.py
      │     │
      │     ├── Extração_Instrumentos/
      │     │   └── WebScrapingContratos_v2.2.3.py
      │     │
      │     ├── Scripts_Analise/
      │     │   ├── Analisa_erros.py
      │     │   └── Extrator_link_empenhos.py
      │     │
      │     └── BotDeContratos.py
      │
      ├── Imagens
      │     └── PowerBI
      │          └── Parlamentar.png
      │
      └── README.md
```
---

## ⚙️ Funcionalidades

-  **Extração automatizada** de dados públicos de contratos, doações e instrumentos.
-  **Web scraping com Python e Selenium**, utilizando scripts separados por finalidade.
-  **Organização e padronização** dos dados coletados para posterior análise.
-  **Scripts auxiliares de análise**, incluindo verificação de erros e extração de links de empenhos.

---

## 🧰 Tecnologias Utilizadas

- **Python**   
    - **Selenium**  
    - **Pandas**   
- **Excel** (como destino final de dados)  
- **Power BI** (para dashboards analíticos, fora deste repositório)

---

## 🚀 Instruções para execução

 ### **Pré-requisitos**:
 >  - Python 3 instalado  
 >  - Google Chrome instalado  
 >  - ChromeDriver compatível com a versão do navegador
 >      - Caso não possua, instale em: https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br
 >  - Clone este repositório
 >  - Instale os pacotes necessários  

1. Clone este repositório  
   ```bash
    git clone https://github.com/Sogayar/Codevasf.git
   ```

2. Instale os pacotes necessários:  
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script desejado
   ```bash
   python WebScrapingDoacoes_v3.2.4.py
   ```
   
---

## 👥 Autoria
- **Henrique Sogayar** — Estudante de Ciência da Computação
- **Eduardo Rabelo** — Estudante de Ciência da Computação
- **Pedro Eros** — Estudante de Estatística

---
   
## ✅ Status do Projeto
 - 🔄 Em desenvolvimento.

