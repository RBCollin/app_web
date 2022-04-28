import streamlit as st
import pandas as pd
import numpy as np
## NA TELA TEM QUE APENAS EXIBIR:
## TON/HR
## CAIXOTES/HORA
## QNTD DE EMBALADEIRAS
## QNTD NO TALO IDEAL
## O AJUSTE TEM QUE SER DE FORMA AUTOMATICA CONFORME OS CAIXOSTES E FRUTOS VARIAM
## POSSO COLOCAR COMO INPUT NO FORMS A QUANTIDADE DE PESSOAS DISPONIVEIS
## A PESSOA DIGITA E ELE N PRECISA FICAR EQUILBRANDO
## O MODELO JA BUSCA A MELHOR COMBINAÇÂO COM BASE NO QUE TA DISPONIVEL
## E APENAS EXIBE NA TELA QUAL SÃO AS QUANTIDADES QUE A PESSOA TEM QUE ATRIBUIR


dataset = pd.read_excel('Planilha Denilton.xlsx')

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

def ritmo(b):
    if b['Calibre'] == 5:
        return 229
    elif b['Calibre'] == 6:
        return 169
    elif b['Calibre'] == 7:
        return 174
    elif b['Calibre'] == 8:
        return 191
    elif b['Calibre'] == 9:
        return 157
    elif b['Calibre'] == 10:
        return 139
    elif b['Calibre'] == 12:
        return 149
    elif b['Calibre'] == 14:
        return 85
    else:
        return 'NADA'
b['Ritmo'] = b.apply(ritmo, axis = 1)




avg_frutos_caixotes = 33
produtividade_embaladeira = 0.75
produtividade_talo = 0.80


###########################################################################################################33
## Tela de inputs
st.title('Talo - Embalagem')
st.subheader('Balanceamento da linha de embalagem')
st.markdown("""Selecione a quantidade de caixotes e a quantidade de embaladeiras disponiveis para calcular a quantidade de pessoas necessárias no corte de talo """, unsafe_allow_html=True)

with st.form(key='planilha'):
    ## armazendnado em uma variavdl
    caixotes = st.number_input(label = 'Insira a quantidade de caixotes: ', format = "%d", step = 1)
    #controle = st.text_input(label = 'Insira o código do controle: ')
    #corte_talo = st.number_input(label = 'Insira a quantidade de pessoas disponíveis para o corte de talo: ', format = "%d", step = 1) 
    embaladeira = st.number_input(label = 'Insira a quantidade de embaladeiras disponíveis: ', format = "%d", step = 1)
    corte_talo = round(embaladeira / 3.33333)
    #fazenda = st.selectbox('Selecione a sua fazenda:', ['Bom Jesus','Brandões'])
    button_submit = st.form_submit_button('Balancear !')
    #corte_talo
#
#caixotes = 504
b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100
b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira


#############################################################################################################
if button_submit:

    #b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100
    #b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira

    #############################################################################################################

    ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))
    ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))*100
    diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))

    corte_talo2 = corte_talo-1
    ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))

    def equilibrio(corte_talo, embaladeira):

        if (ritmo_talo) < (ritmo_embaladeira):
            st.write('A quantidade ideal de pessoas no talo tem que ser:', round(corte_talo-1))
            st.write('Capacidade de caixotes/hora no corte de talo é de:', round((caixotes*0.0416667)/(ritmo_talo_2)))
            st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
            
        #st.write('A quantidade ideal de pessoas na embalagem é de:', 3.33 * corte_talo )
        else :
            st.write('A quantidade ideal de pessoas no talo tem que ser:', round(corte_talo))
            st.write('Capacidade de caixotes/hora no corte de talo é de:', round((caixotes*0.0416667)/(ritmo_talo)))
            st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))

    equilibrio(corte_talo, embaladeira)
    corte_talo
    #st.write('Ritmo de talo é:', ritmo_talo)
    #st.write('Ritmo embaladeira é:', ritmo_embaladeira/100)
    #ritmo_talo
    #b['Horas_4kg'].sum()

#b

import plotly.express as px
b['Calibre Name'] = b['Calibre'].astype(str)
fig = px.histogram(b, x = 'Calibre Name',y = 'Percentual', color = 'Calibre Name')
fig.update_layout(height = 400, width = 800)
st.plotly_chart(fig)






## AS PEQUENAS DIFERENÇAS SE DÃO AO FATO DA PLANILHA DE DENILTON CONSIDERAR AS FAIXAS DE CALIBRES DIFERENTES 
## NA TABELA UM ESTA CERTO, AS FAIXAS
## POREM NA RESUMO ELE FAZ DIFERENTES
## POR FAIXA DE PESO, E ESSAS FAIXAS ESTÃO DIFERENTES O QUE GEROU PROPORÇOES DIFERENTES
## DOS CALIBRES
## EXEMPLO COMPARE AS FAIXAS QUE ELE COLOCA NA RESUMO
## É DIFERENTE DO CALIBRE NOMEADO NA BD
## EXMEPLO SÂOS AS FAIXAS DE 630 e 557
## ele fala que calibre 7 é menor ou igual a 630
## porem a smangas de 630 estao como calibre 6 na planilha

## PARA ATENDER O REQUISITO DE RITMO DE TALO NAO PODE SER MAIS RAPIDO DO QUE EMBALADEIRA EU UTILIZO CORTE DE TALO - 1 E RITMO 2
## PARA ATENDER A PLANILHA EU UTILIZO O NORMAL
## ATENDENDO O REQUISITO ERRA EM VALORES COM 5 NO FINAL
## MAS ISSO SE DA AO FATO DA DIFERENÇA DE CALIBRES
## O IDEAL É DEIXAR COM A RESTRIÇÃO DO RITMO DE TALO NAO SER MAIS RAPIDO
## E CASO SEJA RETIRAR UMA PESSOA DO TALO



################################################## JANELA DOIS -- ABA DOIS DA PLANILHA #################################################################

st.sidebar.title('Packing House - Balanceamento')
st.sidebar.markdown('Selecione a informação para consulta')

pagina_selecionada = st.sidebar.selectbox('Escolha uma opção:', ['Talo X Embalagem','Linhas de embalagem'])

#if pagina_selecionada == 'Talo X Embalagem':
