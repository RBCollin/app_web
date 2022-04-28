import streamlit as st
import pandas as pd
import numpy as np
## NA TELA TEM QUE APENAS EXIBIR:
## TON/HR
## CAIXOTES/HORA
## QNTD DE EMBALADEIRAS
## QNTD NO TALO IDEAL
## O AJUSTE TEM QUE SER DE FORMA AUTOMATICA CONFORME OS CAIXOSTES E FRUTOS VARIAM


dataset = pd.read_excel('Planilha Denilton.xlsx')

filtro = dataset['Calibre'] != 'Pequeno'
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

st.subheader('Balanceamento da linha de embalagem')
st.markdown("""Selecione a quantidade de caixotes e o máximo de pessoas disponíveis para o corte de talo e par a aembalagem. Em seguida, ajuste a quantidade de pessoas no corte de talo e nas embalagens buscando o máximo balanceamento  """, unsafe_allow_html=True)

with st.form(key='planilha'):
    ## armazendnado em uma variavdl
    caixotes = st.number_input(label = 'Insira a quantidade de caixotes: ', format = "%d", step = 1)
    #controle = st.text_input(label = 'Insira o código do controle: ')
    corte_talo = st.number_input(label = 'Insira a quantidade de pessoas no corte de talo: ', format = "%d", step = 1)
    embaladeira = st.number_input(label = 'Insira a quantidade de embaladeiras: ', format = "%d", step = 1)
    #fazenda = st.selectbox('Selecione a sua fazenda:', ['Bom Jesus','Brandões'])
    button_submit = st.form_submit_button('Atende ?')


#############################################################################################################
if button_submit:

    b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100
    b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira
    ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))*100
    ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))*100
    diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))

    def atende(ritmo_talo, ritmo_embaladeira):
        if ritmo_talo < ritmo_embaladeira and diferenca_aceitavel > 0.06:

            st.write('Não atende:')
            st.write('\n')
            st.write('Tempo Embaladeira:',round(ritmo_embaladeira,4),'>','Tempo Talo:', round
            (ritmo_talo,4))
            st.write('\n')
            st.write('A diferença é de:' , diferenca_aceitavel)
    
            st.write('Não existe cenário aceitável com o ritmo de talo mais rápido, reajuste até os ritmos se equilibrarem com uma difereça máxima de 0.06.')


        elif ritmo_talo > ritmo_embaladeira:

            st.write('Não atende:\n','Tempo Embaladeira:',round(ritmo_embaladeira,4),'<','Tempo Talo:', round(ritmo_talo,4),
            '\n','A diferença é de:' , diferenca_aceitavel)
            #st.write('Não existe cenário aceitável com o ritmo de talo maior !!')
            st.write('Equilibre a linha, diferença aceitavél é de:',0.06)

        else:

            st.write('Atende sem muito Gargalo/Ociosidade:')
            st.write('\n')
            st.write('Ritmo Embaladeira',round(ritmo_embaladeira, 4),'=','Ritmo Talo', round(ritmo_talo,4))
            st.write('A diferença é de:', diferenca_aceitavel,', limite aceitável.')

    atende(ritmo_talo,ritmo_embaladeira)
    st.write('\n')
    st.write('Capacidade de caixotes/hora no corte de talo é de:', round((caixotes*0.0416667)/(ritmo_talo/100),0))
    #st.write('Capacidade de caixotes/hora das embaladeiras é de:', round((caixotes*0.0416667)/ritmo_embaladeira,0))
    
    #st.write('\n')
    st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))
    








































































