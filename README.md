# Codevasf
### Organização de todos os projetos e relatórios da CODEVASF feitos pelo Tribunal de Contas da União 

# 1. Introdução
## Objetivo do Documento
Este documento fornece uma visão detalhada do esquema do banco de dados e do entendimento por completo do projeto, visando facilitar em caso de manutenção.

## Descrição do Projeto
O banco de dados é projetado para organizar e facilitar o uso de querys para auditoria e transparência do Tribunal de Contas da União

# 2. Visão Geral do Banco de Dados
## Diagrama ER
(Insira o diagrama ER aqui)

### Resumo das Tabelas
(Descreva cada tabela)

# 3. Descrição das Tabelas

## Contratos
**Descrição:** Armazena informações sobre contratos.

| Coluna           | Tipo de Dados | Restrições             | Descrição                     |
|------------------|---------------|------------------------|-------------------------------|
| ID_Contrato      | UUID          | PRIMARY KEY            | Identificador único do contrato |
| Numero_Contrato  | VARCHAR       | NOT NULL               | Número do contrato             |
| Data_Publicacao  | DATE          | NOT NULL               | Data de publicação do contrato |
| Objeto           | TEXT          |                        | Descrição do objeto do contrato|
| Valor_Total      | DECIMAL       |                        | Valor total do contrato        |

## Ordem_de_Serviço
...

# 4. Relacionamentos entre Tabelas
## Descrição dos Relacionamentos:  

## Tabela Entidades 

 ### A tabela Entidades se relaciona com a tabela Contratos através da coluna ID_Contrato. Isso significa que cada entidade está associada a um contrato específico. 
 
 ### A tabela Entidades se relaciona com a tabela Ordem_de_Servico através da coluna Ordem_de_ServiçoID. Isso significa que cada entidade está associada a uma Ordem de Serviço específica. 
 
 ### A tabela Entidades se relaciona com a tabela Ordem_de_Fornecimento através da coluna Ordem_de_FornecimentoID. Isso significa que cada entidade está associada a uma Ordem de Fornecimento específica. 

 

## Tabela Empenhos 
### A tabela Empenhos se relaciona com a tabela Contratos através da coluna ID_Contrato. Isso significa que cada empenho está associado a um contrato específico. 

### A tabela Empenhos se relaciona com a tabela Ordem_de_Fornecimento através da coluna Ordem_de_FornecimentoID. Isso significa que cada empenho está associado a uma Ordem de Fornecimento específica. 

### A tabela Empenhos se relaciona com a tabela Ordem_de_Servico através da coluna Ordem_de_ServiçoID. Isso significa que cada empenho está associado a uma Ordem de Serviço específica. 

 

## Tabela Periodo_Vigencia 

### A tabela Periodo_Vigencia se relaciona com a tabela Contratos através da coluna ID_Contrato. Isso significa que cada contrato possui um período de vigência. 

### A tabela Periodo_Vigencia se relaciona com a tabela Ordem de Serviço através da coluna Ordem_de_ServiçoID. Isso significa que cada ordem de serviço possui um período de vigência. 

### A tabela Periodo_Vigencia se relaciona com a tabela Ordem de Fornecimento através da coluna Ordem_de_FornecimentoID. Isso significa que cada ordem de fornecimento possui um período de vigência. 

# 5. Regras de Negócio e Restrições


# 6. Procedimentos e Funções


# 7. Exemplos de Consultas


# 8. Notas e Considerações


# 9. Referências

