# BD_Codevasf
### Organização do Banco de Dados das informações e relatórios da CODEVASF para o Tribunal de Contas da União 

## 1. Introdução
### Objetivo do Documento
Este documento fornece uma visão detalhada do esquema do banco de dados e do entendimento por completo do projeto, visando facilitar em caso de manutenção.

### Descrição do Projeto
O banco de dados é projetado para organizar e facilitar o uso de querys para auditoria e transparência do Tribunal de Contas da União

## 2. Visão Geral do Banco de Dados
### Diagrama ER
(Insira o diagrama ER aqui)

### Resumo das Tabelas
(Descreva cada tabela)

## 3. Descrição das Tabelas

### Contratos
**Descrição:** Armazena informações sobre contratos.

| Coluna           | Tipo de Dados | Restrições             | Descrição                     |
|------------------|---------------|------------------------|-------------------------------|
| ID_Contrato      | UUID          | PRIMARY KEY            | Identificador único do contrato |
| Numero_Contrato  | VARCHAR       | NOT NULL               | Número do contrato             |
| Data_Publicacao  | DATE          | NOT NULL               | Data de publicação do contrato |
| Objeto           | TEXT          |                        | Descrição do objeto do contrato|
| Valor_Total      | DECIMAL       |                        | Valor total do contrato        |

### Ordem_de_Serviço
...

## 4. Relacionamentos entre Tabelas
(Descreva os relacionamentos entre as tabelas)

## 5. Regras de Negócio e Restrições
(Descreva as regras e restrições aplicáveis)

## 6. Procedimentos e Funções
(Se aplicável)

## 7. Exemplos de Consultas
(Exemplos de consultas SQL úteis)

## 8. Notas e Considerações
(Dicas de desempenho, manutenção, etc.)

## 9. Referências
(Links e glossário)
