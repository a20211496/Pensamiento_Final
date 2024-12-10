import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Liga española temporada 2023-2024', layout="wide", page_icon = 'https://assets.laliga.com/assets/logos/LL_RGB_h_color/LL_RGB_h_color.png')

st.title("Equipos españoles en las competiciones temporada 2023-2024", "text-align: justify")
df = pd.read_excel('Base de datos finale.xlsx')


competiciones = ["General", "Laliga", "Copa del Rey", "Champions league", "Europa league", "Conference league", "Estadísticas"]
eleccion_campeonato = st.sidebar.selectbox("Selecciona la competición de tu preferencia", competiciones)

if eleccion_campeonato == "General":
    st.write(df.head(20))
    st.markdown('<div style="text-align: justify;">El presente trabajo tiene como objetivo presentar los números de assistencia de los equipos españoles durante la temporada 2023-2024, debido al tiempo que se está desarrollando las estadísticas y el momento de los equipos serán a como llegaban para la mencionada temporada por lo que pueden generar contrastes con las estadísticas actuales.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Asimismo la preparación del mismo ha sido desafiante para mí ya que fuera de las industriales líneas de código que he tenido que realizar (lo cual ha sido más difícil qu hacer la misma base de datos) también porque no soy un programador experto pero con un par de guías para aprender esto ha sido muy entretenido por la parte misma de que uso una afición personal como es el deporte para hacer más divertida las arduas tareas.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Las conclusiones de este trabajo son my buenas, ya que por un lado uso la base de datos para realizar los cáculos y transformar los mismos en gráficos, por otro lado estos números fuera de ser una numeración simple en el sistema numérico estándar es una persona que dedica su tiempo para asisitir al estadio de su equipo favorito y sea cual sea el resultado es sorprendente la gran cantidad de hinchas que circulan entre las principales competiciones en las que se involucran los equipos de fútbol españoles.</div>', unsafe_allow_html=True)
    competicion_laliga = df[df['competición'] == 'laliga']
    asistencia_total = competicion_laliga['asistencia'].sum()
    st.text("")
    st.markdown('<div style="text-align: justify;">Asistentes totales en la liga 2023-2024</div>', unsafe_allow_html=True)
    asistencia_total

elif eleccion_campeonato == "Laliga":
    col1, col2, col3 = st.columns(3)
    st.markdown("<h2 style='text-align: center;'>LaLiga EA Sports </h2>", unsafe_allow_html=True)
    col2.image("https://pbs.twimg.com/media/F1evLeMWcAMqc-m.jpg", width = 300 )
    st.markdown('<div style="text-align: justify;">El campeonato de liga española LaLiga EA Sports antes llamado LigaBBVA (2008-2016), LaLiga Santander (2016-2019) es el campeonato correspondiente a la primera división del fútbol español, compuesto por 20 equipos en los que destacan el Real Madrid, Barcelona, Atlético de Madrid y Sevilla por sus participaciones tanto a nivel nacional como internacional destacando en las principales competiciones como lo son los 14 títulos  de Champions league del Real Madrid, el sextete del Barcelona (Liga, Copa del Rey, Champions league, Supercopa de España, Supercopa de Europa y Mundial de clubes de una temporada), los 7 títulos de Europa league del Sevilla siendo que con los resultados obtenidos por los demás equipos sea considerada la tercera mejor liga de Europa en la actualidad.</div>', unsafe_allow_html=True)
    st.write("")

    st.subheader("Alavés")
    st.image("https://seeklogo.com/images/D/deportivo-alaves-logo-0FBE6894C8-seeklogo.com.png", width = 150)
    alaves = df[df['Equipo_local'] == 'Alavés']
    asistencia_alaves = alaves ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_alaves
    st.markdown('<div style="text-align: justify;">El club deportivo Alavés fundado en 1921 en la ciudad de Vitoria-Álava jugó por primera vez el campeonato en el año 1930 contando desde entonces 18 participaciones en la primera división del fútbol español, se destaca su mejor posición en la tabla con un sexto lugar en la temporada 1999-2000 por lo que no posee títulos de campeón de la liga española o Copa del Rey, los únicos títulos que ha conseguido el equipo se remiten a títulos de categorías inferiores como Segunda División o Segunda División B (Tercera División). Ascendió a la liga 2023-2024 mediante la fase de playoffs por el tercer cupo de ascenso al terminar en cuarto lugar de la segunda división venciendo al S. D. Eibar en semifinales y al  Levante. U. D en una final que se resolvió con un gol al minuto 120+9. En la liga 2023-2024 el equipo terminó en la décima posición con 46 puntos.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Alavés")
    st.write("")
    alaves_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Alavés')]
    resultados_liga_alaves = alaves_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_alaves = resultados_liga_alaves.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_alaves['fecha_campeonato'] = pd.to_numeric(resultados_liga_alaves['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_alaves['fecha_campeonato'],
    weights=resultados_liga_alaves['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#004cff',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Almería")
    st.image("https://www.pointspreads.com/wp-content/uploads/2022/07/UD-Almeria.webp", width = 200)
    almeria = df[df['Equipo_local'] == 'Almería']
    asistencia_almeria = almeria ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_almeria
    st.markdown('<div style="text-align: justify;">El Unión deportiva Almería fundado en 1989 en la ciudad de Almería jugó por primera vez el campeonato por primera vez en el año 2007 desde entonces contando con 7 participaciones en el torneo siendo la de mejor resultado la misma temporada en la que debutó la 2007-2008 el cual fue el segundo mejor desempeño de un equipo recién ascendido no poseyendo un título de segunda división y subcampeonatos de tercera división. El equipo permaneció en la liga por ocupar el puesto 17 de la liga 2022-2023 sin embargo en la liga 2023-2024 terminó en la posición 19 con 21 puntos, su peor cosecha de puntos en una temporada de primera división ya que en la temporada 2010-2011 terminó en la última posición (20) pero con más puntos (30).</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Almería")
    st.write("")
    almeria_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Almería')]
    resultados_liga_almeria = almeria_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_almeria = resultados_liga_almeria.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_almeria['fecha_campeonato'] = pd.to_numeric(resultados_liga_almeria['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_almeria['fecha_campeonato'],
    weights=resultados_liga_almeria['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#eb2f2f',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Athletic de Bilbao")
    st.image("https://1000marcas.net/wp-content/uploads/2022/05/Athletic-Bilbao-Logo.png", width = 200)
    bilbao = df[df['Equipo_local'] == 'Athletic de Bilbao']
    asistencia_bilbao = bilbao ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_bilbao
    st.markdown('<div style="text-align: justify;">El athletic de Bilbao fundado en el año 1898 y es uno de los 3 clubes que ha jugado todas las ediciones de la liga española desde su fundación en el año 1928 y mantiene una tradición particular ya que es el único equipo que juega con jugadores nacidos en territorio vasco  desde el año 1912, contando sus participaciones en la primera división española con 8 títulos de campeón de la primera división y 7 subcampeonatos mientras que en la copa del rey tiene 24 títulos y 16 subcampeonatos 3 supercopas de España y 3 subcampeonatos, toda una historia dentro de la competición. En la temporada 2023-2024 el equipo terminó en la quinta posición lo que le valió la clasificación a la fase de liga de la Europa League.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Athletic de Bilbao")
    st.write("")
    bilbao_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Athletic de Bilbao')]
    resultados_liga_bilbao = bilbao_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_bilbao = resultados_liga_bilbao.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_bilbao['fecha_campeonato'] = pd.to_numeric(resultados_liga_bilbao['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_bilbao['fecha_campeonato'],
    weights=resultados_liga_bilbao['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#f50f22',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Atlético de Madrid")
    st.image("https://1000marcas.net/wp-content/uploads/2020/03/Logo-Atletico-Madrid.png", width = 200)
    atletico_madrid = df[df['Equipo_local'] == 'Atlético de Madrid']
    asistencia_atletico = atletico_madrid ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_atletico
    st.markdown('<div style="text-align: justify;">El Atlético de Madrid fundado en el año 1903 en la ciudad de Madrid, fue uno de los clubes fundadores de la liga española pero no ha participado en todas las ediciones, siendo que ha participado en 87 de ellas, en sus participaciones en la liga se cuentan 11 títulos de campeón de liga y 10 subcampeonatos mientras que en la Copa del Rey cuenta con 10 campeonatos y 9 subcampeonatos, en la Supercopa de España cuenta con 2 campeonatos y 5 subcampeonatos con sus logros internacionales se posiciona como el tercer mejor equipo histórico de la liga española. En la liga 2023-2024 el equipo terminó en la cuarta posición lo que le consiguió la clasificación a la fase de liga de la Champions League 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Atlético de Madrid")
    st.write("")
    atletico_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Atlético de Madrid')]
    resultados_liga_atletico = atletico_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_atletico = resultados_liga_atletico.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_atletico['fecha_campeonato'] = pd.to_numeric(resultados_liga_atletico['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_atletico['fecha_campeonato'],
    weights=resultados_liga_atletico['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#d40213',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Barcelona")
    st.image("https://a.espncdn.com/i/teamlogos/soccer/500/83.png", width = 150)
    barcelona = df[df['Equipo_local'] == 'Barcelona']
    asistencia_barcelona = barcelona ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_barcelona
    st.markdown('<div style="text-align: justify;">El F.C. Barcelona fundado en Cataluña en 1899 registrado oficialmente en 1903, es uno de los clubes fundadores de la liga española con el aditivo que no ha descendido en ninguna de las ediciones, en su palmarés figuran 27 títulos de campeón de liga y 27 subcampeonatos mientras que en la copa del rey tiene 31 campeonatos y 11 subcampeonatos en la Copa del Rey en la que es el máximo ganador sumados a los 13 campeonatos y 11 subcampeonatos de la supercopa de España lo que lo afianza con su gran palmarés internacional como el segundo mejor equipo histórico de la liga española. En la liga 2023-2024 el equipo venía como campeón vigente de la competición pero terminó en segundo lugar del torneo logrando otro subcampeonato más (28) y clasificando a la fase de liga de la Champions League 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Barcelona")
    st.write("")
    barcelona_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Barcelona')]
    resultados_liga_barcelona = barcelona_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_barcelona = resultados_liga_barcelona.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_barcelona['fecha_campeonato'] = pd.to_numeric(resultados_liga_barcelona['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_barcelona['fecha_campeonato'],
    weights=resultados_liga_barcelona['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#0909b3',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Cádiz")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/5/58/C%C3%A1diz_CF_logo.svg/1200px-C%C3%A1diz_CF_logo.svg.png", width = 100)
    cadiz = df[df['Equipo_local'] == 'Cádiz']
    asistencia_cadiz = cadiz ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_cadiz
    st.markdown('<div style="text-align: justify;">El Cádiz fundado en 1910 en la ciudad de Cádiz en la comunidad autónoma de Andalucía, cuenta con 16 participaciones en la primera división de la liga en las que su mejor posición la logró en dos años siendo el duodécimo puesto en las temporadas 1987-1988 y 2020-2021 y su palmarés es mayormente de la segunda y tercera división. Su posición en la liga 2022-2023 logró mantenerlo con vida en la primera división sin embargo en la temporada 2023-2024 terminó en la posición 18 lo que lo orilló a la zona de descenso para la temporada 2024-2025, a pesar de ello perdieron de goleada de local ante el Almería por (1-6) en un partido donde “El Cádiz se fue del partido en el segundo tiempo” esto tras tener una ventaja de 1-0 en el primer tiempo.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Cádiz")
    st.write("")
    cadiz_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Cádiz')]
    resultados_liga_cadiz = cadiz_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_cadiz = resultados_liga_cadiz.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_cadiz['fecha_campeonato'] = pd.to_numeric(resultados_liga_cadiz['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_cadiz['fecha_campeonato'],
    weights=resultados_liga_cadiz['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#fae105',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Celta de Vigo")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/12/RC_Celta_de_Vigo_logo.svg/1200px-RC_Celta_de_Vigo_logo.svg.png", width = 100)
    celta = df[df['Equipo_local'] == 'Celta de Vigo']
    asistencia_celta = celta ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_celta
    st.markdown('<div style="text-align: justify;">El club Celta de Vigo fundado en la ciudad de Vigo en  en 1923 y es el club gallego con más participaciones en la primera división de la liga española, su primera participación en la liga se dió en el año 1935 y desde entonces cuenta con 58 participaciones en las cuales no consiguió el títulos de campeón de liga Copa del Rey o Supercopa aunque posee títulos de otras divisiones inferiores. Su mejor participación en el campeonato de primera división fue en la en la temporada 2002-2003 en la cual terminó en la cuarta posición clasificando a la fase de grupos de la Champions League con el mérito de relegar a puestos de Europa League al Barcelona, equipo histórico y al Valencia quien era el vigente campeón de la competición. En la temporada 2023-2024 terminó en la posición 13 lo cual lo mantiene participando en la temporada 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Celta de Vigo")
    st.write("")
    celta_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Celta de Vigo')]
    resultados_liga_celta = celta_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_celta = resultados_liga_celta.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_celta['fecha_campeonato'] = pd.to_numeric(resultados_liga_celta['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_celta['fecha_campeonato'],
    weights=resultados_liga_celta['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#05c9fa',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Getafe")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Getafe_logo.svg/1200px-Getafe_logo.svg.png", width = 150)
    getafe = df[df['Equipo_local'] == 'Getafe']
    asistencia_getafe = getafe ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_getafe
    st.markdown('<div style="text-align: justify;">El Getafe tiene una situación peculiar sobre su fundación ya que no hay un año de fundación específico del equipo, mientras la administración de la liga española indica 1983 como año de la fundación del club, existen otros registros que datan del año 1923, sea el año de su fundación el equipo tuvo su primera participación en la liga española en el año 2004, durante sus participaciones en la liga no ha conseguido campeonar en el torneo o algún campeonato de primer orden a nivel nacional. Su mejor participación en la liga fue el quinto lugar obtenido en la temporada 2018-2019. En la temporada 2023-2024 terminó en la posición 12 logrando mantener la categoría para la temporada 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Getafe")
    st.write("")
    getafe_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Getafe')]
    resultados_liga_getafe = getafe_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_getafe = resultados_liga_getafe.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_getafe['fecha_campeonato'] = pd.to_numeric(resultados_liga_getafe['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_getafe['fecha_campeonato'],
    weights=resultados_liga_getafe['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#2e05fa',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Girona")
    st.image("https://a.espncdn.com/combiner/i?img=/i/teamlogos/soccer/500/9812.png", width = 150)
    girona = df[df['Equipo_local'] == 'Girona']
    asistencia_girona = girona ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_girona
    st.markdown('<div style="text-align: justify;">El Girona fundado en la ciudad de Girona en el año 1930 en la ciudad de Girona y participa en la liga española desde el año 2017 esto gracias al apoyo brindado al ser adquirido como parte de City Group cuya infraestructura lo hace dotarse de talentos competentes para las distintas competiciones en las que participa siendo que es el equipo con la menor cantidad de participaciones entre los equipos no tiene títulos de competición nacionales. Su mejor temporada fue en la que debutó en la primera división, la temporada 2017-2018 en la posición 10 con 50 puntos posteriormente igualado con su participación en la edición 2022-2023 en la posición (10) pero con un punto menos (49). En la liga 2023-2024 el equipo logró una histórica tercera posición en la liga lo cual le valió la participación a la fase de liga de la Champions League 2024-2025 siendo la primera vez que se clasifica a esa competición y a alguna competición internacional en su historia, añadiendo que durante varios pasajes del torneo el equipo se ubicaba en la primera posición.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Girona")
    st.write("")
    girona_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Girona')]
    resultados_liga_girona = girona_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_girona = resultados_liga_girona.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_girona['fecha_campeonato'] = pd.to_numeric(resultados_liga_girona['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_girona['fecha_campeonato'],
    weights=resultados_liga_girona['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#f0051c',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Granada")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Logo_of_Granada_Club_de_F%C3%BAtbol.svg/1200px-Logo_of_Granada_Club_de_F%C3%BAtbol.svg.png", width = 100)
    granada = df[df['Equipo_local'] == 'Granada']
    asistencia_granada = granada ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_granada
    st.markdown('<div style="text-align: justify;">El Granada fundado en el año 1931 en la ciudad Granada de la comunidad de Andalucía y su primera participación en la liga data del año 1940 contando con 27 participaciones en la competición en la cual sólo se cuenta un subcampeonato en la temporada 1958-1959 sin algún otro título como la Copa del Rey o la Supercopa y al igual que otros equipos sus títulos son en su gran mayoría de divisiones inferiores. Su mejor temporada fue en la temporada 1971-1972 en la que terminó en la posición 6. En la temporada 2023-2024 terminó en la última posición del campeonato (20) descendiendo a la segunda división para la temporada 2024-2025, esto en gran medida por su derrota ante el Girona por goleada (7-0) y la victoria del Almería al Cádiz (1-6) ambos resultados simultáneos en la última fecha.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Granada")
    st.write("")
    granada_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Girona')]
    resultados_liga_granada = granada_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_granada = resultados_liga_granada.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_granada['fecha_campeonato'] = pd.to_numeric(resultados_liga_granada['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_granada['fecha_campeonato'],
    weights=resultados_liga_granada['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#f5142a',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Osasuna")
    st.image("https://seeklogo.com/images/O/osasuna-logo-3B1A04FF7F-seeklogo.com.png", width = 150)
    osasuna = df[df['Equipo_local'] == 'Osasuna']
    asistencia_osasuna = osasuna ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_osasuna
    st.markdown('<div style="text-align: justify;">El Osasuna fundado en Pamplona Navarra en el año 1920 participa en la primera división española desde el año 1935 desde el que suma 42 participaciones entre las cuales la mejor fue en las temporadas 1990-1991 y 2005-2006 logrando la posición 4 sin embargo es en esta última la mejor debido las instancias a las que clasificó y la puntuación obtenida, (Tercera ronda previa de Champions League) y más puntos (68). A nivel nacional cuenta con dos subcampeonatos en la Copa del Rey (2005-2023). En la liga 2023-2024 el equipo terminó en la posición 11 lo cual le permite mantenerse en la primera división para la temporada 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Osasuna")
    st.write("")
    osasuna_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Osasuna')]
    resultados_liga_osasuna = osasuna_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_osasuna = resultados_liga_osasuna.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_osasuna['fecha_campeonato'] = pd.to_numeric(resultados_liga_osasuna['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_osasuna['fecha_campeonato'],
    weights=resultados_liga_osasuna['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#eb0523',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("R. C. D. Mallorca")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Rcd_mallorca.svg/1200px-Rcd_mallorca.svg.png", width = 150)
    mallorca = df[df['Equipo_local'] == 'R. C. D. Mallorca']
    asistencia_mallorca = mallorca ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_mallorca
    st.markdown('<div style="text-align: justify;">El R.C. D. Mallorca fundado en la ciudad de La Palma en el año 1916 participa en la primera división del fútbol español desde el año 1960 contando con 31 participaciones, la mejor de todas en la temporada 1998-1999 en la que ocupó el lugar 3 logrando su primera participación en la Champions League, a nivel nacional cuenta con 1 título de Copa del Rey y 3 subcampeonatos, 1 título de Supercopa y 1 subcampeonato, todos estos resultados durante un gran proceso deportivo de 10 años de duración hasta el año 2003. En la temporada 2023-2024 el equipo terminó en la posición 15 manteniendo la categoría de primera división en la temporada 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del R. C. D. Mallorca")
    st.write("")
    mallorca_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'R. C. D. Mallorca')]
    resultados_liga_mallorca = mallorca_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_mallorca = resultados_liga_mallorca.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_mallorca['fecha_campeonato'] = pd.to_numeric(resultados_liga_mallorca['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_mallorca['fecha_campeonato'],
    weights=resultados_liga_mallorca['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#d10d27',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Rayo Vallecano")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Rayo_Vallecano_logo.svg/1200px-Rayo_Vallecano_logo.svg.png", width = 150)
    rayo = df[df['Equipo_local'] == 'Rayo Vallecano']
    asistencia_rayo = rayo ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_rayo
    st.markdown('<div style="text-align: justify;">El Rayo Vallecano fundado en el año 1924 en la ciudad de Vallecas en Madrid, su primera participación en la primera división española data del año 1977 contando con 21 participaciones en las cuales no han podido conseguir algún título nacional salvo títulos de segunda y tercera división. Su mejor temporada en la liga fue en al temporada 2012-2013 en donde se ubicó en la octava posición, un hecho curioso a pesar de no quedar en zona de competencias europeas un problema legal del Málaga que había ocupado la posición 6 lo dejó fuera de competencias europeas su plaza fue pasada al puesto 7 que era al Real Betis, pero como este ya tenía la plaza de clasificación a la Europa League pasó al Rayo Vallecano pero al este no contar con la licencia de Federación Española de Fútbol (RFEF) para participar en competencias UEFA su plaza fue pasada al Sevilla. En la temporada 2023-2024 el equipo terminó en la posición 17 en el abismo de la zona de descenso logrando mantenerse en la primera división para la temporada 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Rayo Vallecano")
    st.write("")
    rayo_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Rayo Vallecano')]
    resultados_liga_rayo = rayo_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_rayo = resultados_liga_rayo.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_rayo['fecha_campeonato'] = pd.to_numeric(resultados_liga_rayo['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_rayo['fecha_campeonato'],
    weights=resultados_liga_rayo['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#f5f2f3',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Real Betis")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Real_betis_logo.svg/1200px-Real_betis_logo.svg.png", width = 150)
    betis = df[df['Equipo_local'] == 'Real Betis']
    asistencia_betis = betis ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_betis
    st.markdown('<div style="text-align: justify;">El Real Betis Balompié fundado en el año 1908 en la ciudad de Sevilla, tiene logros importantes como ser de los 9 clubes españoles que han ganado liga y Copa del Rey y el que registra más ascensos y descensos de la primera división, participa desde el año 1932 en donde fue campeón en una única ocasión en la temporada 1934-1935, 3 títulos de la Copa del Rey y 2 subcampeonatos y un subcampeonato de supercopa de España. En la temporada 2023-2024 el equipo se ubicó en la posición 7 lo que le valió la clasificación a la fase de liga de la Conference League.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Real Betis")
    st.write("")
    betis_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Real Betis')]
    resultados_liga_betis = betis_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_betis = resultados_liga_betis.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_betis['fecha_campeonato'] = pd.to_numeric(resultados_liga_betis['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_betis['fecha_campeonato'],
    weights=resultados_liga_betis['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#0aa326',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Real Madrid")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/1200px-Real_Madrid_CF.svg.png", width = 150)
    madrid = df[df['Equipo_local'] == 'Real Madrid']
    asistencia_madrid = madrid ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_madrid
    st.markdown('<div style="text-align: justify;">El Real Madrid fundado en el año 1902 en la ciudad de Madrid es considerado el mejor club de la historia de la liga española tanto por su palmarés nacional como internacional, es uno de los clubes fundadores y participa desde la primera edición del campeonato del año 1928 siendo uno de los 3 equipos que no registra descensos, en el ámbito nacional cuenta con 69 títulos 35 títulos de la liga española y 25 subcampeonatos, 20 campeonatos de la Copa del Rey y 20 subcampeonatos, 13 títulos de supercopa de España y 6 subcampeonatos. En la liga 2023-2024 el equipo consiguió el título de campeón del certamen el cual fue su título número 36 afianzándose como el más ganador del torneo.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Real Madrid")
    st.write("")
    madrid_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Real Madrid')]
    resultados_liga_madrid = madrid_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_madrid = resultados_liga_madrid.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_madrid['fecha_campeonato'] = pd.to_numeric(resultados_liga_madrid['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_madrid['fecha_campeonato'],
    weights=resultados_liga_madrid['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#f0f5f1',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Real Sociedad")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/Real_Sociedad_logo.svg/1200px-Real_Sociedad_logo.svg.png", width = 150)
    sociedad = df[df['Equipo_local'] == 'Real Sociedad']
    asistencia_sociedad = sociedad ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_sociedad
    st.markdown('<div style="text-align: justify;">La Real Sociedad fundado en el año 1907 en la ciudad de San Sebastián en la provincia de Guipúzcoa en la comunidad del País Vasco, es uno de los clubes fundadores de la liga y ha participado en 77 ediciones de la competición en las que cuenta con dos títulos de campeón de la competición y 3 subcampeonatos, 3 títulos de Copa del Rey y 4 subcampeonatos y un título de la Supercopa de España. En la temporada 2023-2024 alcanzó la posición 6 y clasificó a la fase de liga de la Europa League.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio de la Real Sociedad")
    st.write("")
    sociedad_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Real Sociedad')]
    resultados_liga_sociedad = sociedad_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_sociedad = resultados_liga_sociedad.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_sociedad['fecha_campeonato'] = pd.to_numeric(resultados_liga_sociedad['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_sociedad['fecha_campeonato'],
    weights=resultados_liga_sociedad['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#1410eb',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Sevilla")
    st.image("https://a.espncdn.com/i/teamlogos/soccer/500/243.png", width = 150)
    sevilla = df[df['Equipo_local'] == 'Sevilla']
    asistencia_sevilla = sevilla ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_sevilla
    st.markdown('<div style="text-align: justify;">El Sevilla fundado en 1890 en la ciudad de Sevilla es uno de los equipos más importantes de la primera división española, su primera participación data del año 1934 y desde entonces suma 80 participaciones en el campeonato en las que ha conseguido 1 título de campeón de liga en la temporada 1945-1946 y 3 subcampeonatos, 5 títulos de Copa del Rey y 4 subcampeonatos, un título de Supercopa de España y 4 subcampeonatos, internacionalmente tiene el récord de más títulos de Copa de Europa conseguidos siendo el vigente campeón de la competición lo que le valió la clasificación directa a la fase de grupos de la Champions League 2023-2024. En la temporada 2023-2024 logró el lugar 14 en una inexplicable debacle del rendimiento general del equipo que fue eliminado rápidamente de la Champions League y en la liga luchó desde el inicio con un riesgo de descenso.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Sevilla")
    st.write("")
    sevilla_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Sevilla')]
    resultados_liga_sevilla = sevilla_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_sevilla = resultados_liga_sevilla.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_sevilla['fecha_campeonato'] = pd.to_numeric(resultados_liga_sevilla['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_sevilla['fecha_campeonato'],
    weights=resultados_liga_sevilla['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#ededf0',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("U. D. Las Palmas")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/2/20/UD_Las_Palmas_logo.svg/1200px-UD_Las_Palmas_logo.svg.png", width = 150)
    palmas = df[df['Equipo_local'] == 'U. D. Las Palmas']
    asistencia_palmas = palmas ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_palmas    
    st.markdown('<div style="text-align: justify;">La U. D. Las Palmas fundado en el año 1949 en la ciudad de Las Palmas de Gran Canaria logrando un rápido ascenso ya que en el año logró ascender a la primera división del fútbol español en donde ha participado en 35 ocasiones, a nivel nacional sólo cuenta con un subcampeonato de la liga española (1968-1969) y un subcampeonato de la Copa del Rey (1977-1978) así como otros títulos de segunda y tercera división. En  la liga 2023-2024 el equipo terminó en la posición 16 cerca de los puestos de zona de descenso pero manteniéndose en la primera posición para la temporada 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del U. D. Las Palmas")
    st.write("")
    palmas_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'U. D. Las Palmas')]
    resultados_liga_palmas = palmas_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_palmas = resultados_liga_palmas.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_palmas['fecha_campeonato'] = pd.to_numeric(resultados_liga_palmas['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_palmas['fecha_campeonato'],
    weights=resultados_liga_palmas['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#cbd124',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Valencia")
    st.image("https://seeklogo.com/images/V/valencia-cf-logo-DE39988814-seeklogo.com.png", width = 150)
    valencia = df[df['Equipo_local'] == 'Valencia']
    asistencia_valencia = valencia ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_valencia
    st.markdown('<div style="text-align: justify;">El Valencia fundado en el año 1919 en la ciudad de Valencia de la comunidad Valenciana, su primera participación en la primera división data del año 1931, desde entonces ha participado en 89 ediciones en las cuales ha conseguido 6 campeonatos de liga española y 6 subcampeonatos 8 títulos de Copa del Rey y 10 subcampeonatos un título de Supercopa de España y 3 subcampeonatos más 2 títulos de campeonato de segunda división. En la liga 2023-2024 terminó en la posición 9 cerca de puestos de competencias europeas y renovando su condición de participante para la temporada 2024-2025.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Valencia")
    st.write("")
    valencia_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Valencia')]
    resultados_liga_valencia = valencia_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_valencia = resultados_liga_valencia.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_valencia['fecha_campeonato'] = pd.to_numeric(resultados_liga_valencia['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_valencia['fecha_campeonato'],
    weights=resultados_liga_valencia['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#ededdd',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Villarreal")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Villarreal_CF_logo-en.svg/1200px-Villarreal_CF_logo-en.svg.png", width = 150)
    villareal = df[df['Equipo_local'] == 'Villarreal']
    asistencia_villareal = villareal ['asistencia'].sum()
    st.markdown('<div style="text-align: justify;">Total de espectadores en la temporada</div>', unsafe_allow_html=True)
    asistencia_villareal
    st.markdown('<div style="text-align: justify;">El Villarreal fundado en el año 1923 en la ciudad de Castellón comunidad Valenciana, su primera participación se dio en el año 1998 y desde entonces ha conseguido participar en 24 ediciones del torneo consiguiendo un subcampeonato en la temporada 2007-2008 lo que a su vez es su mejor resultado en la liga, por otro lado en los torneos de Copa del Rey y Supercopa no registra campeonatos o subcampeonatos, sin embargo tiene  un título de Europa League conseguido en el año 2021. En la liga 2023-2024 terminó en la posición 8 un puesto menos debajo de competiciones internacionales pero asegurando su lugar en la liga 2024-2025.  </div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Asistencia al estadio del Villarreal")
    st.write("")
    villarreal_laliga = df[(df['competición'] == 'laliga') & (df['Equipo_local'] == 'Villarreal')]
    resultados_liga_villarreal = villarreal_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_villarreal = resultados_liga_villarreal.dropna(subset=['fecha_campeonato', 'asistencia'])
    resultados_liga_villarreal['fecha_campeonato'] = pd.to_numeric(resultados_liga_villarreal['fecha_campeonato'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_villarreal['fecha_campeonato'],
    weights=resultados_liga_villarreal['asistencia'],
    bins=range(1, 21),
    alpha=0.5,
    color='#edf50a',
    edgecolor='white'
        )
    plt.xlabel('Jornada de LaLiga', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(1, 20), fontsize=5)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)

    col4, col5, col6 = st.columns(3)
    col5.image("https://cdndeportes.com.do/wp-content/uploads/2024/05/WhatsApp-Image-2024-05-04-at-2.41.43-PM-1.jpeg", width = 300)
    st.markdown('<div style="text-align: center;">Real Madrid Campeón de Laliga 2023-2024</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Partido con menor audiencia")
    st.video("https://www.youtube.com/watch?v=VqNjDg3D91w")
    st.markdown('<div style="text-align: justify;">Almería (Jornada 38) 7558 asistentes : El partido se desarrolló en una instancia en el cual el tanto equipo local como visitante se encontraban en la zona de descenso sin posibilidad de subir a puestos de permanencia, sumado a que era el último partido que tenían que disputar generó un desinterés hasta del público local por asistir al partido superando negativamente al partido en donde el equipo confirmó su descenso a la segunda división contra el getafe 1-2 (Jornada 33).</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Ya en el partido entre Almería y Cádiz el visitante empezó adelantándose en el marcador en el primer tiempo pero para sorpresa de los pocos presentes en el segundo tiempo el equipo de Almería consiguió anotar 6 goles decorando de esa manera su fatal temporada de liga salvándose de terminar en el último lugar de la tabla, relegando al Granada.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("")
    st.video("https://www.youtube.com/watch?v=G4CYmWsfXOM")
    st.markdown('<div style="text-align: justify;">Real Madrid (Jornada 32) 77981 asistentes: El partido tiene contexto en el clásico español, este partido era de vital importancia para el equipo local para afianzarse en la cima de la liga, el Barcelona en cambio jugaba con la presión de ganar el partido y sumado a ello esperar tropiezos del Real Madrid en las jornadas posteriores de la liga mientras que ellos no debían de perder, la oportunidad de “sentenciar” la liga atrajo a una gran cantidad de hinchas del conjunto blanco interesados en el partido.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">El partido fue un ida y vuelta entre ambos equipos, con el Barcelona adelantándose en dos ocasiones (0-1 y 1-2), sin embargo errores puntuales llevaron al partido a las tablas (2-2) hasta el minuto 90 en donde Jude Bellingham anotó el 3-2 definitivo. Las consecuencias del partido fueron casi inmediatas, con ambos equipos ganando su siguiente partido de liga (Jornada 33) y en la jornada 34 el Real Madrid ganaría su partido contra Cádiz (3-0) mientras que el Barcelona sería derrotado 4-2 en su visita al Girona determinando que el Real Madrid se consagrase campeón de liga a falta de 4 jornadas del final.</div>', unsafe_allow_html=True)
    st.write("")


elif eleccion_campeonato == "Copa del Rey":
    col1, col2, col3 = st.columns(3)
    st.markdown("<h2 style='text-align: center;'>Copa del Rey</h2>", unsafe_allow_html=True)
    col2.image("https://imgresizer.eurosport.com/unsafe/2560x1440/filters:format(jpeg)/origin-imgresizer.eurosport.com/2021/03/24/3017043-61896588-2560-1440.jpg", width = 400)
    st.markdown('<div style="text-align: justify;">La competición contó con una ronda de preclasificación y dos rondas de clasificación, luego se dieron los enfrentamientos correspondientes a los dieciseisavos de final, octavos, cuartos, semifinales y final, participando en total unos 125 equipos, el Real Madrid fungió como campeón vigente de la competición siendo eliminado por el Atlético de Madrid en la fase de octavos de final, este a su vez fue el partido de mayor asistencia registrada en toda la competición con 63623 asistentes, lo cual remarca la importancia tanto del partido como de los equipos en la competición.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">El campeón de esta competición fue el Athletic de Bilbao quien se impuso 4-2 en la tanda de penales al R. C. D. Mallorca luego de haber empatado 1 a 1 en el tiempo regular y suplementario, el logro del equipo del país Vasco fue importante ya que era el primer título conseguido luego de 40 años luego de 6 finales perdidas entre 1984 y 2024 (1984, 1985, 2009, 2015, 2020, 2021). El estadio tuvo una asistencia de 57 619  espectadores de ambos equipos y como siempre minorías de otros equipos, este número de personas no es contado para las tablas finales ya que el partido se jugó en el Estadio de la Cartuja y al ser el recinto perteneciente al Sevilla no entra en el conteo general de asistencia.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">El torneo contó con una presencia conjunta de 1 041 638  espectadores en 126 partidos dando un promedio de 9137 asistentes por partido, de lejos este es de los promedios más bajos pero se argumenta debido a que una gran mayoría de los equipos tomados en cuenta juegan en recintos deportivos de capacidades muy bajas siendo 500 asistentes lo más común en equipos de segunda y tercera división quienes no cuentan con la misma popularidad que los equipos frecuentes en la primera división.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de asistentes en la fase interritorial</div>', unsafe_allow_html=True)
    copa_interritorial = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'] == 'interritorial') & ['asistencia']]
    total_cr_it = copa_interritorial['asistencia'].sum()
    total_cr_it
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de asistentes en la primera ronda</div>', unsafe_allow_html=True)
    copa_p1 = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'] == 'primera_ronda') & ['asistencia']]
    total_cr_p1 = copa_p1['asistencia'].sum()
    total_cr_p1
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de asistentes en la segunda ronda</div>', unsafe_allow_html=True)
    copa_s2 = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'] == 'segunda_ronda') & ['asistencia']]
    total_cr_s2 = copa_s2['asistencia'].sum()
    total_cr_s2
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de asistentes en los dieciseisavos de final</div>', unsafe_allow_html=True)
    copa_d16 = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'] == 'dieciseisavos_final') & ['asistencia']]
    total_cr_d16 = copa_d16['asistencia'].sum()
    total_cr_d16
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de asistentes en los octavos de final</div>', unsafe_allow_html=True)
    copa_o8 = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'] == 'octavos_final') & ['asistencia']]
    total_cr_o8 = copa_o8['asistencia'].sum()
    total_cr_o8
    st.markdown('<div style="text-align: justify;">Total de asistentes en los cuartos de final</div>', unsafe_allow_html=True)
    copa_c4 = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'] == 'cuartos_final') & ['asistencia']]
    total_cr_c4 = copa_c4['asistencia'].sum()
    total_cr_c4
    st.markdown('<div style="text-align: justify;">Total de asistentes en la semifinal</div>', unsafe_allow_html=True)
    copa_s2 = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'] == 'cuartos_final') & ['asistencia']]
    total_cr_s2 = copa_s2['asistencia'].sum()
    total_cr_s2
    st.subheader("Asistencia de la Copa del Rey por fases")
    st.write("")
    copa_asistencia = df[(df['competición'] == 'copa_del_rey') & (df['fecha_campeonato'])]
    copa_resultados = copa_asistencia[['fecha_campeonato', 'asistencia']]
    copa_general = copa_resultados.dropna(subset=['fecha_campeonato', 'asistencia'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    copa_general['fecha_campeonato'],
    weights=copa_resultados['asistencia'],
    bins=range(0, 7),
    alpha=0.2,
    color='#79d6b7',
    edgecolor='white'
        )
    plt.xlabel('Fase del torneo', fontsize=12)
    plt.ylabel('Asistencia', fontsize=12)
    plt.xticks(range(0, 7), fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    st.pyplot(plt)
    st.video("https://www.youtube.com/watch?v=xnBip3vHNnA")
    st.markdown('<div style="text-align: center;">Athletic de Bilbao campeón de la Copa del Rey 2023-2024</div>', unsafe_allow_html=True)


elif eleccion_campeonato == "Champions league":
    col48, col49, col50 = st.columns(3)
    st.markdown("<h2 style='text-align: center;'>Champions League</h2>", unsafe_allow_html=True)
    col49.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/%DA%86%D8%A7%D9%85%D9%BE%DB%8C%DB%86%D9%86%D8%B2%D9%84%DB%8C%DA%AF.png")
    st.markdown('<div style="text-align: justify;">La Champions League contó con la presencia de 5 equipos, el Sevilla clasificado por ser campeón de la Europa League 2022-2023 y el Barcelona, Real Madrid, Atlético de Madrid y Real Sociedad clasificados bajo el sistema de clasificación por ligas.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">En la primera fase se disputaron 3 partidos de local por cada equipo los cuales llevaron a un total de 731 745 espectadores entre todos los equipos siendo de nuevo el Real Madrid con 207 278 espectadores lo cual comprende el 28% del total de asistentes en esta fase, esto ya resultado por lo que supone esta competición para el conjunto merengue el cual es el más veces campeón de la competición con 14 títulos.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Todos los equipos tuvieron desenlaces directos como lo son el Barcelona, Real Madrid, Atlético de Madrid y Real Sociedad pasando a la fase de octavos de final mientras que el Sevilla fue eliminado de manera directa tanto del torneo como de la posibilidad de disputar la fase de eliminación de la Europa League quedando en el cuarto lugar de su grupo. </div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">En los octavos de final el único equipo que quedó eliminado fue la Real Sociedad mientras que el Barcelona, Real Madrid y Atlético de Madrid avanzaron a los cuartos de final, la estancia de los octavos de final juntó a 234 959 asistentes en los estadios lo que es el 19% de los totales en toda la competición, otra vez el Real Madrid es el equipo con mayor asistencia con 76 126 asistentes representando el 39% del total en esta instancia.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Los cuartos de final dejaron al Real Madrid como el único equipo español con vida en la competición tras las eliminaciones del Barcelona (2 - 3 de visita y 1 - 4 de local) y el Atlético de Madrid (2 - 1 local y 4 - 2 visitante) el equipo merengue logró empatar los dos partidos ante el Manchester City e imponerse por medio de la vía de los penales, a pesar de que el único partido que se jugó de vuelta fue el del Barcelona este no pudo superar al partido entre Real Madrid y Manchester City jugado en el Santiago Bernabeu con 76 680 asistentes es el partido más visto de la fase. En comparación con la asistencia de toda la competencia los partidos representaron el 16% del total del torneo.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">En las semifinales se encontraba un único equipo que era el Real Madrid, en esta instancia se encontró con el Bayern de Múnich, el partido de ida en Alemania terminó en un 2-2 y todo quedaba a expectativa en la vuelta en España, casi al minuto 68 Davies anotaba el gol que adelantaba a la visita pero ya en el final del partido dos goles casi instantáneos de Joselu al 90 y 90+1 sentenciaron el partido logrando así que el Real Madrid accediera a la final. La asistencia del Santiago Bernabeu fue de 76 759 personas lo que representa la totalidad de la fase y el 6% del total del torneo.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Como en los torneos de formato de final única la sede suele ser en un estadio neutral y aunque se dé la casualidad de que el equipo del estadio llegue a la final no se cuenta para efectos de estadísticas tanto uno como otro escenario el total de asistentes del torneo por parte de la liga española es de 1 238 643 personas el 9% entre todas las competiciones en las que participaron equipos españoles.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de asistentes del Real Madrid en la Champions League</div>', unsafe_allow_html=True)
    rm_champions = df[(df['competición'] == 'champions_league') & (df['Equipo_local'] == 'Real Madrid') & ['asistencia']]
    total_rm_ch = rm_champions['asistencia'].sum()
    total_rm_ch
    st.markdown('<div style="text-align: justify;">Total de asistentes del Barcelona en la Champions League</div>', unsafe_allow_html=True)
    barcelona_champions = df[(df['competición'] == 'champions_league') & (df['Equipo_local'] == 'Barcelona') & ['asistencia']]
    total_barcelona_ch = barcelona_champions['asistencia'].sum()
    total_barcelona_ch
    st.markdown('<div style="text-align: justify;">Total de asistentes del Sevilla en la Champions League</div>', unsafe_allow_html=True)
    sevilla_champions = df[(df['competición'] == 'champions_league') & (df['Equipo_local'] == 'Sevilla') & ['asistencia']]
    total_sevilla_ch = sevilla_champions['asistencia'].sum()
    total_sevilla_ch
    st.markdown('<div style="text-align: justify;">Total de asistentes del Atlético de Madrid en la Champions League</div>', unsafe_allow_html=True)
    atletico_champions = df[(df['competición'] == 'champions_league') & (df['Equipo_local'] == 'Atlético de Madrid') & ['asistencia']]
    total_atleti_ch = atletico_champions['asistencia'].sum()
    total_atleti_ch
    st.markdown('<div style="text-align: justify;">Total de asistentes de la Real Sociedad en la Champions League</div>', unsafe_allow_html=True)
    rs_champions = df[(df['competición'] == 'champions_league') & (df['Equipo_local'] == 'Real Sociedad') & ['asistencia']]
    total_rs_ch = rs_champions['asistencia'].sum()
    total_rs_ch
    st.subheader("Gráfico de assitentes en la champions league por participantes")
    st.write("")
    equipos = ['Real Madrid', 'Barcelona', 'Sevilla', 'Atlético de Madrid', 'Real Sociedad']
    champions = df[(df['competición'] == 'champions_league') & (df['Equipo_local'].isin(equipos))]
    asistencia_champions = champions.groupby('Equipo_local')['asistencia'].sum()
    plt.figure(figsize=(6, 6))
    plt.pie(asistencia_champions, labels=asistencia_champions.index, autopct='%1.1f%%', startangle=90, colors=['#1b676b', '#519548', '#88c425', '#bef202', '#aaa7b8'])
    plt.axis('equal')
    plt.tight_layout()
    st.pyplot(plt)
    st.video("https://www.youtube.com/watch?v=4EALtccIQ-U")
    st.markdown('<div style="text-align: center;">Real Madrid campeón de la Champions League 2023-2024</div>', unsafe_allow_html=True)


elif eleccion_campeonato == "Europa league":
    col1, col2, col3 = st.columns(3)
    st.markdown("<h2 style='text-align: center;'>Europa League</h2>", unsafe_allow_html=True)
    col2.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/UEFA_Europa_League_logo_%282024_version%29.svg/1200px-UEFA_Europa_League_logo_%282024_version%29.svg.png", width = 300)
    st.markdown('<div style="text-align: justify;">Los equipos clasificados a la Europa League fueron el Villarreal y el Real Betis debido al sistema de clasificación de la liga española de la temporada 2022-2023, en la fase de grupos ambos equipos lograron reunir a 174 001 espectadores el 92% del total, en esta fase el Villarreal consiguió clasificar a la fase de octavos de final mientras que el Real Betis quedó en la tercera posición de su grupo y fue relegado a los dieciseisavos de final de la Conference league.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">En su partido de octavos de final el Villarreal se enfrentó al Olympique de Marsella con el que perdió 4-0 en su visita a Francia con un panorama muy incierto para la vuelta generando el interés de sus hinchas por asistir, ya en el partido estuvieron ganando 3-0 de manera parcial hasta que un gol de Clauss al 90+4 sentenció la eliminatoria. El partido tuvo una asistencia de 15 378 siendo el segundo mejor de la competición para el Villarreal representando el 8% del total de la competición.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">En total la competición congregó a 189 379 espectadores lo cual supone el 1% del total entre todas las competiciones.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de asistentes del Villarreal en la Europa League</div>', unsafe_allow_html=True)
    villarreal_europa = df[(df['competición'] == 'europa_league') & (df['Equipo_local'] == 'Villarreal') & ['asistencia']]
    total_villarreal_eu = villarreal_europa['asistencia'].sum()
    total_villarreal_eu
    st.markdown('<div style="text-align: justify;">Total de asistentes del Real Betis en la Europa League</div>', unsafe_allow_html=True)
    betis_europa = df[(df['competición'] == 'europa_league') & (df['Equipo_local'] == 'Real Betis') & ['asistencia']]
    total_betis_eu = betis_europa['asistencia'].sum()
    total_betis_eu

    st.subheader("Asistencia del Villarreal")
    st.write("")
    villarreal_laliga = df[(df['competición'] == 'europa_league') & (df['Equipo_local'] == 'Villarreal')]
    resultados_liga_villarreal = villarreal_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_villarreal = resultados_liga_villarreal.dropna(subset=['fecha_campeonato', 'asistencia'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_villarreal['fecha_campeonato'],
    weights=resultados_liga_villarreal['asistencia'],
    bins=range(0, 5),
    alpha=0.5,
    color='#f9d423',
    edgecolor='white'
        )
    plt.xlabel('Fecha de Europa League', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(0, 5), fontsize=5)
    plt.yticks(fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

    st.subheader("Asistencia del Real Betis")
    st.write("")
    betis_laliga = df[(df['competición'] == 'europa_league') & (df['Equipo_local'] == 'Real Betis')]
    resultados_liga_betis = betis_laliga[['fecha_campeonato', 'asistencia']]
    resultados_liga_betis = resultados_liga_betis.dropna(subset=['fecha_campeonato', 'asistencia'])
    plt.figure(figsize=(12, 8))
    plt.hist(
    resultados_liga_betis['fecha_campeonato'],
    weights=resultados_liga_betis['asistencia'],
    bins=range(0, 4),
    alpha=0.5,
    color='#23b004',
    edgecolor='white'
        )
    plt.xlabel('Fecha de Europa League', fontsize=10)
    plt.ylabel('Asistencia Total', fontsize=10)
    plt.xticks(range(0, 4), fontsize=5)
    plt.yticks(fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)
    st.video("https://www.youtube.com/watch?v=5UXtgNOL7Y0")
    st.markdown('<div style="text-align: center;"> Partido de vuelta octavos de final Villarreal - Marsella</div>', unsafe_allow_html=True)

elif eleccion_campeonato == "Conference league":
    col1, col2, col3 = st.columns(3)
    st.markdown("<h2 style='text-align: center;'>Conference League</h2>", unsafe_allow_html=True)
    col2.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/UEFA_Conference_League_full_logo_%282024_version%29.svg/800px-UEFA_Conference_League_full_logo_%282024_version%29.svg.png", width = 300)
    st.markdown('<div style="text-align: justify;">Para efectos de las estadísticas cuentan como equipos participantes los que juegan las fases preliminares de un torneo internacional el cual es el caso del Osasuna en la Conference League, por su posición en la liga y de acuerdo al ranking de ligas de la UEFA el equipo fue ubicado en la cuarta fase de clasificación, es decir que si ganaban su partido clasificaban a la fase de grupos de la Conference League pero fueron vencidos por el club Brujas de Bélgica, en su partido de local fueron derrotados 1 - 2 mientras que en su visita a Bélgica lograron empatar 2 - 2 esto a pesar de haber volteado el global de la eliminatoria al minuto 57 (1 - 2) pero en los minutos 73 y 76 el Brujas anotó los goles de la clasificación. El partido en España trajo 21 985 espectadores lo cual supone el 47% del total de españoles en la competición.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">El otro equipo participante es el Real Betis quien había terminado en la competición por su posición en la Europa League terminó en los dieciseisavos de final emparejado con el Dinamo Zagreb de Croacia un equipo importante en el panorama europeo por su constancia en las distintas competiciones, el partido de ida se disputó en España con derrota del equipo local por la mínima diferencia (0-1), en la vuelta en Croacia el equipo español se adelantó en el marcador empatando el global al minuto 38 sin embargo en el segundo tiempo el equipo local anotó el gol del empate al minuto 59 por lo que aguantó el resultado lo que quedó del partido y eliminó de esta manera al Real Betis. El saldo del partido en españa fue de 25 901 asistentes lo cual supone el 53% del total en la competición.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">El total de los equipos españoles participantes de esta competición fue de 47 076, el 0.3% entre todas las competiciones de la temporada siendo un número muy bajo que se justifica por la cantidad de equipos y los partidos jugados.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de participantes del Osasuna en la Conference League</div>', unsafe_allow_html=True)
    osasuna_conference = df[(df['competición'] == 'conference_league') & (df['Equipo_local'] == 'Osasuna') & ['asistencia']]
    total_osa_conference = osasuna_conference['asistencia'].sum()
    total_osa_conference
    st.write("")
    st.markdown('<div style="text-align: justify;">Total de participantes del Real Betis en la Conference League</div>', unsafe_allow_html=True)
    betis_conference = df[(df['competición'] == 'conference_league') & (df['Equipo_local'] == 'Real Betis') & ['asistencia']]
    total_betis_conference = betis_conference['asistencia'].sum()
    total_betis_conference
    st.video("https://www.youtube.com/watch?v=q0FAmxDzZKg")
    st.markdown('<div style="text-align: center;">Partido del Real Betis de local</div>', unsafe_allow_html=True)

elif eleccion_campeonato == "Estadísticas":
    st.markdown("<h2 style='text-align: center;'>Estadísticas</h2>", unsafe_allow_html=True)
    st.write("")
    st.subheader("")
    st.image("https://www.2playbook.com/uploads/s1/30/64/82/santiago-bernabeu-2023.jpeg", width = 600)
    st.markdown('<div style="text-align: justify;">Real Madrid tiene la mayor cantidad de público en el 95% de las localidades (18), luego le sigue el Atlético de Madrid con el otro 5% (1), esto demuestra la gran influencia del equipo Merengue para atraer a una gran cantidad de hinchas, que van motivados gracias a la gran cantidad de títulos nacionales como internacionales que consigue el equipo, sumado a ello el equipo tiene el estadio con mayor capacidad del torneo. El Atlético de Madrid por su parte tiene el segundo estadio con mayor capacidad con una afluencia impresionante, siendo que el partido con más asistencia ha sido el Derbi entre Atlético de Madrid y Real Madrid.</div>', unsafe_allow_html=True)
    st.write("")
    st.image("https://www.ecured.cu/images/6/66/Coliseum_alfonso_perez.jpg", width = 600)
    st.markdown('<div style="text-align: justify;">Getafe tiene la menor cantidad de público en el 53% de las localidades (10), le siguen el Girona y Almería con 21% cada uno (4), finalmente el Granada con el 5% (1).</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("La mejor y peor localidad por jornada")
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 1 Mejor: Real Madrid (Real Madrid - Getafe, Jornada 4)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 1 Peor: Girona (Girona - Getafe, Jornada 2)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 2 Mejor: Real Madrid (Real Madrid - Real Sociedad, Jornada 5)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 2 Peor: Getafe (Getafe - Alavés, Jornada 3)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 3 Mejor: Atlético de Madrid (Atlético de Madrid - Jornada 6)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 3 Peor: Getafe (Getafe - Osasuna, Jornada 5)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 4 Mejor: Real Madrid (Real Madrid - Osasuna, Jornada 9)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 4 Mejor: Getafe (Getafe - Villarreal, Jornada 8)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 5 Mejor: Real Madrid (Real Madrid - Rayo Vallecano, Jornada 12)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 5 Peor: Girona (Girona - Almería, Jornada 10)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 6 Mejor: Real Madrid (Real Madrid - Valencia, Jornada 13)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 6 Peor: Getafe (Getafe - Cádiz, Jornada 12)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 7 Mejor: Real Madrid (Real Madrid - Granada, Jornada 15)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 7 Peor: Getafe (Getafe - Almería, Jornada 14)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 8 Mejor: Real Madrid (Real Madrid - Villarreal, Jornada 17)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 8 Peor: Getafe (Getafe - Valencia, Jornada 16)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 9 Mejor: Real Madrid (Real Madrid - Mallorca, Jornada 19)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 9 Peor: Getafe (Getafe - Rayo Vallecano, Jornada 19)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 10 Mejor: Real Madrid (Real Madrid - Almería, Jornada 21)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 10 Peor: Almería (Almería - Girona, Jornada 20)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 11 Mejor: Real Madrid (Real Madrid - Atlético de Madrid, Jornada 23)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 11 Peor: Getafe (Getafe - Granada, Jornada 22)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 12 Mejor: Real Madrid (Real Madrid - Girona, Jornada 24)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 12 Peor: Getafe (Getafe - Celta de Vigo, Jornada 24)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 13 Mejor: Real Madrid (Real Madrid - Sevilla, Jornada 26)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 13 Peor: Getafe (Getafe -U. D. Las Palmas, Jornada 27)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 14 Mejor: Real Madrid (Real Madrid - Celta de Vigo, Jornada 28)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 14 Peor: Girona (Girona - Osasuna, Jornada 28)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 15 Mejor: Real Madrid (Real Madrid - Athletic de Bilbao, Jornada 30)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 15 Peor: Granada (Granada - Real Sociedad, Jornada 28)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 16 Mejor: Real Madrid (Real Madrid - Barcelona, Jornada 32)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 16 Peor: Almería (Almería - Villarreal, Jornada 32)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 17 Mejor: Real Madrid (Real Madrid - Cádiz, Jornada 34)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 17 Peor: Almería (Almería - Getafe, Jornada 33)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 18 Mejor: Real Madrid (Real Madrid - Alavés, Jornada 36)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 18 Peor: Girona (Girona - Villarreal, Jornada 36)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Localidad 19 Mejor: Real Madrid (Real Madrid - Real Betis, Jornada 38)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Localidad 19 Peor: Almería (Almería - Cádiz, Jornada 38)</div>', unsafe_allow_html=True)
    st.write("")
    st.image("https://fotografias.antena3.com/clipping/cmsimages01/2024/06/04/85C9A955-E1C1-4448-9EEE-7971232A38E8/florentino-coloca-decimoquinta-copa-europa-blanca_104.jpg?crop=546,546,x0,y0&width=1200&height=1200&optimize=low&format=webply", width = 600)
    st.markdown('<div style="text-align: justify;">Real Madrid tiene la mayor cantidad de público en el 95% de las localidades (18), luego le sigue el Atlético de Madrid con el otro 5% (1), esto demuestra la gran influencia del equipo Merengue para atraer a una gran cantidad de hinchas, que van motivados gracias a la gran cantidad de títulos nacionales como internacionales que consigue el equipo, sumado a ello el equipo tiene el estadio con mayor capacidad del torneo. El Atlético de Madrid por su parte tiene el segundo estadio con mayor capacidad con una afluencia impresionante, siendo que el partido con más asistencia ha sido el Derbi entre Atlético de Madrid y Real Madrid.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Asimismo reafirma su gran popularidad como el mejor equipo de la liga española, con la mayor afluencia total y la mayor afluencia en promedio a su estadio, manteniendo estos números de manera constante a lo largo de los 19 partidos que le tocó jugar de local siendo superado por única en el “Derbi Madrileño” o “Clásico de Madrid” en el cual se enfrentan los equipos del Real Madrid y Atlético de Madrid</div>', unsafe_allow_html=True)
    st.write("")
    st.image("https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2023/07/11/el-coliseum-alfonso-perez-tras-el-getafe-tenerife-del-ascenso-de-2017.jpeg", width = 1200)
    st.markdown('<div style="text-align: justify;">Getafe tiene la menor cantidad de público en el 53% de las localidades (10), le siguen el Girona y Almería con 21% cada uno (4), finalmente el Granada con el 5% (1).</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Aunque podamos deber la cantidad de espectadores a la capacidad total del estadio del Getafe es de ver que de acuerdo a la capacidad total del estadio los números rara vez pasó del 80% de la capacidad total, siendo en 2 veces (82% y 90% respectivamente) que se dió esta situación por lo que la necesidad de los hinchas por asistir no es una condicional de ello ya que el promedio de costo de entradas es de entre 40 y 90 euros haciéndolo accesible para los que buscan asistir a un partido.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Equipo con el mejor porcentaje de asistencia")
    st.markdown('<div style="text-align: justify;">Granada 105% (Jornada 18)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Partido: Granada - Sevilla</div>', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=t11sz4zP9kw")
    st.markdown('<div style="text-align: justify;">Este gran porcentaje de asistencia se resume en una sobre asistencia en la sede ya que a diferencia de otros equipos en situaciones puntuales que cambian de sede de estadio, el Granada tiene la locación del partido en el mismo estadio con el que ha jugado, los registros datan de un 105% de asistencia al partido, la razón sería debido al “Derbi Andaluz” partido que enfrenta a los equipos de la región autónoma de Andalucía Granada y Sevilla siendo este último que pasaba por una mala racha y su tercer director técnico en lo que iba de liga, el partido creó expectativa en poder aprovechar esa mala situación para sumar puntos en la tabla general, sin embargo el partido fue una goleada 0 - 3 por parte del equipo visitante que mantuvo el mal momento del Granada en la zona de descenso, zona en la que se quedaría hasta el final de temporada.</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Equipo con el peor porcentaje registrado")
    st.markdown('<div style="text-align: justify;">Getafe 45% (Jornada 27)</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div style="text-align: justify;">Partido: Getafe - U. D. Las Palmas</div>', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=W_mtPr93TkM")
    st.markdown('<div style="text-align: justify;">Con el equipo de getafe en la décima posición y el visitante en la sorpresiva octava posición este partido de media tabla no tendría importante injerencia en la situación final de la tabla para ambos equipos y puesto a que el rival no era comercialmente “atractivo” para los aficionados sumado al mal momento del equipo en lugar de crear expectativa y más asistencia, este fue un partido más en el cual ambos equipos empataron 3 - 3 en un partido en donde el equipo local se adelantó hasta quedar 3 - 1 en la primera mitad, en la segunda parte del partido el equipo visitante logró igualar el partido en los primeros minutos del segundo tiempo el partido se mantuvo así hasta su final. Los efectos fueron negativos para el Getafe que bajó del lugar 10 al 11 mientras que el visitante logró mantener su octavo lugar en la tabla.</div>', unsafe_allow_html=True)
    st.write("")