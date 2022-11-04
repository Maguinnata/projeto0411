import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Análise DRX x OPTC',
                   page_icon= ':bar_chart:',
                   #layout= 'wide',
                   )

st.title('w7m')
st.title('Lado de Ataque')
st.markdown('##')
st.write('Nesse lado, o time teve boas execuções, mas senti falta de variar um pouco os rounds. '
         'É perceptível que há um costume do time começar em maioria na parte de baixo do mapa, e usando sempre o mesmo setup da Viper. '
         'Além disso há alguns erros que ocorreram mais de uma vez nesse lado do mapa:')
st.write('Raze: Melhorar o uso da ultimate, no quesito de acertar, o ganho de espaço está bom.')
st.write('Viper: Variar o setup, esse setup é bem demorado e em um outro round não foi feito antes da barreira cair.')
st.write('Omen: Melhorar o uso dos TP')
st.write('Fade: Melhorar o uso das habilidades no geral, tanto escolher melhor qual utilitários usar em determinada situações, '
         'quanto ter mais pixels e maneiras eficientes de usar o Spot.')
st.write('Chamber: Melhorar onde colocar os TPs, algumas vezes eles ficam expostos ou não são os mais eficientes.')
st.markdown('##')
st.markdown('##')

st.title('-Pistol')
st.markdown('##')

st.image('imagens/pistol atk.png')
st.write('Setup w7m Pistol ATK')
st.markdown('##')

st.video('videos/pistol atk 1.mp4')
st.write('Boa utilizaçãos de utilitários para pegar vantagem numérica logo de início. No final, conseguiram jogar o round bem e finalizar-lo. ')
st.markdown('##')

st.markdown('----')

st.title('-ECO')
st.markdown('##')

st.write('Não houve rounds ecos significativos.')


st.markdown('----')

st.title('-Anti-ECO')
st.markdown('##')

st.image('imagens/AE atk 4.png')
st.video('videos/AE atk 5.mp4')
st.write('Entry da Raze foi bem feito, conseguindo vantagem e dominar a região inicial do retake. '
         'Entretanto, o time estava muito espalhado, pois após a morte da Raze, quem só está dentro do Bomb é a Fade. '
         'Esse é uma possível brecha que o time adversário pode vir a explorar na hora de um retake. '
         'O ideal é que o time estivesse mais coeso na hora de entrar no Bomb.')

st.markdown('----')

st.title('-Armados')
st.markdown('##')

st.subheader('1º Padrão')
st.image('imagens/AR atk 2.png')
st.video('videos/AR atk 2.mp4')
st.write('Round onde rola algum tipo de falha de comunicação. Pois, no início do clipe, conseguimos ver que teve ping onde o Breach tava '
         'e também teve o barulho da porta que ele abriu, sabendo dessa info o Chamber poderia ser um pouco mais paciente na hora de buscar a kill na Neon adversária. '
         'E mesmo após a troca de 1 por 1, também tinhamos a info de onde o Breach tava, então não tinha porque achar que ele estava atrás da caixa')
st.markdown('##')
st.markdown('##')

st.subheader('2º Padrão')
st.image('imagens/AR atk 3.png')
st.video('videos/AR atk 3.mp4')
st.write('Bom uso de utilitárias para limpar o espaço da antena, o que acaba tirando o Chamber adversário de posição. '
         'Além disso, a conquista desse espaço vai ser usada para deixar o Omen jogando costas, oque vai ser um fator importante nesse round.')
st.markdown('##')
st.video('videos/AR atk 4.mp4')
st.write('Omen conseguindo definir o post plant, devido ao espaço conquistado no início do round')
st.markdown('##')
st.markdown('##')

st.subheader('3º Padrão')
st.image('imagens/AR atk 6.png')
st.video('videos/AR atk 6.mp4')
st.write('Round onde ocorreu um erro de timing, pois a viper liga a smoke da garagem muito antes do time chegar, '
         'assim quando vai fazer o domínio, não tem smoke e nenhum outro utilitário é usado para limpar o espaço.'
         'Além disso, alguns problemas de abrir junto ou usar utilitários de maneira correta.')
st.markdown('##')

st.markdown('----')
st.markdown('----')


st.title('Lado de Defesa')
st.markdown('##')
st.write('')
st.markdown('##')
st.markdown('##')

st.title('-Pistol')
st.markdown('##')

st.image('imagens/pistol def.png')
st.write('Setup w7m Pistol ATK')
st.markdown('##')

st.video('videos/pistol def 1.mp4')
st.write('Apesar de terem deixado espaço no Bomb, a maneira que a Viper recuou e conseguiu jogar para trás foi muito bom, '
         'mas poderia ter valorizado um pouco mais depois da primeira kill, para comprar tempo da rotação. ')
st.markdown('----')

st.title('-ECO')
st.markdown('##')

st.subheader('1º Padrão')
st.image('imagens/E def 2.png')
st.video('videos/E def 2.mp4')
st.write('Antes de abrir, poderia ter usado algum utilitário para amenizar a desvantagem de armas e facilitar de pegar as kills.')

st.markdown('##')
st.markdown('##')

st.subheader('2º Padrão')
st.image('imagens/E def 4.png')
st.video('videos/E def 4.mp4')
st.write('Aqui, um exemplo de como o round eco anterior poderia ter sido, já que teve uso de utilitárias.')

st.markdown('----')

st.title('-Anti-ECO')
st.markdown('##')

st.write('Não houve rounds anti-ecos significativos.')

st.markdown('----')

st.title('-Armados')
st.markdown('##')

st.subheader('1º Padrão')
st.image('imagens/AR def 3.png')
st.video('videos/AR def 3.mp4')
st.write('Apesar da má qualidade do vídeo, a ideia é questionar o porque de uma rotação tão rápida e cedo para o outro Bomb, '
         'pois não tinha tido nenhuma informação que os adversários estavam entrando lá. ')
st.markdown('##')
st.markdown('##')

st.markdown('----')

