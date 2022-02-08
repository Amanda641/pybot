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


#carga horaria
carga_horaria = pd.read_csv('carga_horaria_evolucao_24.csv', encoding = "utf8", sep=';')


carga_horaria['media'] = carga_horaria['ch_total']/carga_horaria['total_docentes']
df_ccab = carga_horaria.loc[carga_horaria['unidade']== "CENTRO DE CIÊNCIAS AGRÁRIAS E DA BIODIVERSIDADE"]
df = df_ccab.groupby(['ano']).sum()['media'].to_frame()
df['media'] = df['media']/2
df['media'] = df['media']/16
ax = df.plot(kind='barh')
plt.title("Média de créditos semanais por semana")
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
plt.savefig('ccab.png')


carga_horaria['media'] = carga_horaria['ch_total']/carga_horaria['total_docentes']
df_iisca = carga_horaria.loc[carga_horaria['unidade']== "INSTITUTO INTERDISCIPLINAR DE SOCIEDADE, CULTURA E ARTE"]
df = df_iisca.groupby(['ano']).sum()['media'].to_frame()
df['media'] = df['media']/2
df['media'] = df['media']/16
ax = df.plot(kind='barh')
plt.title("Média de créditos semanais por semana")
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
plt.savefig('iisca.png')


carga_horaria['media'] = carga_horaria['ch_total']/carga_horaria['total_docentes']
df_ife = carga_horaria.loc[carga_horaria['unidade']== "INSTITUTO DE FORMAÇÃO DE EDUCADORES"]
df = df_ife.groupby(['ano']).sum()['media'].to_frame()
df['media'] = df['media']/2
df['media'] = df['media']/16
ax = df.plot(kind='barh')
plt.title("Média de créditos semanais por semana")
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
plt.savefig('ife.png')


carga_horaria['media'] = carga_horaria['ch_total']/carga_horaria['total_docentes']
df_ccsa = carga_horaria.loc[carga_horaria['unidade']== "CENTRO DE CIÊNCIAS SOCIAIS APLICADAS"]
df = df_ccsa.groupby(['ano']).sum()['media'].to_frame()
df['media'] = df['media']/6
df['media'] = df['media']/2
df['media'] = df['media']/16
ax = df.plot(kind='barh')
plt.title("Média de créditos semanais por semana")
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
plt.savefig('ccsa.png')


carga_horaria['media'] = carga_horaria['ch_total']/carga_horaria['total_docentes']
df_cct = carga_horaria.loc[carga_horaria['unidade']== "CENTRO DE CIÊNCIAS E TECNOLOGIA"]
df = df_cct.groupby(['ano']).sum()['media'].to_frame()
df['media'] = df['media']/2
df['media'] = df['media']/16
ax = df.plot(kind='barh')
plt.title("Média de créditos semanais por semana")
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
plt.savefig('cct.png')


df = carga_horaria.groupby(['ano']).sum()['media'].to_frame()
df['media'] = df['media']/2
df['media'] = df['media']/16
ax = df.plot(kind='barh')
plt.title("Média de créditos semanais por semana")
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
plt.savefig('media_geral.png')


#cursos por campus
graduacao = pd.read_csv('cursos_12.csv', encoding="utf8", sep=';')
graduacao['tipo'] = 'GRADUAÇÃO'

especializacao = pd.read_csv('especializacao.csv', encoding="utf8", sep=';')
especializacao['tipo'] = 'ESPECIALIZAÇÃO'

mestrado = pd.read_csv('mestrado.csv', encoding="utf8", sep=';')
mestrado['tipo'] = 'MESTRADO'

doutorado = pd.read_csv('doutorado.csv', encoding="utf8", sep=';')
doutorado['tipo'] = 'DOUTORADO'

frames = [graduacao, especializacao, mestrado, doutorado]
cursos = pd.concat(frames)
print(frames)

df_jn = cursos.loc[cursos['municipio'] == 'Juazeiro do Norte']
ax = df_jn.iloc[:, [1]]
ax.to_csv('cursos_jn.csv',index=False)

df_ct = cursos.loc[cursos['municipio'] == 'Crato']
ax = df_ct.iloc[:, [1]]
ax.to_csv('cursos_ct.csv', index=False)

df_barbalha = cursos.loc[cursos['municipio'] == 'Barbalha']
ax = df_barbalha.iloc[:, [1]]
ax.to_csv('cursos_barbalha.csv', index=False)

df_bs = cursos.loc[cursos['municipio'] == 'Brejo Santo']
ax = df_bs.iloc[:, [1]]
ax.to_csv('cursos_bs.csv', index=False)

df_ico = cursos.loc[cursos['municipio'] == 'Icó']
ax = df_ico.iloc[:, [1]]
ax.to_csv('cursos_ico.csv', index=False)

