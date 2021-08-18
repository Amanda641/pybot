import pandas as pd
from matplotlib import pyplot as plt

producao = pd.read_csv('UFCA_producao.csv')

PERIODICOS = producao.loc[producao['tipo']== "PERIODICOS"]
ax = PERIODICOS.groupby(['ano']).count()['titulo'].to_frame().plot(kind='barh', color="#C71585")
total_periodicos = PERIODICOS.shape[0]
plt.title("Periódicos")

rects = ax.patches
for rect in rects:
    x_value = rect.get_width()
    y_value = rect.get_y() + rect.get_height() / 2
    space = 5
    ha = 'left'

    if x_value < 0:
        space *= -1
        ha = 'right'
    label = "{:.0f}".format(x_value)
    plt.annotate(label,(x_value, y_value),xytext=(space, 0),textcoords="offset points",va='center',ha=ha)                      
plt.savefig('periodicos.png')

LIVRO_ORGANIZADO = producao.loc[producao['tipo']== "LIVRO_ORGANIZADO_OU_EDICAO"]
ax = LIVRO_ORGANIZADO.groupby(['ano']).count()['titulo'].to_frame().plot(kind='barh', color = "#87CEFA")
total_livro_organizado = LIVRO_ORGANIZADO.shape[0]
plt.title("Livro organizado ou edição")

rects = ax.patches
for rect in rects:
    x_value = rect.get_width()
    y_value = rect.get_y() + rect.get_height() / 2
    space = 5
    ha = 'left'

    if x_value < 0:
        space *= -1
        ha = 'right'
    label = "{:.0f}".format(x_value)
    plt.annotate(label,(x_value, y_value),xytext=(space, 0),textcoords="offset points",va='center',ha=ha)                      
 
plt.savefig('livro_organizado.png')

CAPITULOS = producao.loc[producao['tipo']== "Capítulo de livro publicado"]
ax = CAPITULOS.groupby(['ano']).count()['titulo'].to_frame().plot(kind='barh',color="#D2691E")
total_capitulos= CAPITULOS.shape[0]
plt.title("Capítulo de livro publicado")

rects = ax.patches
for rect in rects:
    x_value = rect.get_width()
    y_value = rect.get_y() + rect.get_height() / 2
    space = 5
    ha = 'left'

    if x_value < 0:
        space *= -1
        ha = 'right'
    label = "{:.0f}".format(x_value)
    plt.annotate(label,(x_value, y_value),xytext=(space, 0),textcoords="offset points",va='center',ha=ha)                      
 

plt.savefig('capitulo.png')


LIVRO_PUBLICADO = producao.loc[producao['tipo']== "LIVRO_PUBLICADO"]
ax = LIVRO_PUBLICADO.groupby(['ano']).count()['titulo'].to_frame().plot(kind='barh', color = "#DAA520")
total_publicados = LIVRO_PUBLICADO.shape[0]
plt.title("Capítulo de livro publicado")
rects = ax.patches
for rect in rects:
    x_value = rect.get_width()
    y_value = rect.get_y() + rect.get_height() / 2
    space = 5
    ha = 'left'

    if x_value < 0:
        space *= -1
        ha = 'right'
    label = "{:.0f}".format(x_value)
    plt.annotate(label,(x_value, y_value),xytext=(space, 0),textcoords="offset points",va='center',ha=ha)                      

plt.savefig('livro_publicado.png')


ANAIS = producao.loc[producao['tipo']== "ANAIS DE EVENTOS"]
ax = ANAIS.groupby(['ano']).count()['titulo'].to_frame().plot(kind='barh', color = "#00FF7F")
total_anais = ANAIS.shape[0]
plt.title("Anais de eventos")
rects = ax.patches
for rect in rects:
    x_value = rect.get_width()
    y_value = rect.get_y() + rect.get_height() / 2
    space = 5
    ha = 'left'

    if x_value < 0:
        space *= -1
        ha = 'right'
    label = "{:.0f}".format(x_value)
    plt.annotate(label,(x_value, y_value),xytext=(space, 0),textcoords="offset points",va='center',ha=ha)                      
                                    
plt.savefig('anais.png')
