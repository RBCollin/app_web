
from genericpath import exists
from math import ceil
import streamlit as st
import pandas as pd
import numpy as np
import requests
import json


st.set_page_config(layout="wide")


#if st.button('Recarregar'):
 #   st.experimental_rerun()



#################### VOU DEIXAR COMO INPUT O PERIODO DE SAFRA E O NUMERO DE EMBALADEIRAS  ####################

coluna_inicial_1, coluna_inicial_2 = st.columns([0.8,1])
with coluna_inicial_1:
    st.title('Packing House - Linhas de Embalagem')

with coluna_inicial_2:
    st.write('')
    st.write('')
    if st.button('Atualizar Controle'):
        url = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_BALANCEAMENTO_PH'
        url_embaladeiras_ativas = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_EMB_ATIVAS'

        variaveis_df = pd.read_json(url)

        def correcao_(variaveis_df):
            if variaveis_df['VARIEDADE'] == 'TOMMY ATKINS':
                return 'Tommy Atkins'
            elif variaveis_df['VARIEDADE'] == 'PALMER':
                return 'Palmer'
            elif variaveis_df['VARIEDADE'] == 'KEITT':
                return 'Keitt'
            elif variaveis_df['VARIEDADE'] == 'KENT':
                return 'Kent'
            else:
                return 'NADA'

        variaveis_df['VARIEDADE'] = variaveis_df.apply(correcao_, axis = 1)
    #variaveis_df.to_excel('teste_keitt__389.xlsx')


        def calibre(variaveis_df):
            if variaveis_df['VARIEDADE'] == 'Palmer' and (variaveis_df['PESO'] <= 1130 and variaveis_df['PESO'] > 980):
                return '4'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 980 and variaveis_df['PESO'] > 777):
                return '5'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 777 and variaveis_df['PESO'] > 630):
                return '6'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 630 and variaveis_df['PESO'] > 557):
                return '7'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 557 and variaveis_df['PESO'] > 478):
                return '8'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 478 and variaveis_df['PESO'] > 438):
                return '9'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 438 and variaveis_df['PESO'] > 376):
                return '10'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 376 and variaveis_df['PESO'] > 295):
                return '12'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 295 and variaveis_df['PESO'] > 280):
                return '14'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 280):
                return '0'
            elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] > 1130):
                return '100'
            #################################################### TOMMY ATKINS #####################################################
            elif variaveis_df['VARIEDADE'] == 'Tommy Atkins' and (variaveis_df['PESO'] <= 1200 and variaveis_df['PESO'] > 1000):
                return '4'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 1000 and variaveis_df['PESO'] > 880):
                return '5'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 880 and variaveis_df['PESO'] > 640):
                return '6'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 640 and variaveis_df['PESO'] > 557):
                return '7'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 557 and variaveis_df['PESO'] > 480):
                return '8'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 480 and variaveis_df['PESO'] > 442):
                return '9'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 442 and variaveis_df['PESO'] > 371):
                return '10'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 371 and variaveis_df['PESO'] > 296):
                return '12'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 296 and variaveis_df['PESO'] > 279):
                return '14'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 279):
                return '0'
            elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] > 1200):
                return '100'
                
            #################################################### KEITT #####################################################

            elif variaveis_df['VARIEDADE'] == 'Keitt' and (variaveis_df['PESO'] <= 1500 and variaveis_df['PESO'] > 880):
                return '4'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 880 and variaveis_df['PESO'] > 770):
                return '5'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 770 and variaveis_df['PESO'] > 622):
                return '6'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 622 and variaveis_df['PESO'] > 553):
                return '7'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 553 and variaveis_df['PESO'] > 476):
                return '8'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 476 and variaveis_df['PESO'] > 439):
                return '9'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 439 and variaveis_df['PESO'] > 385):
                return '10'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 385 and variaveis_df['PESO'] > 305):
                return '12'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 305 and variaveis_df['PESO'] > 279):
                return '14'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] <= 279):
                return '0'
            elif (variaveis_df['VARIEDADE'] == 'Keitt') and (variaveis_df['PESO'] > 1500):
                return '100'

            #################################################### KENT #####################################################
            elif variaveis_df['VARIEDADE'] == 'Kent' and (variaveis_df['PESO'] <= 1300 and variaveis_df['PESO'] > 930):
                return '4'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 930 and variaveis_df['PESO'] > 760):
                return '5'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 760 and variaveis_df['PESO'] > 626):
                return '6'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 626 and variaveis_df['PESO'] > 545):
                return '7'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 545 and variaveis_df['PESO'] > 476):
                return '8'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 476 and variaveis_df['PESO'] > 444):
                return '9'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 444 and variaveis_df['PESO'] > 375):
                return '10'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 375 and variaveis_df['PESO'] > 303):
                return '12'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 303 and variaveis_df['PESO'] > 269):
                return '14'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 269):
                return '0'
            elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] > 1300):
                return '100'


        variaveis_df['CALIBRE'] = variaveis_df.apply(calibre, axis =1)

        #variaveis_df.to_excel('keitt_395.xlsx')

        st.session_state.anterior = variaveis_df

        df_embaladeiras_ativas = pd.read_json(url_embaladeiras_ativas)
        df_embaladeiras_ativas.rename(columns = {'CPF':'MATRICULA'}, inplace = True)

        st.session_state.url_embala = df_embaladeiras_ativas


######################################################## PLANILHA QUE SUBSTITUI OS INPUTS ########################################################
dataset = st.session_state.anterior
#dataset = variaveis_df
#dataset
dataset.rename(columns = {"PESO":"Peso","CALIBRE":"Calibre","NUMERO_FRUTO":"Fruto","QUALIDADE":"Qualidade","VARIEDADE":"Variedade"}, inplace = True)


avg_frutos_caixotes = round(dataset['N_CAIXOTE'].value_counts().sum() / len(dataset['N_CAIXOTE'].value_counts()))




Caixotes = dataset['CONTENTORES'][0].item()
VARIEDADE = dataset['Variedade'][0]

######################################################## PLANILHA QUE SUBSTITUI OS INPUTS ########################################################
#st.session_state_base_crua = dataset

#dataset = dataset['Calibre'] != '4'
#dataset
#filtro = dataset['Qualidade'] != 4
dataset = dataset #[filtro]

#dataset

dataset['Calibre'] = dataset['Calibre'].astype(int)
a = dataset['Calibre'].value_counts() / dataset['Calibre'].count()

b = pd.DataFrame(a)
b = b.reset_index()
b.columns = ['Calibre', 'Percentual']
b['Percentual'] = b['Percentual']*100
b = b.sort_values('Calibre')

#################################################################################   ALTERANDO PERCENTUAIS    ####################################################################################################

result_b = b.Calibre.isin([4]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':4, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([5]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':5, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([6]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':6, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([7]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':7, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([8]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':8, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([9]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':9, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([10]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':10, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([12]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':12, 'Percentual':0}, ignore_index=True)
#################################################################################
result_b = b.Calibre.isin([14]).any().any()
if result_b:
    print(' ')
else:
    b = b.append({'Calibre':14, 'Percentual':0}, ignore_index=True)
#################################################################################


#################################################################################  ALTERANDO PERCENTUAIS    ####################################################################################################

percentual_de_4 = b[b.Calibre==4].Percentual.item()
percentual_de_5 = b[b.Calibre==5].Percentual.item()
percentual_de_6 = b[b.Calibre==6].Percentual.item()
percentual_de_7 = b[b.Calibre==7].Percentual.item()
percentual_de_8 = b[b.Calibre==8].Percentual.item()
percentual_de_9 = b[b.Calibre==9].Percentual.item()
percentual_de_10 = b[b.Calibre==10].Percentual.item()
percentual_de_12 = b[b.Calibre==12].Percentual.item()
percentual_de_14 = b[b.Calibre==14].Percentual.item()


#################################################################################  FIM ALTERANDO PERCENTUAIS    ####################################################################################################

st.session_state_base_crua = b

#filtro2 = dataset['Qualidade'] != 4
dataset_2 = dataset #[filtro2]
aa = pd.DataFrame(dataset_2['Calibre'].value_counts())
aa = aa.reset_index()
aa.columns = ['Calibre','Qtde_mangas']

b['Caixas'] = aa['Qtde_mangas'] / aa['Calibre']


############################################## Considerando QUALIDADE ##############################################

quality = dataset['Qualidade'].value_counts() / dataset['Qualidade'].count()

quality = pd.DataFrame(quality)
quality = quality.reset_index()
quality.columns = ['Qualidade','Percent']
#quality


##################################################### 3 not in quality.Qualidade.values ###########################################################################

result = quality.Qualidade.isin([3]).any().any()
#result
if result:
    print(' ')
else:
    quality = quality.append({'Qualidade':3, 'Percent':0}, ignore_index=True)
#quality


result2 = quality.Qualidade.isin([4]).any().any()
#result
if result2:
    print(' ')
else:
    quality = quality.append({'Qualidade':4, 'Percent':0}, ignore_index=True)



result3 = quality.Qualidade.isin([2]).any().any()
#result
if result3:
    print(' ')
else:
    quality = quality.append({'Qualidade':2, 'Percent':0}, ignore_index=True)





qualidade_calibres = dataset.groupby('Calibre')['Qualidade'].value_counts() / dataset.groupby('Calibre')['Qualidade'].count()
#qualidade_calibres


qualidade_calibres2 = pd.pivot_table(dataset, index = ['Calibre','Qualidade'])


primeira_percent = quality[quality.Qualidade==1].Percent.item()
segunda_percent = quality[quality.Qualidade==2].Percent.item()
terceira_percent = quality[quality.Qualidade==3].Percent.item()

refugo_percent = quality[quality.Qualidade==4].Percent.item()

#st.title('Packing House - Linhas de Embalagem')
#st.markdown('___________________')

#avg_frutos_caixotes 

produtividade_embaladeira = 0.75
produtividade_talo = 0.80
produtividade_limpeza = 0.75
produtividade_limpeza2 = 0.75
caixotes = Caixotes
variedade = VARIEDADE 
#b['Calibre'] == 5
padrao_embaldeiras_total = pd.read_excel('padrao_embaladeiras_TUDO_cenarios.xlsx')



df_embaladeiras_ativas = st.session_state.url_embala

    
df_222 = df_embaladeiras_ativas.merge(padrao_embaldeiras_total)
padrao_embaldeiras = df_222



embaladeira = len(padrao_embaldeiras.groupby('PESSOA'))
Programa_input = 'Entre Safra'
st.session_state.emba_aviso = embaladeira

coluna1, coluna2 = st.columns(2)

with coluna1:
    from PIL import Image
    img = Image.open('agrodn.png')
    newsize = (380,110)
    img2 = img.resize(newsize)

    st.sidebar.image(img2, use_column_width=True)
    st.sidebar.title('Menu')
    st.sidebar.markdown('Escolha a informação para visualizar:')
    

pagina_selecionada = st.sidebar.radio('', ['Balanceamento e produtividade','Linhas de embalagem','Distribuição embaladeiras'])


if pagina_selecionada == 'Balanceamento e produtividade':

    ############## CONTROLE ########################################################

    controle = dataset['CONTROLE'][0]
    st.session_state.controle = controle
    
    controle2 = st.session_state.controle
    st.metric(label="Controle", value= controle2, delta= VARIEDADE)  
    

    col2, col3 = st.columns([0.30,1])
    
    emba_aviso = st.session_state.emba_aviso
    st.success('#### Ajuste de distribuição')
    coluna_11, coluna_22, coluna_33, coluna_44, coluna_55 = st.columns([1,1,1,1,1])

    #
    #################################################################################  ALTERANDO PERCENTUAIS    ####################################################################################################
    percent_caliber_4 = coluna_11.number_input(label = 'Ajuste o percentual de calibre 4:', step = 0.01, value = percentual_de_4)
    percent_caliber_5 = coluna_11.number_input(label = 'Ajuste o percentual de calibre 5:', step = 0.01, value = percentual_de_5)
    percent_caliber_6 = coluna_22.number_input(label = 'Ajuste o percentual de calibre 6:', step = 0.01, value = percentual_de_6)
    percent_caliber_7 = coluna_22.number_input(label = 'Ajuste o percentual de calibre 7:', step = 0.01, value = percentual_de_7)
    percent_caliber_8 = coluna_33.number_input(label = 'Ajuste o percentual de calibre 8:', step = 0.01, value = percentual_de_8)
    percent_caliber_9 = coluna_33.number_input(label = 'Ajuste o percentual de calibre 9:', step = 0.01, value = percentual_de_9)
    percent_caliber_10 = coluna_44.number_input(label = 'Ajuste o percentual de calibre 10:', step = 0.01, value = percentual_de_10)
    percent_caliber_12 = coluna_44.number_input(label = 'Ajuste o percentual de calibre 12:', step = 0.01, value = percentual_de_12)
    percent_caliber_14 = coluna_55.number_input(label = 'Ajuste o percentual de calibre 14:', step = 0.01, value = percentual_de_14)

    st.session_state_percent_4 = percent_caliber_4 
    st.session_state_percent_5 = percent_caliber_5
    st.session_state_percent_6 = percent_caliber_6 
    st.session_state_percent_7 = percent_caliber_7 
    st.session_state_percent_8 = percent_caliber_8 
    st.session_state_percent_9 = percent_caliber_9 
    st.session_state_percent_10 = percent_caliber_10 
    st.session_state_percent_12 = percent_caliber_12
    st.session_state_percent_14 = percent_caliber_14 

    def ajuste(b):
        if b['Calibre'] == 4:
            return percent_caliber_4
        elif b['Calibre'] == 5:
            return percent_caliber_5
        elif b['Calibre'] == 6:
            return percent_caliber_6
        elif b['Calibre'] == 7:
            return percent_caliber_7
        elif b['Calibre'] == 8:
            return percent_caliber_8
        elif b['Calibre'] == 9:
            return percent_caliber_9
        elif b['Calibre'] == 10:
            return percent_caliber_10
        elif b['Calibre'] == 12:
            return percent_caliber_12
        elif b['Calibre'] == 14:
            return percent_caliber_14

    b['Percentual'] = b.apply(ajuste, axis = 1)

    #################################################################################  ALTERANDO PERCENTUAIS    ####################################################################################################

    
    st.success('#### Balanceamento')
    with st.form(key='planilha'):
        
        coluna1_1, coluna2_2,coluna3_3, coluna4_4 = st.columns([0.4,0.05,0.8,1])
        
        embaladeira_input = coluna1_1.number_input(label = 'Ajuste a quantidade de embaladeiras:', value = emba_aviso  , format = "%d", step = 1)
        Programa_input_2 = coluna1_1.selectbox('Selecione o período:', ['Entre Safra','Safra'])

        produtividade_embaladeira_input = coluna1_1.slider('Produtividade Embaladeiras', min_value = 0.1, max_value = 0.99, value = 0.75, step = 0.01)
        produtividade_talo_input = coluna1_1.slider('Produtividade Corte de Talo', min_value = 0.1, max_value = 0.99, value = 0.80, step = 0.01)
        produtividade_limpeza_input = coluna1_1.slider('Produtividade da Limpeza', min_value = 0.1, max_value = 0.99, value = 0.75, step = 0.01)
        produtividade_limpeza2_input = coluna1_1.slider('Produtividade da Seleção', min_value = 0.1, max_value = 0.99, value = 0.75, step = 0.01) 


        colun, colun2, colun3, colun4 = st.columns([1,0.5,0.5,0.5])

        with colun4:
            colun.success('#### Selecione ao lado se a embalagem é com ou sem papel:')
            colun2.write('')
            colun3.write('')
            colun4.write('')
            calibre_4_papel = colun2.selectbox(label = 'Calibre 4', options = ('Sem','Com'))
            calibre_5_papel = colun3.selectbox(label = 'Calibre 5', options = ('Sem','Com'))
            calibre_6_papel = colun4.selectbox(label = 'Calibre 6', options = ('Sem','Com'))
            calibre_7_papel = colun2.selectbox(label = 'Calibre 7', options = ('Sem','Com'))
            calibre_8_papel = colun3.selectbox(label = 'Calibre 8', options = ('Sem','Com'))
            calibre_9_papel = colun4.selectbox(label = 'Calibre 9', options = ('Sem','Com'))
            calibre_10_papel = colun2.selectbox(label = 'Calibre 10', options = ('Sem','Com'))
            calibre_12_papel = colun3.selectbox(label = 'Calibre 12', options = ('Sem','Com'))
            calibre_14_papel = colun4.selectbox(label = 'Calibre 14', options = ('Sem','Com'))
        
        button_submit = coluna1_1.form_submit_button('Calcular')

    if button_submit:
        embaladeira =  embaladeira_input
        Programa_input = Programa_input_2
        produtividade_embaladeira = produtividade_embaladeira_input
        produtividade_talo= produtividade_talo_input 
        produtividade_limpeza = produtividade_limpeza_input
        produtividade_limpeza2 = produtividade_limpeza2_input


################################################################ PAPEL ################################################################


    def ritmo(b):
            if (b['Calibre'] == 5 and variedade == 'Palmer') and (calibre_4_papel == 'Com' or calibre_4_papel == 'Sem'):
                return 229
            elif (b['Calibre'] == 4 and variedade == 'Palmer') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                return 229
            elif (b['Calibre'] == 6 and variedade == 'Palmer') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                return 169
            elif (b['Calibre'] == 7 and variedade == 'Palmer') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                return 174
            elif (b['Calibre'] == 8 and variedade == 'Palmer') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                return 191
            elif (b['Calibre'] == 9 and variedade == 'Palmer') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                return 157
            elif (b['Calibre'] == 10 and variedade == 'Palmer') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                return 139
            elif (b['Calibre'] == 12 and variedade == 'Palmer') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                return 149
            elif (b['Calibre'] == 14 and variedade == 'Palmer') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                return 85

    ###################################################################### Keitt #############################################################

            elif (b['Calibre'] == 5 and variedade == 'Keitt') and (calibre_5_papel == 'Sem'):
                return 517
            elif (b['Calibre'] == 4 and variedade == 'Keitt') and (calibre_4_papel == 'Sem'):
                return 517
            elif (b['Calibre'] == 6 and variedade == 'Keitt') and (calibre_6_papel == 'Sem'):
                return 412
            elif (b['Calibre'] == 7 and variedade == 'Keitt') and (calibre_7_papel == 'Sem'):
                return 321
            elif (b['Calibre'] == 8 and variedade == 'Keitt') and (calibre_8_papel == 'Sem'):
                return 301
            elif (b['Calibre'] == 9 and variedade == 'Keitt') and (calibre_9_papel == 'Sem'):
                return 257
            elif (b['Calibre'] == 10 and variedade == 'Keitt') and (calibre_10_papel == 'Sem'):
                return 261
            elif (b['Calibre'] == 12 and variedade == 'Keitt') and (calibre_12_papel == 'Sem'):
                return 253
            elif (b['Calibre'] == 14 and variedade == 'Keitt') and (calibre_14_papel == 'Sem'):
                return 220

            elif (b['Calibre'] == 5 and variedade == 'Keitt') and (calibre_5_papel == 'Com'):
                return 235
            elif (b['Calibre'] == 4 and variedade == 'Keitt') and (calibre_4_papel == 'Com'):
                return 235
            elif (b['Calibre'] == 6 and variedade == 'Keitt') and (calibre_6_papel == 'Com'):
                return 178
            elif (b['Calibre'] == 7 and variedade == 'Keitt') and (calibre_7_papel == 'Com'):
                return 185
            elif (b['Calibre'] == 8 and variedade == 'Keitt') and (calibre_8_papel == 'Com'):
                return 195
            elif (b['Calibre'] == 9 and variedade == 'Keitt') and (calibre_9_papel == 'Com'):
                return 154
            elif (b['Calibre'] == 10 and variedade == 'Keitt') and (calibre_10_papel == 'Com'):
                return 144
            elif (b['Calibre'] == 12 and variedade == 'Keitt') and (calibre_12_papel == 'Com'):
                return 158
            elif (b['Calibre'] == 14 and variedade == 'Keitt') and (calibre_14_papel == 'Com'):
                return 90

    ################################################## Kent #############################################################
    #### Valores da Kent na planilha são iguais ao da Keitt
    #### Encontrei anteriormente no estudo das embaladerias que o ritmo era bem parecido com o da Keitt porém com pequenas diferenças
    #### por isso vou considerar os ritmos iguais aos do estudo e não iguais aos da Keitt

            elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Sem'):
                return 510
            elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Sem'):
                return 410
            elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Sem'):
                return 314
            elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Sem'):
                return 300
            elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Sem'):
                return 253
            elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Sem'):
                return 248
            elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Sem'):
                return 246
            elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Sem'):
                return 200


            elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Com'):
                return 235
            elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Com'):
                return 178
            elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Com'):
                return 185
            elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Com'):
                return 195
            elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Com'):
                return 154
            elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Com'):
                return 144
            elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Com'):
                return 158
            elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Com'):
                return 90


    ################################################## Tommy #############################################################

            elif (b['Calibre'] == 5 and variedade == 'Tommy Atkins') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                return 235
            elif (b['Calibre'] == 6 and variedade == 'Tommy Atkins') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                return 178
            elif (b['Calibre'] == 7 and variedade == 'Tommy Atkins') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                return 185
            elif (b['Calibre'] == 8 and variedade == 'Tommy Atkins') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                return 195
            elif (b['Calibre'] == 9 and variedade == 'Tommy Atkins') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                return 154
            elif (b['Calibre'] == 10 and variedade == 'Tommy Atkins') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                return 144
            elif (b['Calibre'] == 12 and variedade == 'Tommy Atkins') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                return 158
            elif (b['Calibre'] == 14 and variedade == 'Tommy Atkins') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                return 90
            else:
                return 'NADA'
    
    b['Ritmo'] = b.apply(ritmo, axis = 1)
    #b
    filtro_ritmo = b['Ritmo'] != 'NADA'
    b = b[filtro_ritmo]
        #b
        ########################################## Criando variaveis #######################################################################
        ############################################## INPUTS #######################################################################
    col1, col2,col3,col4 = st.columns([0.1,0.01,1,1.2])
    


    #corte_talo = round(((embaladeira * produtividade_embaladeira) / (3.5 * produtividade_talo))) + 1

    ##################################################################################################################################################
    
    b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100

    b['Caixas_1'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * primeira_percent) / b['Calibre']) 
    b['Caixas_2'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * segunda_percent)  / b['Calibre']) 
    b['Caixas_3'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * terceira_percent) / b['Calibre']) 
    #b['Caixas_Aereo'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * aereo_percent) / b['Calibre'])
    #
    b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira    



    #b['Horas_aereo'] = (b['Caixas_Aereo'] / b['Ritmo_aereo']) / produtividade_embaladeira 
    

    #b['Horas_4kg'] = (b['Horas_4kg'] + b['Horas_aereo'].fillna(0))
    
    #############################################################################################################
        #import SessionState
    st.session_state.caixotes = caixotes
    st.session_state.embaladeira = embaladeira
    st.session_state.variedade = variedade
    st.session_state.periodo_safra = Programa_input 
    st.session_state.produtividade_embaladeira = produtividade_embaladeira
    st.session_state.produtividade_talo = produtividade_talo
    st.session_state.produtividade_limpeza = produtividade_limpeza
    st.session_state.produtividade_selecao = produtividade_limpeza2

    st.session_state.calibre4 = calibre_4_papel
    st.session_state.calibre5 = calibre_5_papel
    st.session_state.calibre6 = calibre_6_papel
    st.session_state.calibre7 = calibre_7_papel
    st.session_state.calibre8 = calibre_8_papel
    st.session_state.calibre9 = calibre_9_papel
    st.session_state.calibre10 = calibre_10_papel
    st.session_state.calibre12 = calibre_12_papel
    st.session_state.calibre14 = calibre_14_papel


    ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))
    #corte_talo = round(((embaladeira * produtividade_embaladeira) / (3.5 * produtividade_talo))) + 1

    #avg_frutos_caixotes = 30
    #caixotes = 828
    #produtividade_talo = 0.80
    #ritmo_embaladeira = 0.061099691


    corte_talo = round((caixotes * avg_frutos_caixotes) / (101303.19 * produtividade_talo * ritmo_embaladeira))
    
    ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))

    diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))

    corte_talo2 = corte_talo
    ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))
    
        
    def equilibrio(corte_talo, embaladeira):
    
            caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
            #ritmo_talo_2
            Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
            ton_horas = round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2)
            soma = segunda_percent + terceira_percent + refugo_percent                
            selecao_ = round((caixotes_hora * avg_frutos_caixotes * soma / (3501 * produtividade_limpeza2)) + (caixotes_hora * avg_frutos_caixotes * primeira_percent / (6480 * produtividade_limpeza2)))
            st.write('#### Quantidade ideal de pessoas no talo:', corte_talo2)
            st.write('#### Quantidade de pessoas na seleção:',selecao_ )
            st.write('#### Quantidade de pessoas na limpeza:', Limpeza_selecao)
            st.write('#### Capacidade de Caixotes/Hora:', caixotes_hora)
            st.write('#### Capacidade de Toneladas/Hora:', ton_horas)
                    
            st.session_state.caixotes_hora = caixotes_hora
            st.session_state.ton_horas = ton_horas


    with coluna3_3:
                #st.markdown('       ')
                #st.markdown("""__________________________________________""")
                st.info('#### Recomendação para balanceamento:')
                #st.markdown('_____')
                st.markdown('       ')
                st.markdown('       ')
                st.markdown('       ')
            #st.markdown('_____')
                equilibrio(corte_talo, embaladeira)
            
        #equilibrio(corte_talo, embaladeira)
        
        #corte_talo
        #b
########################################### grafico plotly ################################################################
        #st.write('A variedade selecionada foi:', variedade)
    with coluna4_4:
                #st.markdown('       ')
                st.info('#### Distribuição de calibres:')
                #st.markdown('_____')
                import plotly.express as px

                dataset_33 = st.session_state_base_crua 
                #dataset_33

                dataset_33['Calibre Name'] = dataset_33['Calibre'].astype(str)
                c = round(dataset_33['Percentual'],2)
                

                def rename(dataset_33):
                    if dataset_33['Calibre Name'] == '0':
                        return 'Pequeno'
                    elif dataset_33['Calibre Name'] == '100':
                        return 'Grande'
                    else:
                        return dataset_33['Calibre Name']

                dataset_33['Calibre Name'] = dataset_33.apply(rename, axis = 1) 
                

                fig = px.bar(dataset_33, x = 'Calibre Name',y = 'Percentual', color = 'Calibre Name', text = c, color_discrete_sequence= px.colors.sequential.Aggrnyl, category_orders={'Calibre Name':['4','5','6','7','8','9','10','12','14']})
                fig.update_layout(height = 440, width = 750,
                uniformtext_minsize=8, uniformtext_mode='show',
                xaxis_title = "Calibre", font = dict(size = 16))
                fig.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)
                st.plotly_chart(fig) 
    with coluna2_2:
        st.write(" ")
        st.session_state.b = b

elif pagina_selecionada == 'Linhas de embalagem':
    
    caixotes_hora = st.session_state.caixotes_hora
    controle2 = st.session_state.controle
    ton_horas = st.session_state.ton_horas
    #caixotes_hora2 = st.session_state.caixotes_hora2 = caixotes_hora2
    col1, col2, col3, col4 = st.columns([1,1,1,1])

    col1.write("")
    col2.metric(label="Controle", value= controle2, delta= VARIEDADE)
    col3.metric(label="Caixotes/Hora", value= caixotes_hora, delta= None)
    col4.metric(label="Toneladas/Hora", value= ton_horas, delta= None)
    
    

    col11,col22, col33 = st.columns([0.3,0.4,0.4])
    coluna1, coluna2 = st.columns(2)

    col1, col2 = st.columns([0.01,1])
    
    #col11.write('##### Selecione o período:')
    #Programa_input = col11.selectbox(' ', ['Entre Safra','Safra'])
    #  
    Programa_input = st.session_state.periodo_safra

    caixotes = st.session_state.caixotes 
    embaladeira = st.session_state.embaladeira 
    variedade = st.session_state.variedade

    produtividade_embaladeira = st.session_state.produtividade_embaladeira
    produtividade_talo = st.session_state.produtividade_talo
    produtividade_limpeza = st.session_state.produtividade_limpeza 
    produtividade_limpeza2 = st.session_state.produtividade_selecao 

    calibre_4_papel = st.session_state.calibre4 
    calibre_5_papel = st.session_state.calibre5 
    calibre_6_papel = st.session_state.calibre6 
    calibre_7_papel = st.session_state.calibre7 
    calibre_8_papel = st.session_state.calibre8 
    calibre_9_papel = st.session_state.calibre9 
    calibre_10_papel = st.session_state.calibre10
    calibre_12_papel = st.session_state.calibre12
    calibre_14_papel = st.session_state.calibre14


    percent_caliber_4 = st.session_state_percent_4
    percent_caliber_5 = st.session_state_percent_5
    percent_caliber_6 = st.session_state_percent_6
    percent_caliber_7 = st.session_state_percent_7
    percent_caliber_8 = st.session_state_percent_8
    percent_caliber_9 = st.session_state_percent_9
    percent_caliber_10 = st.session_state_percent_10
    percent_caliber_12 = st.session_state_percent_12
    percent_caliber_14 = st.session_state_percent_14
    
    def ajuste(b):
        if b['Calibre'] == 4:
            return percent_caliber_4
        elif b['Calibre'] == 5:
            return percent_caliber_5
        elif b['Calibre'] == 6:
            return percent_caliber_6
        elif b['Calibre'] == 7:
            return percent_caliber_7
        elif b['Calibre'] == 8:
            return percent_caliber_8
        elif b['Calibre'] == 9:
            return percent_caliber_9
        elif b['Calibre'] == 10:
            return percent_caliber_10
        elif b['Calibre'] == 12:
            return percent_caliber_12
        elif b['Calibre'] == 14:
            return percent_caliber_14
    b['Percentual'] = b.apply(ajuste, axis = 1)
    def ritmo(b):
            if (b['Calibre'] == 5 and variedade == 'Palmer') and (calibre_4_papel == 'Com' or calibre_4_papel == 'Sem'):
                return 229
            elif (b['Calibre'] == 4 and variedade == 'Palmer') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                return 229
            elif (b['Calibre'] == 6 and variedade == 'Palmer') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                return 169
            elif (b['Calibre'] == 7 and variedade == 'Palmer') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                return 174
            elif (b['Calibre'] == 8 and variedade == 'Palmer') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                return 191
            elif (b['Calibre'] == 9 and variedade == 'Palmer') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                return 157
            elif (b['Calibre'] == 10 and variedade == 'Palmer') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                return 139
            elif (b['Calibre'] == 12 and variedade == 'Palmer') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                return 149
            elif (b['Calibre'] == 14 and variedade == 'Palmer') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                return 85

    ###################################################################### Keitt #############################################################

            elif (b['Calibre'] == 5 and variedade == 'Keitt') and (calibre_5_papel == 'Sem'):
                return 517
            elif (b['Calibre'] == 4 and variedade == 'Keitt') and (calibre_4_papel == 'Sem'):
                return 517
            elif (b['Calibre'] == 6 and variedade == 'Keitt') and (calibre_6_papel == 'Sem'):
                return 412
            elif (b['Calibre'] == 7 and variedade == 'Keitt') and (calibre_7_papel == 'Sem'):
                return 321
            elif (b['Calibre'] == 8 and variedade == 'Keitt') and (calibre_8_papel == 'Sem'):
                return 301
            elif (b['Calibre'] == 9 and variedade == 'Keitt') and (calibre_9_papel == 'Sem'):
                return 257
            elif (b['Calibre'] == 10 and variedade == 'Keitt') and (calibre_10_papel == 'Sem'):
                return 261
            elif (b['Calibre'] == 12 and variedade == 'Keitt') and (calibre_12_papel == 'Sem'):
                return 253
            elif (b['Calibre'] == 14 and variedade == 'Keitt') and (calibre_14_papel == 'Sem'):
                return 220

            elif (b['Calibre'] == 5 and variedade == 'Keitt') and (calibre_5_papel == 'Com'):
                return 235
            elif (b['Calibre'] == 4 and variedade == 'Keitt') and (calibre_4_papel == 'Com'):
                return 235
            elif (b['Calibre'] == 6 and variedade == 'Keitt') and (calibre_6_papel == 'Com'):
                return 178
            elif (b['Calibre'] == 7 and variedade == 'Keitt') and (calibre_7_papel == 'Com'):
                return 185
            elif (b['Calibre'] == 8 and variedade == 'Keitt') and (calibre_8_papel == 'Com'):
                return 195
            elif (b['Calibre'] == 9 and variedade == 'Keitt') and (calibre_9_papel == 'Com'):
                return 154
            elif (b['Calibre'] == 10 and variedade == 'Keitt') and (calibre_10_papel == 'Com'):
                return 144
            elif (b['Calibre'] == 12 and variedade == 'Keitt') and (calibre_12_papel == 'Com'):
                return 158
            elif (b['Calibre'] == 14 and variedade == 'Keitt') and (calibre_14_papel == 'Com'):
                return 90

    ################################################## Kent #############################################################
    #### Valores da Kent na planilha são iguais ao da Keitt
    #### Encontrei anteriormente no estudo das embaladerias que o ritmo era bem parecido com o da Keitt porém com pequenas diferenças
    #### por isso vou considerar os ritmos iguais aos do estudo e não iguais aos da Keitt

            elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Sem'):
                return 510
            elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Sem'):
                return 410
            elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Sem'):
                return 314
            elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Sem'):
                return 300
            elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Sem'):
                return 253
            elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Sem'):
                return 248
            elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Sem'):
                return 246
            elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Sem'):
                return 200


            elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Com'):
                return 235
            elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Com'):
                return 178
            elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Com'):
                return 185
            elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Com'):
                return 195
            elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Com'):
                return 154
            elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Com'):
                return 144
            elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Com'):
                return 158
            elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Com'):
                return 90


    ################################################## Tommy #############################################################

            elif (b['Calibre'] == 5 and variedade == 'Tommy Atkins') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                return 235
            elif (b['Calibre'] == 6 and variedade == 'Tommy Atkins') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                return 178
            elif (b['Calibre'] == 7 and variedade == 'Tommy Atkins') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                return 185
            elif (b['Calibre'] == 8 and variedade == 'Tommy Atkins') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                return 195
            elif (b['Calibre'] == 9 and variedade == 'Tommy Atkins') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                return 154
            elif (b['Calibre'] == 10 and variedade == 'Tommy Atkins') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                return 144
            elif (b['Calibre'] == 12 and variedade == 'Tommy Atkins') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                return 158
            elif (b['Calibre'] == 14 and variedade == 'Tommy Atkins') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                return 90
            else:
                return 'NADA'
    
    b['Ritmo'] = b.apply(ritmo, axis = 1)
    
    filtro_ritmo = b['Ritmo'] != 'NADA'
    b = b[filtro_ritmo]
        #b
        ########################################## Criando variaveis #######################################################################
        ############################################## INPUTS #######################################################################
    
    col1, col2,col3,col4 = st.columns([0.1,5,1,1.2])
    
    #corte_talo = round(((embaladeira * produtividade_embaladeira) / (3.5 * produtividade_talo))) + 1

    ##################################################################################################################################################
    
    b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100

    b['Caixas_1'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * primeira_percent) / b['Calibre']) 
    b['Caixas_2'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * segunda_percent)  / b['Calibre']) 
    b['Caixas_3'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * terceira_percent) / b['Calibre']) 
    #b['Caixas_Aereo'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * aereo_percent) / b['Calibre'])
    #
    b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira    
    

    ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))

    corte_talo = round((caixotes * avg_frutos_caixotes) / (101303.19 * produtividade_talo * ritmo_embaladeira))
    
    ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))

    diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))

    corte_talo2 = corte_talo
    ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))
    

    #selecao_ =(caixotes_hora * avg_frutos_caixotes) * (segunda_percent + terceira_percent + refugo_percent) / (3501 * produtividade_limpeza2) + caixotes_hora * avg_frutos_caixotes * primeira_percent / (6480 * produtividade_limpeza2)

    def equilibrio(corte_talo, embaladeira):


        caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
        soma = segunda_percent + terceira_percent + refugo_percent
        selecao_ = round((caixotes_hora * avg_frutos_caixotes * soma / (3501 * produtividade_limpeza2)) + (caixotes_hora * avg_frutos_caixotes * primeira_percent / (6480 * produtividade_limpeza2)))
        st.write("A quantidade ideal de pessoas no talo tem que ser:", corte_talo2)
        st.write('Capacidade de caixotes/hora no corte de talo é de:', caixotes_hora)
        st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
        Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
            #Limpeza_selecao
        st.write('Quantidade de pessoas na limpeza:', Limpeza_selecao)
        st.write('Quantidade de pessoas na selelao:', selecao_)
            
        
    
    ########################################### SAIDA DA ABA DE LINHAS ###########################################
    Layout_linha = pd.DataFrame({"Linha":['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22'],
                                "Calibre":"",
                                "Qualidade":"",
                                "Calibre2":"",
                                "Qualidade2":"",
                                "Auxiliar":"",
                                "Auxiliar2":"",
                                "Frutos":"",
                                "Frutos2":"",
                                "Caixas":"",
                                "Caixas2":"",
                                "Horas":"",
                                "Embaladeiras":"",
                                "Paletizadores":""}) 
    #Layout_linha



    def preenchendo_calibre(Layout_linha):
        if (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
            return '6'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
            return '12'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
            return '6'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
            return '7'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
            return '7'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
            return '5'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
            return '5'

########################################################## TOMMY ############################################################################

        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
            return '12'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
            return '7'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
            return '7'



############################################################### KENT E KEITT ###############################################################
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Aéreo'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Aéreo'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '6'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '6'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '7'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '7'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '9'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '9'
################################################### PERIODO DE SAFRA ##################################################################################################

        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '14'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '14'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '7'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '7'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '10'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '10'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '12'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '12'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '8'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '8'

############################################################### KENT E KEITT ###############################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '14'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '14'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '9'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '9'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '6'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '8'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '8'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '7'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '7'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '12'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '12'

        else:
            return 'NADA'

    Layout_linha['Calibre'] = Layout_linha.apply(preenchendo_calibre, axis = 1)

    def preenchendo_qualidade(Layout_linha):
        if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
            return '2'
        ####################################################### TOMMY ATKINS #############################################################

        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
            return '2'

############################################################### KENT E KEITT ###############################################################
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'

        ################################################### PERIODO DE SAFRA ##################################################################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
############################################################### KENT E KEITT ###############################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'

        else:
            return 'NADA'

    Layout_linha['Qualidade'] = Layout_linha.apply(preenchendo_qualidade, axis = 1)

    def preenchendo_calibre2(Layout_linha):
        if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
            return '12'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
            return '10'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
            return '9'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
            return '9'

################################################ TOMMY ATKINS ################################################

        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
            return '12'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
            return '14'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
            return '14'

############################################################### KENT E KEITT ###############################################################

        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '16'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '12'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '12'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '5'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '5'
        ################################################### PERIODO DE SAFRA ##################################################################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '5'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '5'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
############################################################### KENT E KEITT ###############################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '16'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '6'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '5'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '5'


        else:
            return 'NADA'

    Layout_linha['Calibre2'] = Layout_linha.apply(preenchendo_calibre2, axis = 1)

    def preenchendo_qualidade2(Layout_linha):
        if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
            return '2'
#################################################### TOMMY ATKINS ########################################3

        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
            return '2'

############################################################### KENT E KEITT ###############################################################
    
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'

################################################### PERIODO DE SAFRA ##################################################################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
############################################################### KENT E KEITT ###############################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'

        else:
            return 'NADA'

    Layout_linha['Qualidade2'] = Layout_linha.apply(preenchendo_qualidade2, axis = 1)

    Layout_linha['Auxiliar'] = Layout_linha['Calibre'] + Layout_linha['Qualidade']
    Layout_linha['Auxiliar2'] = Layout_linha['Calibre2'] + Layout_linha['Qualidade2']

    #Layout_linha

    #Layout_linha
    type(Layout_linha['Qualidade'])

    #Layout_linha
    #quality

    b['Calibre'] = b['Calibre'].astype(str)
    #b

    quality['Qualidade']=quality['Qualidade'].astype(str)

##################################### CALCULO DA QUANTIDADE DE FRUTOS NAS LINHAS ################################################################

    #Layout_linha
    Layout_linha_2 = pd.merge(Layout_linha, quality, on = 'Qualidade', how = 'left')
    Layout_linha_2.rename(columns={'Percent':'P_Quali_1'}, inplace = True)
    #Layout_linha_2
    #Layout_linha_2

    Layout_linha_3 = pd.merge(Layout_linha_2, quality, left_on = 'Qualidade2',right_on = 'Qualidade', how = 'left')
    Layout_linha_3.rename(columns={'Percent':'P_Quali_2'}, inplace = True)
    Layout_linha_3 = Layout_linha_3.drop(columns = ['Qualidade_y'])
    #Layout_linha_3



    Layout_linha_4 = pd.merge(Layout_linha_3, b[['Calibre','Percentual']], left_on = 'Calibre', right_on = 'Calibre', how = 'left')
    Layout_linha_4.rename(columns={'Percentual':'P_cal_1'}, inplace = True)
    #Layout_linha_4


    Layout_linha_5 = pd.merge(Layout_linha_4, b[['Calibre','Percentual']], left_on = 'Calibre2', right_on = 'Calibre', how = 'left')
    Layout_linha_5.rename(columns={'Percentual':'P_cal_2'}, inplace = True)
    Layout_linha_5 = Layout_linha_5.drop(columns = ['Calibre_y'])
    Layout_linha_5.rename(columns = {'Calibre_x':'Calibre','Qualidade_x':'Qualidade'}, inplace = True)
    
    #Layout_linha_5
    
    Layout_linha_5['Frutos'] = (caixotes * avg_frutos_caixotes) * Layout_linha_5['P_cal_1'] * (Layout_linha_5['P_Quali_1']/100)

    Layout_linha_5['Frutos2'] = (caixotes * avg_frutos_caixotes) * Layout_linha_5['P_cal_2'] * (Layout_linha_5['P_Quali_2']/100)

    #Layout_linha_5['Frutos_aereo'] = (caixotes * avg_frutos_caixotes) * Layout_linha_5['P_cal_2'] * (Layout_linha_5['P_Quali_2']/100)

    #Layout_linha_5

##################################### CALCULO DE CAIXAS POR LINHAS ################################################################

    Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].replace("Refugo","1")
    Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].replace("Aéreo","2")

    Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].replace("","1")

    Layout_linha_5['Calibre2'] = Layout_linha_5['Calibre2'].replace("","1")


    Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].astype(float)
    Layout_linha_5['Calibre2'] = Layout_linha_5['Calibre2'].astype(float)

    Layout_linha_5['Caixas'] = Layout_linha_5['Frutos'] / Layout_linha_5['Calibre']
    Layout_linha_5['Caixas2'] = Layout_linha_5['Frutos2'] / Layout_linha_5['Calibre2']

    #Layout_linha_5
    
    ##################################### CALCULO DE HORAS POR LINHA ################################################################

    #b['Caixas'] = b['Caixas'].astype(str)
    b['Calibre'] = b['Calibre'].astype(float)
    #Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].astype(str)

    Layout_linha_6 = pd.merge(Layout_linha_5, b[['Calibre','Ritmo']], left_on = 'Calibre', right_on = 'Calibre', how = 'left')
    Layout_linha_6.rename(columns={'Ritmo':'Ritmo_1'}, inplace = True)
    
    Layout_linha_7 = pd.merge(Layout_linha_6, b[['Calibre','Ritmo']], left_on = 'Calibre2', right_on = 'Calibre', how = 'left')
    Layout_linha_7 = Layout_linha_7.drop(columns = ['Calibre_y'])
    Layout_linha_7.rename(columns = {'Ritmo':'Ritmo_2','Calibre_x':'Calibre'}, inplace = True) 



    Layout_linha_7['Horas_1'] = (Layout_linha_7['Caixas'] / Layout_linha_7['Ritmo_1'])
    Layout_linha_7['Horas_1'].fillna(0, inplace = True)

    Layout_linha_7['Horas_2'] = (Layout_linha_7['Caixas2'] / Layout_linha_7['Ritmo_2'])
    Layout_linha_7['Horas_2'].fillna(0, inplace = True)

    Layout_linha_7['Horas'] = Layout_linha_7['Horas_1'] + Layout_linha_7['Horas_2']

    Layout_linha_7['Embaladeiras'] = round((embaladeira * Layout_linha_7['Horas']) / Layout_linha_7['Horas'].sum(),1)

    Layout_linha_7['Embaladeiras_1'] = round((embaladeira * Layout_linha_7['Horas_1']) / Layout_linha_7['Horas'].sum(),1)
    Layout_linha_7['Embaladeiras_2'] = round((embaladeira * Layout_linha_7['Horas_2']) / Layout_linha_7['Horas'].sum(),1)
    #Layout_linha_7


    def setores(Layout_linha_7):
        if Layout_linha_7['Linha'] == '1' or Layout_linha_7['Linha'] == '2':
            return 1
        elif Layout_linha_7['Linha'] == '3' or Layout_linha_7['Linha'] == '4' or Layout_linha_7['Linha'] == '5' or Layout_linha_7['Linha'] == '6':
            return 2
        elif Layout_linha_7['Linha'] == '7' or Layout_linha_7['Linha'] == '8' or Layout_linha_7['Linha'] == '9' or Layout_linha_7['Linha'] == '10':
            return 3
        elif Layout_linha_7['Linha'] == '11' or Layout_linha_7['Linha'] == '12' or Layout_linha_7['Linha'] == '13' or Layout_linha_7['Linha'] == '14':
            return 4
        elif Layout_linha_7['Linha'] == '15' or Layout_linha_7['Linha'] == '16' or Layout_linha_7['Linha'] == '17' or Layout_linha_7['Linha'] == '18':
            return 5
        elif Layout_linha_7['Linha'] == '19' or Layout_linha_7['Linha'] == '20' or Layout_linha_7['Linha'] == '21' or Layout_linha_7['Linha'] == '22':
            return 6
        else:
            return 'NADA'

    Layout_linha_7['Setores'] = Layout_linha_7.apply(setores, axis = 1)
    Layout_linha_7['Setores'] = Layout_linha_7['Setores'].astype(str)
    
    #coluna_1, coluna_2 = st.columns([1,1])
    import plotly.express as px
    import plotly.graph_objects as go
    
    with col11:
        st.write("")
        st.info('##### Percentuais de qualidade:')
        fig = go.Figure(data=[go.Pie(labels = quality['Qualidade'], values = quality['Percent'], marker_colors = px.colors.sequential.Emrld ,hole = .35, pull=0.025)])
        #fig = px.pie(b, names = 'Calibre Name', values = 'Percentual', hole = .35)
        fig.update_traces(textinfo='label+percent', textfont_size=15, textposition="inside")
        fig.update_layout(height = 450, width = 450, font = dict(size = 15))
        #fig.update_traces(textinfo='label+percent', textfont_size=20, textposition="inside")
        st.plotly_chart(fig) 


    with col22:
        st.write(" ")
        st.info('##### Quantidade de embaladeiras por setor:')
        #import plotly.express as px
        df_setores = round(Layout_linha_7.groupby('Setores')['Embaladeiras'].sum(),2)

        df_setores = df_setores.reset_index()
        df_setores['Embaladeiras'] = round(df_setores['Embaladeiras'],0)
        fig2 = px.bar(df_setores, x = 'Setores', y = 'Embaladeiras', color = 'Setores', text= 'Embaladeiras', color_discrete_sequence= px.colors.sequential.Aggrnyl ) 
        fig2.update_layout(height = 450, width = 650, uniformtext_minsize = 8, uniformtext_mode = 'show', font = dict(size = 14))
        fig2.update_traces(textfont_size = 14, textangle = 0, textposition = 'outside', cliponaxis = False)
        st.plotly_chart(fig2)



        #import plotly.express as px
        #b['Calibre Name'] = b['Calibre'].astype(str)
        #c = round(b['Percentual'],2)
        
    with col33:
        st.write(" ")
        st.info('##### Quantidade de embaladeiras por linha:')
        #Layout_linha_8
        fig = px.bar(Layout_linha_7, x = 'Linha', y = 'Embaladeiras', 
        color = 'Setores', text = 'Embaladeiras',color_discrete_sequence= px.colors.sequential.Aggrnyl)
        fig.update_layout(height = 450, width = 650, uniformtext_minsize=8, uniformtext_mode='show', font = dict(size = 14))
        fig.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig)

    with col2:

        st.info('##### Informações detalhadas das linhas de embalagem:')
        st.write('_______')
        Layout_linha_8 = Layout_linha_7[['Linha','Calibre','Qualidade','Calibre2','Qualidade2','Frutos','Frutos2','Caixas','Caixas2','Embaladeiras','Setores','Embaladeiras_1','Embaladeiras_2']]
        Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].astype(str)
        Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].replace('1.0',' ')
        Layout_linha_8  = Layout_linha_8.fillna(0)
        Layout_linha_8 = round(Layout_linha_8,1)
        Layout_linha_8 = Layout_linha_8.astype(str)
        Layout_linha_8 = Layout_linha_8.replace('0.0',' ')
        Layout_linha_8 = Layout_linha_8.replace('1.0',' ')
        Layout_linha_8
        Layout_linha_8.to_excel('Layout_final.xlsx')
        

        
elif pagina_selecionada == 'Distribuição embaladeiras':
    embaladeira = st.session_state.embaladeira 

    produtividade_embaladeira = st.session_state.produtividade_embaladeira
    produtividade_talo = st.session_state.produtividade_talo

    b = st.session_state.b
    caixotes_hora = st.session_state.caixotes_hora
    controle2 = st.session_state.controle
    ton_horas = st.session_state.ton_horas

    col1x, col2x, col3x, col4x = st.columns([1,1,1,1])
    col3x.metric(label="Toneladas/Hora anterior", value= ton_horas, delta= None)
    col1x.metric(label="Controle", value= controle2, delta= VARIEDADE)
    col2x.metric(label="Caixotes/Hora", value= caixotes_hora, delta= None)
    #col4x.metric(label="Toneladas/Hora", value= ton_horas, delta= None)
    
    variedade = st.session_state.variedade
    colunas1, colunas2 = st.columns(2)
    col1, col2, col3 = st.columns(3)
    colunas1, colunas2 = st.columns([1,0.001])
    with colunas1:
        st.success('### Recomendação de embaladeiras por calibre:')

    colu1, colu2, colu3, colu4  = st.columns(4)
    import plotly.express as px
    Layout_linha_9 = pd.read_excel('Layout_final.xlsx')
    #Layout_linha_9
    Layout_linha_9 = Layout_linha_9.drop(columns = ['Unnamed: 0'])
    Layout_linha_9['Setores'] = Layout_linha_9['Setores'].astype(str)

    Layout_linha_9['Embaladeiras'] = Layout_linha_9['Embaladeiras'].replace(' ','0')
    Layout_linha_9['Embaladeiras'] = Layout_linha_9['Embaladeiras'].astype(float)

    Layout_linha_9['Embaladeiras_1'] = Layout_linha_9['Embaladeiras_1'].replace(' ','0')
    Layout_linha_9['Embaladeiras_1'] = Layout_linha_9['Embaladeiras_1'].astype(float)

    Layout_linha_9['Embaladeiras_2'] = Layout_linha_9['Embaladeiras_2'].replace(' ','0')
    Layout_linha_9['Embaladeiras_2'] = Layout_linha_9['Embaladeiras_2'].astype(float)

##################################### DATASET EMBALADEIRAS #######################################################################

    
    padrao_embaldeiras['PESSOA'] = padrao_embaldeiras['PESSOA'].str[6:]
    #padrao_embaldeiras
##################################### DATASET EMBALADEIRAS #######################################################################


    #filtro_melhor = padrao_embaldeiras['Cenario'] == 'Melhor'
    #padrao_embaldeiras = padrao_embaldeiras[filtro_melhor]

    def correcao_variedade(padrao_embaldeiras):
        if padrao_embaldeiras['VARIEDADE'] == 'Tommy ':
            return 'Tommy Atkins'
        elif padrao_embaldeiras['VARIEDADE'] == 'Keitt ':
            return 'Keitt'
        else:
            return padrao_embaldeiras['VARIEDADE']
    padrao_embaldeiras['VARIEDADE'] = padrao_embaldeiras.apply(correcao_variedade, axis = 1)
    
    import plotly.express as px

    #st.write('As melhores embaladeiras para cada calibre da variedade',variedade, 'podem ser consultadas nas tabelas abaixo:')
    def check_valores(Layout_linha_9, list_values):
        resultDict = {}
        for elem in list_values:
            if elem in Layout_linha_9['Calibre'] and variedade == 'Palmer':
                resultDict[elem] = True

                aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                aaa = aaa.reset_index()
                #aaa

                bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                bbb = bbb.reset_index()
                bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})
                #bbb
                ccc = pd.concat((aaa,bbb))
                ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                ccc['Calibre'] = ccc['Calibre'].astype(float)
                ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                ccc = ccc.reset_index()
                #ccc
                
                if elem == 5.0:
                    #kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    #kl1 = round(kl1,0)

                    #if kl1 == 0:
                    #    kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    #elif kl1 > 0: 
                    #    kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                    #    kl = kl.astype(int)
                    #kl
                    #ccc

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']


                    a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                    a = a.reset_index()
                    a['mean'] = round(a['mean'],0)
                    a = a.rename(columns = {'mean':'Caixas/Hora'})
                    a['Calibre'] = 5.0
                    a['Calibre'] = a['Calibre'].astype(str)
                    a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)
                    media_a = a['Caixas/Hora'].mean()
                    st.session_state.media_a = media_a
                    aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 5',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                    aa.add_hline(229)
                    aa.update_layout(height = 350, width = 350)
                    

                elif elem == 6.0:
                    
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]



                    b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    b = b.reset_index()
                    b['mean'] = round(b['mean'],0)
                    b = b.rename(columns = {'mean':'Caixas/Hora'})
                    b['Calibre'] = 6.0
                    b['Calibre'] = b['Calibre'].astype(str)
                    b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                    media_b = b['Caixas/Hora'].mean()
                    st.session_state.media_b = media_b
                    bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                    bb.add_hline(media_b, line_color="green")
                    #bb.add_vrect(x0=0.9, x1=2)
                    bb.add_hline(169)
                    bb.update_layout(height = 350, width = 350)

                elif elem == 7.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl
                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']



                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]





                    c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    c = c.reset_index()
                    c['mean'] = round(c['mean'],0)
                    c = c.rename(columns = {'mean':'Caixas/Hora'})
                    c['Calibre'] = 7.0
                    c['Calibre'] = c['Calibre'].astype(str)
                    c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                    media_c = c['Caixas/Hora'].mean()
                    st.session_state.media_c = media_c
                    cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 7',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])

                    cc.add_hline(174)

                    cc.update_layout(height = 350, width = 350)

                elif elem == 8.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]





                    d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    d = d.reset_index()
                    d['mean'] = round(d['mean'],0)
                    d = d.rename(columns = {'mean':'Caixas/Hora'})
                    d['Calibre'] = 8.0
                    d['Calibre'] = d['Calibre'].astype(str)
                    d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)
                    media_d = d['Caixas/Hora'].mean()
                    st.session_state.media_d = media_d
                    dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                    dd.add_hline(189)
                    dd.update_layout(height = 350, width = 350)
                    

                elif elem == 9.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0) 
                        kl = kl.astype(int)

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    
            
                    ## nesse intervalo aqui tenho que retirar os valores que estão dentro do calibre anteiror
                    # padrao emabaldeiras aqui não pode conter o mesmo ID do c anterior


                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]



                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    e = e.reset_index()
                    e['mean'] = round(e['mean'],0)
                    e = e.rename(columns = {'mean':'Caixas/Hora'})
                    e['Calibre'] = 9.0
                    e['Calibre'] = e['Calibre'].astype(str)
                    #e['ID_PESSOA'] = e['ID_PESSOA'].astype(str)
                    media_e = e['Caixas/Hora'].mean()
                    st.session_state.media_e = media_e
                    ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 9',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                    ee.add_hline(157)
                    ee.update_layout(height = 350, width = 350)

                elif elem == 10.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    
                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]







                    f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    f = f.reset_index()
                    f['mean'] = round(f['mean'],0)
                    f = f.rename(columns = {'mean':'Caixas/Hora'})
                    f['Calibre'] = 10.0
                    f['Calibre'] = f['Calibre'].astype(str)
                    f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)
                    media_f = f['Caixas/Hora'].mean()
                    st.session_state.media_f = media_f
                    ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 10', hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                    ff.add_hline(139)
                    ff.update_layout(height = 350, width = 350)
                    
                    
                
                elif elem == 12.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]




                    g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    g = g.reset_index()
                    g['mean'] = round(g['mean'],0)
                    g = g.rename(columns = {'mean':'Caixas/Hora'})
                    g['Calibre'] = 12.0
                    g['Calibre'] = g['Calibre'].astype(str)
                    g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)
                    media_g = g['Caixas/Hora'].mean()
                    st.session_state.media_g = media_g
                    gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 12',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                    gg.add_hline(149)
                    gg.update_layout(height = 350, width = 350)
                
                elif elem == 14.0:

                    #kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    #kl = round(kl,0)
                    #kl = kl.astype(int)
                    #kl = kl + 3
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                    h = h.reset_index()
                    h['mean'] = round(h['mean'],0)
                    h = h.rename(columns = {'mean':'Caixas/Hora'})
                    h['Calibre'] = 14.0
                    h['Calibre'] = h['Calibre'].astype(str)
                    h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
                    media_h = h['Caixas/Hora'].mean()
                    st.session_state.media_h = media_h
                    hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                    hh.update_layout(height = 350, width = 350)



            elif elem in Layout_linha_9['Calibre'] and variedade == 'Kent':
                resultDict[elem] = True
                #bbb = Layout_linha_9.groupby('Calibre2')['Embaladeiras'].sum()
                #bbb
                aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                aaa = aaa.reset_index()
                #aaa

                bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                bbb = bbb.reset_index()
                bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})
                #bbb
                ccc = pd.concat((aaa,bbb))
                ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                ccc['Calibre'] = ccc['Calibre'].astype(float)
                ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                ccc = ccc.reset_index()

                if elem == 5.0:
                    #kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    #kl1 = round(kl1,0)

                    #if kl1 == 0:
                    #    kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    #elif kl1 > 0: 
                    #    kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                    #    kl = kl.astype(int)
                    #kl
                    #ccc

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    a = a.reset_index()
                    a['mean'] = round(a['mean'],0)
                    a = a.rename(columns = {'mean':'Caixas/Hora'})
                    a['Calibre'] = 5.0
                    a['Calibre'] = a['Calibre'].astype(str)
                    a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)
                    aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 5',hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                    
                    aa.update_layout(height = 350, width = 350)

                elif elem == 6.0:
                    
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]
                    
                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']


                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]


                    b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    b = b.reset_index()
                    b['mean'] = round(b['mean'],0)
                    b = b.rename(columns = {'mean':'Caixas/Hora'})
                    b['Calibre'] = 6.0
                    b['Calibre'] = b['Calibre'].astype(str)
                    b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                    bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 6',hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                    bb.update_layout(height = 350, width = 350)

                elif elem == 7.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]


                    c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    c = c.reset_index()
                    c['mean'] = round(c['mean'],0)
                    c = c.rename(columns = {'mean':'Caixas/Hora'})
                    c['Calibre'] = 7.0
                    c['Calibre'] = c['Calibre'].astype(str)
                    c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                    cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 7', hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                    cc.update_layout(height = 350, width = 350)
                
                elif elem == 8.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int) 
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]


                    d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    d = d.reset_index()
                    d['mean'] = round(d['mean'],0)
                    d = d.rename(columns = {'mean':'Caixas/Hora'})
                    d['Calibre'] = 8.0
                    d['Calibre'] = d['Calibre'].astype(str)
                    d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)
                    dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 8', hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                    dd.update_layout(height = 350, width = 350)
                
                elif elem == 9.0:


                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]


                    e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    e = e.reset_index()
                    e['mean'] = round(e['mean'],0)
                    e = e.rename(columns = {'mean':'Caixas/Hora'})
                    e['Calibre'] = 9.0
                    e['Calibre'] = e['Calibre'].astype(str)
                    e['ID_PESSOA'] = e['ID_PESSOA'].astype(str)
                    ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 9' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                    ee.update_layout(height = 350, width = 350)
                
                elif elem == 10.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]




                    f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    f = f.reset_index()
                    f['mean'] = round(f['mean'],0)
                    f = f.rename(columns = {'mean':'Caixas/Hora'})
                    f['Calibre'] = 10.0
                    f['Calibre'] = f['Calibre'].astype(str)
                    f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)
                    ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 10' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                    ff.update_layout(height = 350, width = 350)
                
                elif elem == 12.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]


                    g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    g = g.reset_index()
                    g['mean'] = round(g['mean'],0)
                    g = g.rename(columns = {'mean':'Caixas/Hora'})
                    g['Calibre'] = 12.0
                    g['Calibre'] = g['Calibre'].astype(str)
                    g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)
                    gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 12',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                    gg.update_layout(height = 350, width = 350)
                
                elif elem == 14.0:

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                    h = h.reset_index()
                    h['mean'] = round(h['mean'],0)
                    h = h.rename(columns = {'mean':'Caixas/Hora'})
                    h['Calibre'] = 14.0
                    h['Calibre'] = h['Calibre'].astype(str)
                    h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
                    hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )

                    hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                    hh.update_layout(height = 350, width = 350)
            elif elem in Layout_linha_9['Calibre'] and variedade == 'Keitt':
                resultDict[elem] = True
                aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                aaa = aaa.reset_index()
                #aaa

                bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                bbb = bbb.reset_index()
                bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})
                #bbb
                ccc = pd.concat((aaa,bbb))
                ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                ccc['Calibre'] = ccc['Calibre'].astype(float)
                ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                ccc = ccc.reset_index()
                #ccc

                if elem == 5.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl
                    #ccc

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    a = a.reset_index()
                    a['mean'] = round(a['mean'],0)
                    a = a.rename(columns = {'mean':'Caixas/Hora'})
                    a['Calibre'] = 5.0
                    a['Calibre'] = a['Calibre'].astype(str)
                    a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)

                    media_a = a['Caixas/Hora'].mean()
                    st.session_state.media_a = media_a

                    aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 5',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                    aa.add_hline(517)
                    aa.update_layout(height = 350, width = 350)

                elif elem == 6.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]


                    b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    b = b.reset_index()
                    b['mean'] = round(b['mean'],0)
                    b = b.rename(columns = {'mean':'Caixas/Hora'})
                    b['Calibre'] = 6.0
                    b['Calibre'] = b['Calibre'].astype(str)
                    b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                    media_b = b['Caixas/Hora'].mean()
                    st.session_state.media_b = media_b
                    bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                    bb.add_hline(412)
                    bb.update_layout(height = 350, width = 350)

                elif elem == 7.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]


                    c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    c = c.reset_index()
                    c['mean'] = round(c['mean'],0)
                    c = c.rename(columns = {'mean':'Caixas/Hora'})
                    c['Calibre'] = 7.0
                    c['Calibre'] = c['Calibre'].astype(str)
                    c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                    media_c = c['Caixas/Hora'].mean()
                    st.session_state.media_c = media_c
                    cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 7',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                    cc.add_hline(321)
                    cc.update_layout(height = 350, width = 350)

                elif elem == 8.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]





                    d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    d = d.reset_index()
                    d['mean'] = round(d['mean'],0)
                    d = d.rename(columns = {'mean':'Caixas/Hora'})
                    d['Calibre'] = 8.0
                    d['Calibre'] = d['Calibre'].astype(str)
                    d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)
                    media_d = d['Caixas/Hora'].mean()
                    st.session_state.media_d = media_d
                    dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA',title = 'Keitt - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                    dd.add_hline(301)
                    dd.update_layout(height = 350, width = 350)

                elif elem == 9.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]



                    e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    e = e.reset_index()
                    e['mean'] = round(e['mean'],0)
                    e = e.rename(columns = {'mean':'Caixas/Hora'})
                    e['Calibre'] = 9.0
                    e['Calibre'] = e['Calibre'].astype(str)
                    e['ID_PESSOA'] = e['ID_PESSOA'].astype(str)
                    media_e = e['Caixas/Hora'].mean()
                    st.session_state.media_e = media_e
                    ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 9' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                    ee.add_hline(257)
                    ee.update_layout(height = 350, width = 350)
                elif elem == 10.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]


                    f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    f = f.reset_index()
                    f['mean'] = round(f['mean'],0)
                    f = f.rename(columns = {'mean':'Caixas/Hora'})
                    f['Calibre'] = 10.0
                    f['Calibre'] = f['Calibre'].astype(str)
                    f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)
                    media_f = f['Caixas/Hora'].mean()
                    st.session_state.media_f = media_f
                    ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 10',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                    ff.add_hline(261)
                    ff.update_layout(height = 350, width = 350)
                elif elem == 12.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]

                    
                    g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    g = g.reset_index()
                    g['mean'] = round(g['mean'],0)
                    g = g.rename(columns = {'mean':'Caixas/Hora'})
                    g['Calibre'] = 12.0
                    g['Calibre'] = g['Calibre'].astype(str)
                    g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)
                    media_g = g['Caixas/Hora'].mean()
                    st.session_state.media_g = media_g
                    gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 12' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                    gg.add_hline(253)
                    gg.update_layout(height = 350, width = 350)
                elif elem == 14.0:
                    #kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    #kl = round(kl,0)
                    #kl = kl.astype(int)
                    #kl = kl 
                    #kl
                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                    h = h.reset_index()
                    h['mean'] = round(h['mean'],0)
                    h = h.rename(columns = {'mean':'Caixas/Hora'})
                    h['Calibre'] = 14.0
                    h['Calibre'] = h['Calibre'].astype(str)
                    h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
                    media_h = h['Caixas/Hora'].mean()
                    st.session_state.media_h = media_h
                    hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                    hh.update_layout(height = 350, width = 350)

            elif elem in Layout_linha_9['Calibre'] and variedade == 'Tommy Atkins':
                resultDict[elem] = True

                aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                aaa = aaa.reset_index()
                #aaa

                bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                bbb = bbb.reset_index()
                bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})
                #bbb
                ccc = pd.concat((aaa,bbb))
                ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                ccc['Calibre'] = ccc['Calibre'].astype(float)
                ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                ccc = ccc.reset_index()
                #ccc
                #ccc

                if elem == 5.0:

                    #kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    #kl1 = round(kl1,0)

                    #if kl1 == 0:
                    #    kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    #elif kl1 > 0: 
                    #    kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                    #    kl = kl.astype(int)
                    #kl
                    #ccc

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                    a = a.reset_index()
                    a['mean'] = round(a['mean'],0)
                    a = a.rename(columns = {'mean':'Caixas/Hora'})
                    a['Calibre'] = 5.0
                    a['Calibre'] = a['Calibre'].astype(str)
                    a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)

                    media_a = a['Caixas/Hora'].mean()
                    st.session_state.media_a = media_a

                    aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 5',hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                    aa.add_hline(235)
                    aa.update_layout(height = 350, width = 350)

                elif elem == 6.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]

                    b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    b = b.reset_index()
                    b['mean'] = round(b['mean'],0)
                    b = b.rename(columns = {'mean':'Caixas/Hora'})
                    b['Calibre'] = 6.0
                    b['Calibre'] = b['Calibre'].astype(str)
                    b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                    media_b = b['Caixas/Hora'].mean()
                    st.session_state.media_b = media_b


                    bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                    bb.add_hline(178)
                    bb.update_layout(height = 350, width = 350)

                elif elem == 7.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]





                    c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    c = c.reset_index()
                    c['mean'] = round(c['mean'],0)
                    c = c.rename(columns = {'mean':'Caixas/Hora'})
                    c['Calibre'] = 7.0
                    c['Calibre'] = c['Calibre'].astype(str)
                    c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                    media_c = c['Caixas/Hora'].mean()
                    st.session_state.media_c = media_c

                    cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 7', hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                    cc.add_hline(185)
                    cc.update_layout(height = 350, width = 350)

                elif elem == 8.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    d = d.reset_index()
                    d['mean'] = round(d['mean'],0)
                    d = d.rename(columns = {'mean':'Caixas/Hora'})
                    d['Calibre'] = 8.0
                    d['Calibre'] = d['Calibre'].astype(str)
                    d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)

                    media_d = d['Caixas/Hora'].mean()
                    st.session_state.media_d = media_d

                    
                    dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                    dd.add_hline(195)
                    dd.update_layout(height = 350, width = 350)

                elif elem == 9.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    e = e.reset_index()
                    e['mean'] = round(e['mean'],0)
                    e = e.rename(columns = {'mean':'Caixas/Hora'})
                    e['Calibre'] = 9.0
                    e['Calibre'] = e['Calibre'].astype(str)
                    e['ID_PESSOA'] = e['ID_PESSOA'].astype(str)

                    media_e = e['Caixas/Hora'].mean()
                    st.session_state.media_e = media_e

                    ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 9',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                    ee.add_hline(154)
                    ee.update_layout(height = 350, width = 350)

                elif elem == 10.0:
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                    f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    f = f.reset_index()
                    f['mean'] = round(f['mean'],0)
                    f = f.rename(columns = {'mean':'Caixas/Hora'})
                    f['Calibre'] = 10.0
                    f['Calibre'] = f['Calibre'].astype(str)
                    f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)

                    media_f = f['Caixas/Hora'].mean()
                    st.session_state.media_f = media_f

                    ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 10',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                    ff.add_hline(144)
                    ff.update_layout(height = 350, width = 350)

                elif elem == 12.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)
                    
                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']

                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]

                    g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    g = g.reset_index()
                    g['mean'] = round(g['mean'],0)
                    g = g.rename(columns = {'mean':'Caixas/Hora'})
                    g['Calibre'] = 12.0
                    g['Calibre'] = g['Calibre'].astype(str)
                    g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)

                    media_g = g['Caixas/Hora'].mean()
                    st.session_state.media_g = media_g

                    gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins  - Calibre 12',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                    gg.add_hline(158)
                    gg.update_layout(height = 350, width = 350)

                elif elem == 14.0:

                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)
                    
                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                    padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                    padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]
                    padrao_embaldeiras_palmer_8 = padrao_embaldeiras_palmer_7[~padrao_embaldeiras_palmer_7.ID_PESSOA.isin(g['ID_PESSOA'])]

                    h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    h = h.reset_index()
                    h['mean'] = round(h['mean'],0)
                    h = h.rename(columns = {'mean':'Caixas/Hora'})
                    h['Calibre'] = 14.0
                    h['Calibre'] = h['Calibre'].astype(str)
                    h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)

                    media_h = h['Caixas/Hora'].mean()
                    st.session_state.media_h = media_h

                    hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                    hh.add_hline(90)
                    hh.update_layout(height = 350, width = 350)


            else:
                resultDict[elem] = False

        return colu1.write(aa), colu1.write(bb), colu2.write(cc), colu2.write(dd), colu3.write(ee), colu3.write(ff), colu4.write(gg), colu4.write(hh)
    #st.write('As melhores embaladeiras para cada calibre da variedade',variedade, 'podem ser consultadas nas tabelas abaixo:')
    result = check_valores(Layout_linha_9, [5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0])
    result
    media_a = st.session_state.media_a
    media_b = st.session_state.media_b
    media_c = st.session_state.media_c
    media_d = st.session_state.media_d
    media_e = st.session_state.media_e
    media_f = st.session_state.media_f
    media_g = st.session_state.media_g
    media_h = st.session_state.media_h

    def ritmo(b):
        if b['Calibre'] == 5:
            return media_a
        elif b['Calibre'] == 6:
            return media_b
        elif b['Calibre'] == 7:
            return media_c
        elif b['Calibre'] == 8:
            return media_d
        elif b['Calibre'] == 9:
            return media_e
        elif b['Calibre'] == 10:
            return media_f
        elif b['Calibre'] == 12:
            return media_g
        elif b['Calibre'] == 14:
            return media_h
        else:
            return 'NADA'

    b['Ritmo_embaladeira'] = b.apply(ritmo, axis = 1) 
    filtro = b['Ritmo_embaladeira'] != 'NADA'
    b = b[filtro]

    b['Horas_4kg_embaladeiras'] = (b['Caixas_total'] / b['Ritmo_embaladeira']) / produtividade_embaladeira 
    ton_horas_embaladeiras = round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg_embaladeiras'].sum()/embaladeira),2)


    with col3:
        Layout_linha_9 = Layout_linha_9.fillna(' ')
        Layout_linha_9['Qualidade'] = Layout_linha_9['Qualidade'].astype(str)
        Layout_linha_9['Qualidade2'] = Layout_linha_9['Qualidade2'].astype(str)
        #Layout_linha_9 = Layout_linha_9.fillna(' ')
        Layout_linha_9['Calibre - Qualidade'] = Layout_linha_9['Calibre'] + '-' +Layout_linha_9['Qualidade'] + ' '+ '/' + ' ' + Layout_linha_9['Calibre2'] + '-' + Layout_linha_9['Qualidade2']
        Layout_linha_9['Embaladeiras'] = round(Layout_linha_9['Embaladeiras'],1)

        st.error('##### Embaladeiras por linha de embalagem:')

        fig4 = px.bar(Layout_linha_9, x = 'Linha', y = 'Embaladeiras', color = 'Calibre - Qualidade', text = 'Embaladeiras',color_discrete_sequence= px.colors.sequential.Oranges ,
        category_orders={"Calibre":['5.0','6.0','7.0','8.0','9.0','10.0','12.0','14.0']}, hover_name = 'Linha')
        fig4.update_layout(height = 450, width = 550, uniformtext_minsize=10, uniformtext_mode='show', font = dict(size = 15))
        fig4.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)
        
        st.plotly_chart(fig4)

    with col1:
        import plotly.graph_objects as go

        b['Calibre Name'] = b['Calibre'].astype(str)
        c = round(b['Percentual'],2)
        #fig = px.bar(b, x = 'Calibre Name',y = 'Percentual', color = 'Calibre Name', title = 'Distribuição de calibres:', text = c)
        #fig.update_layout(height = 450, width = 550,uniformtext_minsize=8, uniformtext_mode='show')
        #fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

        st.error('##### Concentração de calibres:')

        fig = go.Figure(data=[go.Pie(labels = b['Calibre Name'], values = b['Percentual'], marker_colors = px.colors.sequential.Oranges ,hole = .35, pull=0.01)])
        #fig = px.pie(b, names = 'Calibre Name', values = 'Percentual', hole = .35)
        fig.update_traces(textinfo='label+percent', textfont_size=15, textposition="inside")
        fig.update_layout(height = 450, width = 450, font = dict(size = 15))
        #fig.update_traces(textinfo='label+percent', textfont_size=20, textposition="inside")
        st.plotly_chart(fig)
        


    with col2:
        aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
        aaa = aaa.reset_index()
        #aaa

        bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
        bbb = bbb.reset_index()
        bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})
        #bbb
        ccc = pd.concat((aaa,bbb))
        #ccc
        ccc['Calibre'] = ccc['Calibre'].replace(' ',0)
        drop_2 = ccc[ccc['Calibre'] == 0 ].index
        ccc2 = ccc.drop(drop_2, inplace = True)
        #drop_3 = ccc[ccc['Calibre'] == '2.0'].index
        #ccc.drop(drop_3, inplace = True)
        ccc['Embaladeiras_1'] = round(ccc['Embaladeiras_1'],1)
        #ccc
        st.error('##### Quantidade de embaladeiras por calibre:')

        fig = px.bar(ccc, y = 'Calibre', x = 'Embaladeiras_1', color = 'Calibre',
        category_orders = {'Calibre':['2.0','5.0','6.0','7.0','8.0','9.0','10.0','12.0','14.0']}, text = 'Embaladeiras_1', color_discrete_sequence= px.colors.sequential.Oranges)
        fig.update_layout(height = 450, width = 500,uniformtext_minsize=8, uniformtext_mode='show', font = dict(size = 15))
    #    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False, marker_line_width=1.5)
        fig
    
    conta_delta = round(((100 * ton_horas_embaladeiras) / ton_horas) - 100,1)

    col4x.metric(label="Nova capacidade de Toneladas/Hora", value= ton_horas_embaladeiras, delta= conta_delta)
    st.info('### ER atual vs ER embaladeiras selecionadas')
    #b
    dataframe = b[['Calibre','Percentual','Caixas_total','Ritmo','Horas_4kg','Ritmo_embaladeira','Horas_4kg_embaladeiras']]

    dataframe.rename(columns = {'Ritmo':'Ritmo Atual','Ritmo_embaladeira':'Ritmo Embaladeiras',
                                'Horas_4kg_embaladeiras':'Horas Embaladeiras','Caixas_total':'Total de caixas',
                                'Horas_4kg':'Horas Atual'}, inplace = True)
    dataframe['Controle'] = controle2
    dataframe

    st.download_button( label = 'Baixar Planilha',data = dataframe.to_csv(), mime = 'text/csv')
