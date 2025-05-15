# Projeto de WebScrapping
---
## Objetivo do projeto
  Automatizar a coleta, organização e análise de dados públicos disponíveis no site da Codevasf (Companhia de Desenvolvimento dos Vales do São Francisco e do Parnaíba), visando construir um painel de transparência para apoiar auditorias e investigações conuzidas pelo TCU, evitando desvios de gastos públicos.
### 📁 Organização das pastas do projeto de extração de dados efetuados para o Tribunal de Contas da União
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
- **ChromeDriver**  
- **Excel** (como destino final de dados em algumas entregas)  
- **Power BI** (para dashboards analíticos, fora deste repositório)

---

## 🚀 Como Executar

 ### **Pré-requisitos**:
 > - Python 3.x instalado  
 > - Google Chrome instalado  
 > - ChromeDriver compatível com a versão do navegador  

1. Clone este repositório  
   ```bash
    git clone https://github.com/Sogayar/Codevasf.git
   ```

2. Instale os pacotes necessários:  
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script desejado
   ```
   python WebScrapingDoacoes_v3.2.4.py
   ```
   
---

## Autores
- Henrique Sogayar (Ciência da Computação)
- Eduardo Rabelo (Ciência da Computação)
- Pedro Eros (Estatística)

---
   
## ✅ Status do Projeto
 - 🔄 Em desenvolvimento contínuo — funcionalidades estão sendo ajustadas.

