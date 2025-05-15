import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from colorama import Fore, Style, init
import time

init(autoreset=True) 

def contador_iteração(inicio, fim):
    tempo_duracao = fim - inicio
    print(f'\tEssa Iteração durou {Fore.YELLOW}{tempo_duracao:.2f}{Style.RESET_ALL} SEGUNDOS')
def contador_tempototal(inicio_total, fim):
    tempo_duracao = fim - inicio_total
    horas, resto = divmod(tempo_duracao, 3600) 
    minutos, segundos = divmod(resto, 60) 
    tempo_formatado = f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}" 
    print(f"\t\tTempo percorrido até o momento: {Fore.YELLOW}{tempo_formatado}")

def save_excel():
    if not os.path.exists("XLS_Files"): 
        os.makedirs("XLS_Files")
    with pd.ExcelWriter(f"XLS_Files/Doações_{ano_celebracao}_2304.xlsx", engine='openpyxl') as writer:
        df_doacoes.to_excel(writer, sheet_name='Doações', index=False)
        df_entidades.to_excel(writer, sheet_name='Entidades Vinculadas', index=False)
        df_inteiro_teor.to_excel(writer, sheet_name='Termos Vinculados', index=False)
    print(f"\t{Fore.GREEN}Excel atualizado salvo com sucesso!")

def solicitar_ano():
    while True:
        try:
            ano_celebracao = int(input(f"\nPor favor, insira o ano a ser contemplado {Fore.LIGHTBLUE_EX}(entre 2010 e 2023):{Fore.GREEN} "))
            if 2010 <= ano_celebracao <= 2023:
                print(f"\nAno selecionado: {Fore.YELLOW}{ano_celebracao}")
                return str(ano_celebracao)
            else:
                print(f"{Fore.RED}Ano inválido!{Style.RESET_ALL} Por favor, insira um ano entre 2000 e 2023.")
        except ValueError:
            print(f"{Fore.RED}Entrada inválida!{Style.RESET_ALL} Certifique-se de digitar um ano numérico.")

def configura_pagina():
    waitUrl.until(EC.presence_of_element_located((By.XPATH,'//*[@id="exercicio"]/option[1]'))) 
    waitUrl.until(EC.presence_of_element_located((By.XPATH,'//*[@id="uf"]/option[1]'))) 

    exercicio_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="exercicio"]'))) 
    exercicio_box.click()
    seleciona = Select(exercicio_box)
    seleciona.select_by_value(ano_celebracao) # print(f"Campo contrato preenchido com {ano_celebracao}")    

    botao_pesquisar = waitUrl.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="exConsultar"]')))  
    botao_pesquisar.click() # print("Botão de pesquisa clicado.")

    resultList = waitUrl.until(EC.presence_of_element_located((By.XPATH, '//*[@id="resultList"]/div'))).text
    a,qtd_doacoes,b,c = resultList.rsplit(' ', 3)
    print(f"{Fore.LIGHTRED_EX}{resultList}")
    botao_listar = waitUrl.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="exListar"]')))
    botao_listar.click()
    return qtd_doacoes
    
df_doacoes = pd.DataFrame(columns=[
    'Número de Instrumento', 'Tipo de Instrumento', 'Data','Valor da Doação', 
    'Entidades Vinculadas', 'Termos Vinculados', 'Objeto'
])
df_entidades = pd.DataFrame(columns=['Número de Instrumento', 'Entidade', 'CNPJ'])
df_inteiro_teor = pd.DataFrame(columns=['Número de Instrumento', 'Termo'])


inicio_total = time.time()
driver_path = "chromedriver.exe" 
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 25) 
waitUrl = WebDriverWait(driver, 70)

url = "https://www.codevasf.gov.br/acesso-a-informacao/doacoes/doacoes-2010-a-2023" 
driver.get(url)
ano_celebracao = solicitar_ano()
qtd_doacoes = configura_pagina()
instrumentos = True

contador_refresh = 0
index = 2312 

print(f"\n\nIniciando processamento das doações referentes ao ano: {Fore.BLUE}{Style.BRIGHT}{ano_celebracao}")
while instrumentos:
    try:
        inicio = time.time()
        sucesso = False
        entidades = []
        inteiro_teor = [] 
        doacoes_xpath = f'//*[@id="quadroDoacoes"]/div/table/tbody/tr[{index}]/td[1]/a'
        doacao_link = waitUrl.until(EC.element_to_be_clickable((By.XPATH, doacoes_xpath)))
        doacao_link.click()  
        elemento = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modalPanel"]/div/table/tbody/tr[2]/td'))).text
        tipo_instrumento, numero_instrumento = elemento.rsplit(' ', 1) # print(f"Tipo de Instrumento: {tipo_instrumento}")
        print(f"\nN° Instrumento: {Fore.LIGHTMAGENTA_EX} {numero_instrumento}")
        
        data = wait.until(EC.visibility_of_element_located((By.XPATH, '//td[text()="Data :"]/following-sibling::td'))).text
        if data == '':
            data = 'Não existe' # print(f"Data: {data}")

        try:
            objeto = driver.find_element(By.XPATH, '//td[text()="Objeto :"]/following-sibling::td').text # print(f"Objeto: {objeto}")
        except NoSuchElementException:
            objeto = 'Não Disponível' # print("Objeto não encontrado.")

        try:
           valor_doacao = driver.find_element(By.XPATH, '//td[text()="Valor da doação :"]/following-sibling::td').text # print(f"Valor Total (com aditivos): {valor_total}")
        except NoSuchElementException:
            valor_doacao = 'Não Disponível' # print("Valor Total (com aditivos) não encontrado.")

        try:
            tr_entidades = driver.find_element(By.XPATH, '//td[text()="Entidades Vinculadas :"]/ancestor::tr')
            tr_seguinte_entidades = tr_entidades.find_elements(By.XPATH, 'following-sibling::tr')
            
            for tr in tr_seguinte_entidades:
                primeiro_td_entidades = tr.find_element(By.XPATH, './td[1]').text.strip()
                if primeiro_td_entidades == '':
                    cnpj = tr.find_element(By.XPATH, './td[2]').text.strip()
                    nome_entidade = tr.find_element(By.XPATH, './td[3]').text.strip()
                    entidades.append({'CNPJ': cnpj, 'Nome da Entidade': nome_entidade})
                else:
                    break

            qtd_entidades = len(entidades) # print(f"Quantidade de Entidades Vinculadas: {qtd_entidades}") # print(f"Entidades Capturadas:")
            for entidade in entidades: # print(f"\t{entidade['CNPJ']}, {entidade['Nome da Entidade']}")
                df_entidades = pd.concat([df_entidades, pd.DataFrame([{ 'Número de Instrumento': numero_instrumento, 
                    'Entidade': entidade['Nome da Entidade'], 'CNPJ': entidade['CNPJ'] }])], ignore_index=True)
        except NoSuchElementException:
            qtd_entidades = 0
            pass
        
        try:
            tr_inteiro_teor = driver.find_element(By.XPATH, '//td[text()="Inteiro Teor :"]/ancestor::tr')
            tr_seguinte_inteiro_teor = tr_inteiro_teor.find_elements(By.XPATH, 'following-sibling::tr')
            for tr in tr_seguinte_inteiro_teor:
                try:
                    termo = tr.find_element(By.XPATH, './td[2]').text.strip()
                    inteiro_teor.append(termo)
                except NoSuchElementException:
                    break

            qtd_inteiro_teor = len(inteiro_teor) # print(f"Quantidade de Termos Vinculados: {qtd_inteiro_teor}") #  print(f"Termos Capturados:")
            for termo in inteiro_teor: # print(f'\t{termo}')
                df_inteiro_teor = pd.concat([df_inteiro_teor, pd.DataFrame([{
                    'Número de Instrumento': numero_instrumento, 'Termo': termo }])], ignore_index=True)
        except NoSuchElementException:
            qtd_inteiro_teor = 0
            pass

        df_doacoes = pd.concat([df_doacoes, pd.DataFrame([{ 'Número de Instrumento': numero_instrumento,'Tipo de Instrumento': tipo_instrumento, 'Data': data, 
            'Valor da Doação': valor_doacao, 'Entidades Vinculadas': qtd_entidades, 'Termos Vinculados': qtd_inteiro_teor, 'Objeto': objeto }])], ignore_index=True)
        
        save_excel()
        sucesso = True  

        index += 1
        contador_refresh += 1

        botao_fechar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="closeModal"]')))
        botao_fechar.click() 
        fim = time.time()
        contador_iteração(inicio = inicio,fim = fim)
        print(f"\t\tN° de ITERAÇÕES para refresh: {Fore.RED}{Style.BRIGHT}{contador_refresh}/150")
        print(f"\tQuantidade de instrumentos analisados: {Fore.LIGHTMAGENTA_EX}{index-1}")
        restante_doacoes = int(qtd_doacoes) - (index - 1)
        print(f"\tQuantidade de instrumentos restantes: {Fore.LIGHTBLUE_EX}{restante_doacoes}")
        contador_tempototal(inicio_total = inicio_total, fim = fim)

        if contador_refresh >= 150:
            driver.refresh()
            contador_refresh = 0 
            configura_pagina()
            print(f"\n\t{Fore.LIGHTBLUE_EX}Site recarregado com sucesso após refresh.")
        
        if restante_doacoes == 0:
            instrumentos = False
        
    except NoSuchElementException:
        print("Não possui mais nenhum contrato para processar.")
        break
    except TimeoutException:
        print("Timeout Error - Recarregando pagina")
        driver.get(url)
        configura_pagina()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break

driver.quit()
print(f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Processo concluído.')
