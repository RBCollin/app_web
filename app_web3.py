
from math import ceil
import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(layout="wide")
#dataset = pd.read_excel('Planilha Denilton.xlsx')
#st.write('Recarregue para um novo controle')
#if st.button('Recarregar'):
 #   st.experimental_rerun()
######################################################## PLANILHA QUE SUBSTITUI OS INPUTS ########################################################



#random_qualidade = np.random.randint(1, 4, size=150)
#planilha_inputs = pd.DataFrame(random_qualidade, columns = ['Qualidade'])
#planilha_inputs = planilha_inputs.reset_index()
#planilha_inputs = planilha_inputs.rename(columns = {'index':'Fruto'})
#random_peso = np.random.randint(289,870,size = 150)
#planilha_inputs['Peso'] = random_peso
        
#planilha_inputs['Calibre'] = planilha_inputs.apply(calibre, axis = 1)
#dataset = planilha_inputs 
#dataset['Embaladeiras'] = 52
#dataset['Caixotes'] = 504

#dataset['Variedade'] = np.random.randint(5,109) 
#dataset['Variedade'] = 'Palmer'

#dataset.to_excel('Planilha_teste.xlsx')
#dataset

#################### VOU DEIXAR COMO INPUT O PERIODO DE SAFRA E O NUMERO DE EMBALADEIRAS  ####################

coluna_inicial_1, coluna_inicial_2 = st.columns([0.8,1])
with coluna_inicial_1:
    st.title('Packing House - Linhas de Embalagem')

with coluna_inicial_2:
    st.write('')
    st.write('')
    if st.button('Atualizar Controle'):
        url = 'http://177.52.21.58:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_BALANCEAMENTO_PH'
        url_embaladeiras_ativas = 'http://177.52.21.58:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_EMB_ATIVAS'
        st.session_state.url = url
        st.session_state.url_embala = url_embaladeiras_ativas

url =  st.session_state.url 
variaveis_df = pd.read_json(url)


#variaveis_df = pd.read_json("http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_BALANCEAMENTO_PH") 

#variaveis_df

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
#variaveis_df


def calibre(variaveis_df):
    if variaveis_df['PESO'] > 886:
        return '4'
    elif variaveis_df['PESO'] < 885 and variaveis_df['PESO'] >= 751:
        return '5'
    elif variaveis_df['PESO'] < 751 and variaveis_df['PESO'] >= 631:
        return '6'
    elif variaveis_df['PESO'] < 631 and variaveis_df['PESO'] >= 561:
        return '7'
    elif variaveis_df['PESO'] < 561 and variaveis_df['PESO'] >= 471:
        return '8'
    elif variaveis_df['PESO'] < 471 and variaveis_df['PESO'] >= 430:
        return '9'
    elif variaveis_df['PESO'] < 430 and variaveis_df['PESO'] >= 375:
        return '10'
    elif variaveis_df['PESO'] < 375 and variaveis_df['PESO'] >= 294:
        return '12'
    elif variaveis_df['PESO'] < 294 and variaveis_df['PESO'] >= 278:
        return '14'
    elif variaveis_df['PESO'] <= 278:
        return '16'
    else:
        'Refugo'

variaveis_df['CALIBRE'] = variaveis_df.apply(calibre, axis =1)
#variaveis_df

## melhor mudar s colunas do  df atual para opadrao do codgigo, e nao ao cnotratio

######################################################## PLANILHA QUE SUBSTITUI OS INPUTS ########################################################
dataset = variaveis_df
dataset.rename(columns = {"PESO":"Peso","CALIBRE":"Calibre","NUMERO_FRUTO":"Fruto","QUALIDADE":"Qualidade","VARIEDADE":"Variedade"}, inplace = True)


avg_frutos_caixotes = dataset['N_CAIXOTE'].value_counts().sum() / len(dataset['N_CAIXOTE'].value_counts())
#avg_frutos_caixotes


Caixotes = dataset['CONTENTORES'][0].item()
VARIEDADE = dataset['Variedade'][0]

######################################################## PLANILHA QUE SUBSTITUI OS INPUTS ########################################################

#dataset
filtro = dataset['Qualidade'] != 4
dataset = dataset[filtro]

dataset['Calibre'] = dataset['Calibre'].astype(int)
a = dataset['Calibre'].value_counts() / dataset['Calibre'].count()
b = pd.DataFrame(a)
b = b.reset_index()
b.columns = ['Calibre', 'Percentual']
b['Percentual'] = b['Percentual']*100
b = b.sort_values('Calibre')


filtro2 = dataset['Qualidade'] != 4
dataset_2 = dataset[filtro2]
aa = pd.DataFrame(dataset_2['Calibre'].value_counts())
aa = aa.reset_index()
aa.columns = ['Calibre','Qtde_mangas']
b['Caixas'] = aa['Qtde_mangas'] / aa['Calibre']

############################################## Considerando QUALIDADE ##############################################

quality = dataset['Qualidade'].value_counts() / dataset['Qualidade'].count()

quality = pd.DataFrame(quality)
quality = quality.reset_index()
quality.columns = ['Qualidade','Percent']


primeira_percent = quality[quality.Qualidade==1].Percent.item()
segunda_percent = quality[quality.Qualidade==2].Percent.item()
terceira_percent = quality[quality.Qualidade==3].Percent.item()

#st.title('Packing House - Linhas de Embalagem')
#st.markdown('___________________')

#avg_frutos_caixotes 

produtividade_embaladeira = 0.75
produtividade_talo = 0.80
produtividade_limpeza = 0.75
caixotes = Caixotes
variedade = VARIEDADE 
#b['Calibre'] == 5






padrao_embaldeiras_total = pd.read_excel('padrao_embaladeiras_TUDO_cenarios.xlsx')

url_embaladeiras_ativas = st.session_state.url_embala 

df_embaladeiras_ativas = pd.read_json(url_embaladeiras_ativas)
df_embaladeiras_ativas.rename(columns = {'CPF':'MATRICULA'}, inplace = True)
    
df_222 = df_embaladeiras_ativas.merge(padrao_embaldeiras_total)
padrao_embaldeiras = df_222

embaladeira = len(padrao_embaldeiras.groupby('PESSOA'))
Programa_input = 'Entre Safra'
st.session_state.emba_aviso = embaladeira



coluna1, coluna2 = st.columns(2)

#if controle not in st.session_state:   
    #st.session_state.controle = 0
#st.write(st.session_state.controle)

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

    #if st.button('Novo controle'):
        #dataset['Controle'] = np.random.randint(5,109)                  ######################################################## CONTORLE
    controle = variaveis_df['CONTROLE'][0]
    st.session_state.controle = controle

    #st.session_state.controle = controle
    controle2 = st.session_state.controle
    st.metric(label="Controle", value= controle2, delta= VARIEDADE)  
    #st.write('A variedade é', VARIEDADE,'e controle:',controle2)

    col2, col3 = st.columns([0.30,1])
    #col1.subheader('Selecione a variedade de manga:')
    #variedade = col1.selectbox('',['Keitt','Kent','Palmer','Tommy Atkins'])
    emba_aviso = st.session_state.emba_aviso
    #st.write('Balanceamento feito com a quantidade total de embaladeiras ativas:',emba_aviso)

    with st.form(key='planilha'):
        ## armazendnado em uma variavdl
        coluna1_1, coluna2_2,coluna3_3 = st.columns([0.35,1,1])
    #    coluna1_1.subheader("""Quantidade de embaladeiras disponíveis:""")
        embaladeira_input = coluna1_1.number_input(label = 'Ajuste a quantidade de embaladeiras:', value = emba_aviso  , format = "%d", step = 1)
        #fazenda = st.selectbox('Selecione a sua fazenda:', ['Bom Jesus','Brandões'
        #coluna1_1.subheader(' Selecione o período:')
        Programa_input_2 = coluna1_1.selectbox('Selecione o período:', ['Entre Safra','Safra'])
        button_submit = coluna1_1.form_submit_button('Calcular')

    if button_submit:
        embaladeira =  embaladeira_input
        Programa_input = Programa_input_2

    def ritmo(b):
            if b['Calibre'] == 5 and variedade == 'Palmer':
                return 229
            elif b['Calibre'] == 6 and variedade == 'Palmer':
                return 169
            elif b['Calibre'] == 7 and variedade == 'Palmer':
                return 174
            elif b['Calibre'] == 8 and variedade == 'Palmer':
                return 191
            elif b['Calibre'] == 9 and variedade == 'Palmer':
                return 157
            elif b['Calibre'] == 10 and variedade == 'Palmer':
                return 139
            elif b['Calibre'] == 12 and variedade == 'Palmer':
                return 149
            elif b['Calibre'] == 14 and variedade == 'Palmer':
                return 85
    ################################################## Keitt #############################################################
            elif b['Calibre'] == 5 and variedade == 'Keitt':
                return 517
            elif b['Calibre'] == 6 and variedade == 'Keitt':
                return 412
            elif b['Calibre'] == 7 and variedade == 'Keitt':
                return 321
            elif b['Calibre'] == 8 and variedade == 'Keitt':
                return 301
            elif b['Calibre'] == 9 and variedade == 'Keitt':
                return 257
            elif b['Calibre'] == 10 and variedade == 'Keitt':
                return 261
            elif b['Calibre'] == 12 and variedade == 'Keitt':
                return 253
            elif b['Calibre'] == 14 and variedade == 'Keitt':
                return 220

    ################################################## Kent #############################################################
    #### Valores da Kent na planilha são iguais ao da Keitt
    #### Encontrei anteriormente no estudo das embaladerias que o ritmo era bem parecido com o da Keitt porém com pequenas diferenças
    #### por isso vou considerar os ritmos iguais aos do estudo e não iguais aos da Keitt

            elif b['Calibre'] == 5 and variedade == 'Kent':
                return 510
            elif b['Calibre'] == 6 and variedade == 'Kent':
                return 410
            elif b['Calibre'] == 7 and variedade == 'Kent':
                return 314
            elif b['Calibre'] == 8 and variedade == 'Kent':
                return 300
            elif b['Calibre'] == 9 and variedade == 'Kent':
                return 253
            elif b['Calibre'] == 10 and variedade == 'Kent':
                return 248
            elif b['Calibre'] == 12 and variedade == 'Kent':
                return 246
            elif b['Calibre'] == 14 and variedade == 'Kent':
                return 200

    ################################################## Tommy #############################################################
            elif b['Calibre'] == 5 and variedade == 'Tommy Atkins':
                return 235
            elif b['Calibre'] == 6 and variedade == 'Tommy Atkins':
                return 178
            elif b['Calibre'] == 7 and variedade == 'Tommy Atkins':
                return 185
            elif b['Calibre'] == 8 and variedade == 'Tommy Atkins':
                return 195
            elif b['Calibre'] == 9 and variedade == 'Tommy Atkins':
                return 154
            elif b['Calibre'] == 10 and variedade == 'Tommy Atkins':
                return 144
            elif b['Calibre'] == 12 and variedade == 'Tommy Atkins':
                return 158
            elif b['Calibre'] == 14 and variedade == 'Tommy Atkins':
                return 90
            else:
                return 'NADA'

    b['Ritmo'] = b.apply(ritmo, axis = 1)

    filtro_ritmo = b['Ritmo'] != 'NADA'
    b = b[filtro_ritmo]
        #b
        ########################################## Criando variaveis #######################################################################
        ############################################## INPUTS #######################################################################
    col1, col2,col3,col4 = st.columns([0.1,0.01,1,1.2])
    
    corte_talo = round(embaladeira / 3.33333)

    ##################################################################################################################################################
    
    b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100

    b['Caixas_1'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * primeira_percent) / b['Calibre']) 
    b['Caixas_2'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * segunda_percent)  / b['Calibre']) 
    b['Caixas_3'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * terceira_percent) / b['Calibre']) 
    #b['Caixas_Aereo'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * aereo_percent) / b['Calibre'])

    b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira    
    #b['Horas_aereo'] = (b['Caixas_Aereo'] / b['Ritmo_aereo']) / produtividade_embaladeira 


    #b['Horas_4kg'] = (b['Horas_4kg'] + b['Horas_aereo'].fillna(0))
    
    #############################################################################################################
        #import SessionState
    st.session_state.caixotes = caixotes
    st.session_state.embaladeira = embaladeira
    st.session_state.variedade = variedade
    st.session_state.periodo_safra = Programa_input 

    ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))
    ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))*100
    diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))

    corte_talo2 = corte_talo
    ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))
        
        
    def equilibrio(corte_talo, embaladeira):

                if (ritmo_talo) < (ritmo_embaladeira):
                    caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
                    #ritmo_talo_2
                    Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                    ton_horas = round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2)

                    st.write('#### Quantidade ideal de pessoas no talo:', corte_talo2)
                    st.write('#### Quantidade de pessoas na limpeza e seleção:', Limpeza_selecao)
                    st.write('#### Capacidade de Caixotes/Hora:', caixotes_hora)
                    st.write('#### Capacidade de Toneladas/Hora:', ton_horas)
                    st.session_state.caixotes_hora = caixotes_hora
                    st.session_state.ton_horas = ton_horas
                    #Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                    #Limpeza_selecao
                    #st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao)
                
            
                else :
                    caixotes_hora2 = round((caixotes*0.0416667)/(ritmo_talo))
                    Limpeza_selecao2 = round((caixotes_hora2 * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                    #caixotes_hora2 = round((caixotes*0.0416667)/(ritmo_talo))
                    st.write('#### Quantidade ideal de pessoas no talo:', round(corte_talo))
                    st.write('#### Quantidade de pessoas na limpeza e seleção:', Limpeza_selecao2)
                    st.write('#### Capacidade de Caixotes/Hora:', caixotes_hora2)
                    st.write('#### Capacidade de Toneladas/Hora:', ton_horas)
                    st.session_state.caixotes_hora = caixotes_hora2
                    st.session_state.ton_horas = ton_horas
                    #Limpeza_selecao2 = round((caixotes_hora2 * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                    #st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao2)

            #col1, col2 = st.columns(2)
            #st.write('A variedade selecionada foi:', variedade)
        #with col3:
        #        st.write('')
    with coluna2_2:
                #st.markdown('       ')
                #st.markdown("""__________________________________________""")
                st.success('#### Recomendação para balanceamento:')
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
    with coluna3_3:
                #st.markdown('       ')
                st.success('#### Distribuição de calibres:')
                #st.markdown('_____')
                import plotly.express as px
                b['Calibre Name'] = b['Calibre'].astype(str)
                c = round(b['Percentual'],2)
                fig = px.bar(b, x = 'Calibre Name',y = 'Percentual', color = 'Calibre Name', text = c, color_discrete_sequence= px.colors.sequential.Aggrnyl)
                fig.update_layout(height = 440, width = 750,
                uniformtext_minsize=8, uniformtext_mode='show',
                xaxis_title = "Calibre", font = dict(size = 16))
                fig.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)
                st.plotly_chart(fig) 


elif pagina_selecionada == 'Linhas de embalagem':

    caixotes_hora = st.session_state.caixotes_hora
    controle2 = st.session_state.controle
    ton_horas = st.session_state.ton_horas
    #caixotes_hora2 = st.session_state.caixotes_hora2 = caixotes_hora2
    col1, col2, col3, col4 = st.columns([0.5,1,1,1])
    col1.write("")
    col2.metric(label="Controle", value= controle2, delta= VARIEDADE)
    col3.metric(label="Caixotes/Hora", value= caixotes_hora, delta= None)
    col4.metric(label="Toneladas/Hora", value= ton_horas, delta= None)
    
    

    col11,col22, col33 = st.columns([0.015,0.5,0.5])
    coluna1, coluna2 = st.columns(2)

    col1, col2 = st.columns([0.01,1])
    
    #col11.write('##### Selecione o período:')
    #Programa_input = col11.selectbox(' ', ['Entre Safra','Safra'])
    #  
    Programa_input = st.session_state.periodo_safra

    caixotes = st.session_state.caixotes 
    embaladeira = st.session_state.embaladeira 
    variedade = st.session_state.variedade
    corte_talo = round(embaladeira / 3.33333)
    def ritmo(b):
        if b['Calibre'] == 5 and variedade == 'Palmer':
            return 229
        elif b['Calibre'] == 6 and variedade == 'Palmer':
            return 169
        elif b['Calibre'] == 7 and variedade == 'Palmer':
            return 174
        elif b['Calibre'] == 8 and variedade == 'Palmer':
            return 191
        elif b['Calibre'] == 9 and variedade == 'Palmer':
            return 157
        elif b['Calibre'] == 10 and variedade == 'Palmer':
            return 139
        elif b['Calibre'] == 12 and variedade == 'Palmer':
            return 149
        elif b['Calibre'] == 14 and variedade == 'Palmer':
            return 85
    ################################################## Keitt #############################################################

        elif b['Calibre'] == 5 and variedade == 'Keitt':
            return 517
        elif b['Calibre'] == 6 and variedade == 'Keitt':
            return 412
        elif b['Calibre'] == 7 and variedade == 'Keitt':
            return 321
        elif b['Calibre'] == 8 and variedade == 'Keitt':
            return 301
        elif b['Calibre'] == 9 and variedade == 'Keitt':
            return 257
        elif b['Calibre'] == 10 and variedade == 'Keitt':
            return 261
        elif b['Calibre'] == 12 and variedade == 'Keitt':
            return 253
        elif b['Calibre'] == 14 and variedade == 'Keitt':
            return 220

    ################################################## Kent #############################################################
    #### Valores da Kent na planilha são iguais ao da Keitt
    #### Encontrei anteriormente no estudo das embaladerias que o ritmo era bem parecido com o da Keitt porém com pequenas diferenças
    #### por isso vou considerar os ritmos iguais aos do estudo e não iguais aos da Keitt

        elif b['Calibre'] == 5 and variedade == 'Kent':
            return 510
        elif b['Calibre'] == 6 and variedade == 'Kent':
            return 410
        elif b['Calibre'] == 7 and variedade == 'Kent':
            return 314
        elif b['Calibre'] == 8 and variedade == 'Kent':
            return 300
        elif b['Calibre'] == 9 and variedade == 'Kent':
            return 253
        elif b['Calibre'] == 10 and variedade == 'Kent':
            return 248
        elif b['Calibre'] == 12 and variedade == 'Kent':
            return 246
        elif b['Calibre'] == 14 and variedade == 'Kent':
            return 200

    ################################################## Tommy #############################################################
        elif b['Calibre'] == 5 and variedade == 'Tommy Atkins':
            return 235
        elif b['Calibre'] == 6 and variedade == 'Tommy Atkins':
            return 178
        elif b['Calibre'] == 7 and variedade == 'Tommy Atkins':
            return 185
        elif b['Calibre'] == 8 and variedade == 'Tommy Atkins':
            return 195
        elif b['Calibre'] == 9 and variedade == 'Tommy Atkins':
            return 154
        elif b['Calibre'] == 10 and variedade == 'Tommy Atkins':
            return 144
        elif b['Calibre'] == 12 and variedade == 'Tommy Atkins':
            return 158
        elif b['Calibre'] == 14 and variedade == 'Tommy Atkins':
            return 90

        else:
            return 'NADA'

    b['Ritmo'] = b.apply(ritmo, axis = 1) 
 
    ##################################################################################################################################################
    
    b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100

    b['Caixas_1'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * primeira_percent) / b['Calibre']) 
    b['Caixas_2'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * segunda_percent)  / b['Calibre']) 
    b['Caixas_3'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * terceira_percent) / b['Calibre'])
    #b['Caixas_Aereo'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * aereo_percent) / b['Calibre'])
    #b['Caixas_aereo'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * aereo_percent) / b['Calibre'])  
    
    #b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira
    filtro_ritmo = b['Ritmo'] != 'NADA'
    b = b[filtro_ritmo]

    b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira   

    #b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira    
    #b['Horas_aereo'] = (b['Caixas_Aereo'] / b['Ritmo_aereo']) / produtividade_embaladeira
    #b['Horas_4kg'] = (b['Horas_4kg'] + b['Horas_aereo'].fillna(0))
    #b['Horas_aereo'] = b['Horas_aereo'].fillna(0)

    #b['Horas_aereo'] = (b['Caixas_Aereo'] / b['Ritmo_aereo']) / produtividade_embaladeira 
    #b['Horas_4kg'] = (b['Horas_4kg'] + b['Horas_aereo'])

    #b['Ritmo_aereo'] = b['Ritmo_aereo'] .fillna(1)
    #############################################################################################################


    #if#:
    ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))
    ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))*100
    diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))
    
    corte_talo2 = corte_talo
    ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))

    def equilibrio(corte_talo, embaladeira):

        if (ritmo_talo) < (ritmo_embaladeira):

            caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
                #caixotes_hora
            st.write("A quantidade ideal de pessoas no talo tem que ser:", corte_talo2)
            st.write('Capacidade de caixotes/hora no corte de talo é de:', caixotes_hora)
            st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
            Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                #Limpeza_selecao
            st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao)
            
        else :
            caixotes_hora2 = round((caixotes*0.0416667)/(ritmo_talo))
            st.write("A quantidade ideal de pessoas no talo tem que ser:", round(corte_talo))
            st.write('Capacidade de caixotes/hora no corte de talo é de:', caixotes_hora2)
            st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
            Limpeza_selecao2 = round((caixotes_hora2 * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
            st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao2)
    
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
        if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '12'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '12'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '5'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '5'
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
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '8'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '7'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '7'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '9'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '12'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '12'
################################################### PERIODO DE SAFRA ##################################################################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '14'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '14'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '9'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
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
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '10'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '9'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '9'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Aéreo'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Aéreo'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '6'
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
        if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
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
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'

        ################################################### PERIODO DE SAFRA ##################################################################################################
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
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
            return 'Refugo'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Aéreo'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt'):
            return 'Aéreo'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
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
        if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '6'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '14'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '14'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '7'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '7'

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
            return '6'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '14'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '14'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
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
            return '14'
        elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '14'
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
        if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '2'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return '1'
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
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
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '2'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt'):
            return '1'
        elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt'):
            return ''
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
    with col22:
        st.write(" ")
        st.info('##### Quantidade de embaladeiras por setor:')
        import plotly.express as px
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
        Layout_linha_8 = Layout_linha_7[['Linha','Calibre','Qualidade','Calibre2','Qualidade2','Frutos','Frutos2','Caixas','Caixas2','Embaladeiras','Setores','Embaladeiras_1','Embaladeiras_2']]
        Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].astype(str)
        Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].replace('1.0',' ')
        Layout_linha_8  = Layout_linha_8.fillna(0)
        Layout_linha_8 = round(Layout_linha_8,1)
        Layout_linha_8 = Layout_linha_8.astype(str)
        Layout_linha_8 = Layout_linha_8.replace('0.0',' ')
        Layout_linha_8 = Layout_linha_8.replace('1.0',' ')
         
        fig = px.bar(Layout_linha_7, x = 'Linha', y = 'Embaladeiras', 
        color = 'Setores', text = 'Embaladeiras',color_discrete_sequence= px.colors.sequential.Aggrnyl)
        fig.update_layout(height = 450, width = 650, uniformtext_minsize=8, uniformtext_mode='show', font = dict(size = 14))
        fig.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig)

    with col2:

        st.info('##### Informações detalhadas das linhas de embalagem:')
        st.write('_______')
        Layout_linha_8.to_excel('Layout_final.xlsx')
        Layout_linha_8
        st.session_state.b = b

        
elif pagina_selecionada == 'Distribuição embaladeiras':
    embaladeira = st.session_state.embaladeira 

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
                    kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl1 = round(kl1,0)

                    if kl1 == 0:
                        kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                    elif kl1 > 0: 
                        kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                        kl = kl.astype(int)
                    #kl
                    #ccc

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
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
                    aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 5',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
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
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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


                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 5',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                    aa.update_layout(height = 350, width = 350)

                elif elem == 6.0:
                    #ccc
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                    bb.update_layout(height = 350, width = 350)

                elif elem == 7.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 7',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                    cc.update_layout(height = 350, width = 350)

                elif elem == 8.0:
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl
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
                    dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA',title = 'Keitt - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                    dd.update_layout(height = 350, width = 350)

                elif elem == 9.0:
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 9' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                    ee.update_layout(height = 350, width = 350)
                elif elem == 10.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl
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
                    ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 10',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                    ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                    ff.update_layout(height = 350, width = 350)
                elif elem == 12.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl
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
                    gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 12' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                    gg.update_layout(height = 350, width = 350)
                elif elem == 14.0:
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
                    kl
                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                    padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                    filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                    padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                    h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    h = h.reset_index()
                    h['mean'] = round(h['mean'],0)
                    h = h.rename(columns = {'mean':'Caixas/Hora'})
                    h['Calibre'] = 14.0
                    h['Calibre'] = h['Calibre'].astype(str)
                    h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
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
                #ccc

                if elem == 5.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
                    #kl
                    #ccc

                    filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
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
                    aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 5',hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                    aa.update_layout(height = 350, width = 350)

                elif elem == 6.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                    bb.update_layout(height = 350, width = 350)

                elif elem == 7.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl
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
                    cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 7', hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                    cc.update_layout(height = 350, width = 350)

                elif elem == 8.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl
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
                    dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                    dd.update_layout(height = 350, width = 350)

                elif elem == 9.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl
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
                    ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 9',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                    ee.update_layout(height = 350, width = 350)

                elif elem == 10.0:
                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
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
                    ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 10',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                    ff.update_layout(height = 350, width = 350)

                elif elem == 12.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl
                    #kl

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
                    gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins  - Calibre 12',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                    gg.update_layout(height = 350, width = 350)

                elif elem == 14.0:

                    kl = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                    kl = round(kl,0)
                    kl = kl.astype(int)
                    kl = kl 
                    #kl

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

                    h = padrao_embaldeiras_palmer_8.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                    h = h.reset_index()
                    h['mean'] = round(h['mean'],0)
                    h = h.rename(columns = {'mean':'Caixas/Hora'})
                    h['Calibre'] = 14.0
                    h['Calibre'] = h['Calibre'].astype(str)
                    h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
                    hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                    hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
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
    b['Horas_4kg_embaladeiras'] = (b['Caixas_total'] / b['Ritmo_embaladeira']) / produtividade_embaladeira 
    ton_horas_embaladeiras = round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg_embaladeiras'].sum()/embaladeira),2)
    #ton_horas_embaladeiras
    #Layout_linha_9
    #st.title('Em construção')
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
        fig4.update_layout(height = 450, width = 550, uniformtext_minsize=8, uniformtext_mode='show', font = dict(size = 15))
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
