import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")
dataset = pd.read_excel('Planilha Denilton.xlsx')
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
#b
############################################## Considerando QUALIDADE ##############################################

quality = dataset['Qualidade'].value_counts() / dataset['Qualidade'].count()
#quality
quality = pd.DataFrame(quality)
quality = quality.reset_index()
quality.columns = ['Qualidade','Percent']
#quality

primeira_percent = quality[quality.Qualidade==1].Percent.item()
segunda_percent = quality[quality.Qualidade==2].Percent.item()
terceira_percent = quality[quality.Qualidade==3].Percent.item()
#aereo_percent = quality[quality.Qualidade=="Aéreo"].Percent.item()
#aereo_percent
#terceira_percent

st.title('Packing House - Linhas de Embalagem')
col1, col2 = st.columns(2)
col1.subheader('Selecione a variedade de manga:')
variedade = col1.selectbox(' ',['Keitt','Kent','Palmer','Tommy Atkins'])

#variedade = 'Palmer'
#col1.variedade

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


#def ritmo_aereo(b):
#    if b['Calibre'] == 5 and variedade == 'Kent':
#        return 83
    #elif b['Calibre'] == 6 and variedade == 'Kent':
#        return 70
#    elif b['Calibre'] == 7 and variedade == 'Kent':
#        return 59
#    elif b['Calibre'] == 8 and variedade == 'Kent':
    #    return 45 
#    elif b['Calibre'] == 9 and variedade == 'Kent':
#        return 33
#    else:
#        return None

#b['Ritmo_aereo'] = b.apply(ritmo_aereo, axis = 1)


avg_frutos_caixotes = 33
produtividade_embaladeira = 0.75
produtividade_talo = 0.80
produtividade_limpeza = 0.75

###########################################################################################################33
#


################################################## JANELA DOIS -- ABA DOIS DA PLANILHA #################################################################
coluna1, coluna2 = st.columns(2)
with coluna1:
    from PIL import Image
    img = Image.open('agrodn.png')
    newsize = (380,110)
    img2 = img.resize(newsize)

    st.sidebar.image(img2, use_column_width=True)
    st.sidebar.title('Menu')
    st.sidebar.markdown('Escolha a informação para visualizar')
    


pagina_selecionada = st.sidebar.selectbox('Escolha as informações na ordem:', ['1 - Balanceamento e produtividade','2 - Linhas de embalagem','3 - Distribuição embaladeiras'])


if pagina_selecionada == '1 - Balanceamento e produtividade':
    ## Tela de inputs
    #st.title('Talo - Embalagem')
    #st.title('Balanceamento da linha de embalagem')
    st.subheader("""Selecione a quantidade de caixotes e a quantidade de embaladeiras disponíveis:""")

    with st.form(key='planilha'):

        ## Criando variaveis
        ################ INPUTS ################
        col1, col2 = st.columns(2)
        caixotes = col1.number_input(label = 'Insira a quantidade de caixotes: ', format = "%d", step = 1)
        embaladeira = col1.number_input(label = 'Insira a quantidade de embaladeiras disponíveis: ', format = "%d", step = 1)

        corte_talo = round(embaladeira / 3.33333)
        button_submit = st.form_submit_button('Balancear !')
        

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

    if button_submit:
        ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))
        ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))*100
        diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))

        corte_talo2 = corte_talo-1
        ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))
        
        
        def equilibrio(corte_talo, embaladeira):

            if (ritmo_talo) < (ritmo_embaladeira):
                caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
                #caixotes_hora
                Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))

                st.write('A quantidade ideal de pessoas no talo tem que ser:', round(corte_talo-1))
                st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao)
                st.write('Capacidade de caixotes/hora:', caixotes_hora)
                st.write('Capacidade de Toneladas/Horas:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
                #Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                #Limpeza_selecao
                #st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao)
            
            else :
                caixotes_hora2 = round((caixotes*0.0416667)/(ritmo_talo))
                Limpeza_selecao2 = round((caixotes_hora2 * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                #caixotes_hora2 = round((caixotes*0.0416667)/(ritmo_talo))
                st.write('A quantidade ideal de pessoas no talo tem que ser:', round(corte_talo))
                st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao2)
                st.write('Capacidade de caixotes/hora:', caixotes_hora2)
                st.write('Capacidade de Toneladas/Horas:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
                #Limpeza_selecao2 = round((caixotes_hora2 * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                #st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao2)

        #col1, col2 = st.columns(2)
        #st.write('A variedade selecionada foi:', variedade)
        
        with col1:
            st.markdown("""__________________________________________""")
            st.write('**Siga a ecomendação abaixo de acordo com as variáveis exibidas:**')
            equilibrio(corte_talo, embaladeira)
        #equilibrio(corte_talo, embaladeira)
        
        #corte_talo
        #b
########################################### grafico plotly ################################################################
        #st.write('A variedade selecionada foi:', variedade)
        with col2:
            import plotly.express as px
            b['Calibre Name'] = b['Calibre'].astype(str)
            c = round(b['Percentual'],2)
            fig = px.bar(b, x = 'Calibre Name',y = 'Percentual', color = 'Calibre Name', title = 'Distribuição de calibres:', text = c)
            fig.update_layout(height = 450, width = 700,uniformtext_minsize=8, uniformtext_mode='show')
            fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig)
            #b
        #with col3:
        #    fig2 = px.pie(b, values = 'Percentual', names = 'Calibre')
        #st.plotly_chart(fig2)
        #b

        #st.write('Ritmo de talo é:', ritmo_talo)
        #st.write('Ritmo embaladeira é:', ritmo_embaladeira/100)
        #ritmo_talo
        #b['Horas_4kg'].sum()

################################### OBJETIVO -- FALAR QUANTAS PESSOAS PRECISAM EM CADA LINHA ############################

elif pagina_selecionada == '2 - Linhas de embalagem':

    #col1.title('Linhas de Embalagem')
        #caixotes
    col1.subheader('Selecione o período:')

    Programa_input = col1.selectbox(' ', ['Entre Safra','Safra'])

    #col1, col2 = st.columns(2)
    #col2.subheader('Repita o balancamento:')
#    col2.markdown("_______")
    #col2.markdown("_______")
    
    #col2.markdown(" ")
    with col1.form(key='planilha'):
        
        st.subheader('Balanceamento:')
        ## Criando variaveis
        ################ INPUTS ################
        caixotes = st.number_input(label = 'Insira a quantidade de caixotes: ', format = "%d", step = 1)
        embaladeira = st.number_input(label = 'Insira a quantidade de embaladeiras disponíveis: ', format = "%d", step = 1)

        corte_talo = round(embaladeira / 3.33333)
        button_submit = st.form_submit_button('Balancear !')
        

    ##################################################################################################################################################
    
    b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100

    b['Caixas_1'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * primeira_percent) / b['Calibre']) 
    b['Caixas_2'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * segunda_percent)  / b['Calibre']) 
    b['Caixas_3'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * terceira_percent) / b['Calibre'])
    #b['Caixas_Aereo'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * aereo_percent) / b['Calibre'])
    #b['Caixas_aereo'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * aereo_percent) / b['Calibre'])  
    
    #b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira
    b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira   

    #b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira    
    #b['Horas_aereo'] = (b['Caixas_Aereo'] / b['Ritmo_aereo']) / produtividade_embaladeira
    #b['Horas_4kg'] = (b['Horas_4kg'] + b['Horas_aereo'].fillna(0))
    #b['Horas_aereo'] = b['Horas_aereo'].fillna(0)

    #b['Horas_aereo'] = (b['Caixas_Aereo'] / b['Ritmo_aereo']) / produtividade_embaladeira 
    #b['Horas_4kg'] = (b['Horas_4kg'] + b['Horas_aereo'])

    #b['Ritmo_aereo'] = b['Ritmo_aereo'] .fillna(1)
    #############################################################################################################


    if button_submit:
        ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))
        ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))*100
        diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))

        corte_talo2 = corte_talo-1
        ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))

        def equilibrio(corte_talo, embaladeira):

            if (ritmo_talo) < (ritmo_embaladeira):
                caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
                #caixotes_hora
                st.write('A quantidade ideal de pessoas no talo tem que ser:', round(corte_talo-1))
                st.write('Capacidade de caixotes/hora no corte de talo é de:', caixotes_hora)
                st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
                Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                #Limpeza_selecao
                st.write('Quantidade de pessoas na limpeza e seleção tem que ser de:', Limpeza_selecao)
            
            else :
                caixotes_hora2 = round((caixotes*0.0416667)/(ritmo_talo))
                st.write('A quantidade ideal de pessoas no talo tem que ser:', round(corte_talo))
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
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
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
            return ''
        elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
            return ''
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

    with col2:
        import plotly.express as px
        #st.markdown("________")
        #Layout_linha_7 
        #Layout_linha_7['Embaladeiras'] = round(Layout_linha_7['Embaladeiras'],2)

        df_setores = round(Layout_linha_7.groupby('Setores')['Embaladeiras'].sum(),2)
        #df_setores['Embaladeiras'] = round(df_setores['Embaladeiras'],2)

        df_setores = df_setores.reset_index()
        fig2 = px.bar(df_setores, x = 'Setores', y = 'Embaladeiras', color = 'Setores', text= 'Embaladeiras', title = 'Total de embaladeiras por Setor') 
        fig2.update_layout(height = 450, width = 700, uniformtext_minsize = 8, uniformtext_mode = 'show')
        fig2.update_traces(textfont_size = 12, textangle = 0, textposition = 'outside', cliponaxis = False)
        st.plotly_chart(fig2)



        #import plotly.express as px
        #b['Calibre Name'] = b['Calibre'].astype(str)
        #c = round(b['Percentual'],2)
        fig = px.bar(Layout_linha_7, x = 'Linha', y = 'Embaladeiras', 
        color = 'Setores', title = 'Distribuição de embaladeiras nas linhas de embalagem:', text = 'Embaladeiras')
        fig.update_layout(height = 450, width = 700, uniformtext_minsize=8, uniformtext_mode='show')
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig)

        #Layout_linha_7
        Layout_linha_8 = Layout_linha_7[['Linha','Calibre','Qualidade','Calibre2','Qualidade2','Frutos','Frutos2','Caixas','Caixas2','Embaladeiras','Setores']]
        Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].astype(str)
        Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].replace('1.0',' ')
        Layout_linha_8  = Layout_linha_8.fillna(0)
        Layout_linha_8 = round(Layout_linha_8,1)
        Layout_linha_8 = Layout_linha_8.astype(str)
        Layout_linha_8 = Layout_linha_8.replace('0.0',' ')
        Layout_linha_8 = Layout_linha_8.replace('1.0',' ')
        #Layout_linha_8
        #Layout_linha_9 = Layout_linha_8.astype(float)

    with col1:
        Layout_linha_8.to_excel('Layout_final.xlsx')
        Layout_linha_8
        #Layout_linha_7
        #Layout_linha_5



elif pagina_selecionada == '3 - Distribuição embaladeiras':

    import plotly.express as px
    Layout_linha_9 = pd.read_excel('Layout_final.xlsx')

    Layout_linha_9 = Layout_linha_9.drop(columns = ['Unnamed: 0'])
    Layout_linha_9['Setores'] = Layout_linha_9['Setores'].astype(str)

    Layout_linha_9['Embaladeiras'] = Layout_linha_9['Embaladeiras'].replace(' ','0')
    Layout_linha_9['Embaladeiras'] = Layout_linha_9['Embaladeiras'].astype(float)

##################################### DATASET EMBALADEIRAS #######################################################################

    padrao_embaldeiras = pd.read_excel('padrao_embaladeiras_TUDO_cenarios.xlsx')

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

    #Layout_linha_9
    #st.title('Em construção')

#############################################  COLUNAS  #########################################################################
    col1, col2 = st.columns(2)
    
#################################################   PALMER #################################################
    with col1.form(key='planilha'):
        
        st.subheader('Escolha o calibre para visualizar a recomendação:')
        ## Criando variaveis
        ################ INPUTS ################
        calibre_input = st.number_input(label = '', format = "%d", step = 1)
        #variedade2 = variedade
        button_submit = st.form_submit_button('Visualizar Recomendação')

        #Layout_linha_9['Calibre'] = Layout_linha_9['Calibre'].replace(' ','0')
        #Layout_linha_9['Calibre'] = Layout_linha_9['Calibre'].astype(float)

        #linhas = Layout_linha_9.merge(calibre_input, left_on = 'Calibre')
        #linhas

    with col1:
        if button_submit:
            st.write('Recomenda-se designar estas embaladeiras para as linhas de calibre',calibre_input,'da variedade',variedade,':')
            st.markdown('*Ordem de produtividade:*')
            #st.markdown('Recomenda-se designar estas embaladeiras para as linhas de calibre 10:')

            if calibre_input == 5 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 6 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b
            elif calibre_input == 7 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 8 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b
            elif calibre_input == 9 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 10 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 12 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 14 and variedade == 'Palmer':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b
            elif calibre_input == 5 and variedade == 'Kent':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                a

            elif calibre_input == 6 and variedade == 'Kent':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                a
            elif calibre_input == 7 and variedade == 'Kent':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 8 and variedade == 'Kent':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b
            elif calibre_input == 9 and variedade == 'Kent':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 10 and variedade == 'Kent':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 12 and variedade == 'Kent':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 14 and variedade == 'Kent':
                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 5 and variedade == 'Tommy Atkins':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 6 and variedade == 'Tommy Atkins':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b
            elif calibre_input == 7 and variedade == 'Tommy Atkins':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 8 and variedade == 'Tommy Atkins':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b
            elif calibre_input == 9 and variedade == 'Tommy Atkins':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 10 and variedade == 'Tommy Atkins':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 12 and variedade == 'Tommy Atkins':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 14 and variedade == 'Tommy Atkins':
                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 5 and variedade == 'Keitt':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 6 and variedade == 'Keitt':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b
            elif calibre_input == 7 and variedade == 'Keitt':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 8 and variedade == 'Keitt':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                #a['Calibre'] = calibre_input
                b
            elif calibre_input == 9 and variedade == 'Keitt':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 10 and variedade == 'Keitt':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 12 and variedade == 'Keitt':

                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            elif calibre_input == 14 and variedade == 'Keitt':
                filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]


                    #padrao_embaldeiras_palmer.groupby(['CALIBRE','PESSOA'])['mean']
                a = padrao_embaldeiras_palmer.groupby(['PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                a = a.reset_index()
                b = a['PESSOA'].astype(str)
                b

            else:
                st.write('Atenção nos valores de entrada')
        
    with col2:
            #Layout_linha_9
        if button_submit:
            Layout_linha_9 = Layout_linha_9.fillna(' ')
            Layout_linha_9['Qualidade'] = Layout_linha_9['Qualidade'].astype(str)
            Layout_linha_9['Qualidade2'] = Layout_linha_9['Qualidade2'].astype(str)
            #Layout_linha_9 = Layout_linha_9.fillna(' ')
            Layout_linha_9['Calibre - Qualidade'] = Layout_linha_9['Calibre'] + '-' +Layout_linha_9['Qualidade'] + ' '+ '/' + ' ' + Layout_linha_9['Calibre2'] + '-' + Layout_linha_9['Qualidade2']
            
            fig4 = px.bar(Layout_linha_9, x = 'Linha', y = 'Embaladeiras', color = 'Calibre - Qualidade', title = 'Distribuição de embaladeiras nas linhas de embalagem:', text = 'Embaladeiras',
            category_orders={"Calibre":['5.0','6.0','7.0','8.0','9.0','10.0','12.0','14.0']}, hover_name = 'Linha')
            fig4.update_layout(height = 450, width = 750, uniformtext_minsize=8, uniformtext_mode='show')
            fig4.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)
            col2.plotly_chart(fig4)

            #st.title('nada')
            #Layout_linha_9
            #a



    #Layout_linha_8



    
    

#################################################################### KMEANS PARA DIRECIONAR EMBALADEIRAS ###########################################################################
## CRIAR AQUI UMA RECOMENDAÇÃO DE EMBALADEIRAS PARA CADA LINHA
## EXEMPLO:
## LINHA TAL PRECISA DE 8 pessoas para palmer de calibre 8
## eu vou recomendar as 8 primeiras daquele estudo com um caixa/alta maior
## AI FICA ASSIM
## LINHA X
## EMBALADEIRAS YS, WS, ZS







        










        
    




