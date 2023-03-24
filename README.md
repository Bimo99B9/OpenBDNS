# Web Scraping: Recuperando datos.
Daniel López Gala - 03/03/2023 at Hack&Beers Gijón
@Bimo99B9
danilopezgala@gmail.com

Notas de la ponencia.

---
# ¿Qué es el web scraping y cómo funciona?

## Concepto de Web Scraping.

Extracción de datos de un sitio web.
datos no estructurados en formato HTML

- El rastreador (araña)
 inteligencia artificial que navega por Internet para indexar y buscar contenido siguiendo enlaces y explorando

* El raspador (scraper)
herramienta especializada diseñada para extraer datos de una página web de forma precisa y rápida. localizadores de datos (o selectores) que se utilizan para encontrar los datos que desea extraer del archivo HTML

## Proceso de Web Scraping.

1.  Bot de extracción, envía una **solicitud HTTP** GET a un sitio web específico.
2.  Cuando el sitio web responde, el scraper analiza el documento HTML para buscar un **patrón de datos específico**.
3.  Una vez se hayan extraído los datos, se convierten a cualquier **formato específico** proyectado por el autor del bot de scraper.

-   Identificar el sitio web de destino
-   Recopila las URL de las páginas de las que deseas extraer datos
-   Realiza una solicitud a estas URL para obtener el HTML de la página.
-   Utiliza localizadores para encontrar los datos en el HTML
-   Guarda los datos en un archivo JSON o CSV o en algún otro formato estructurado

Este proceso conlleva:
- Evasión de Web Application Firewalls (WAFs)
- Evasión de sistemas de detección y prevención de intrusiones (IPS/IDS)
- Incluso métodos que aplican deep learning para simular el comportamiento humano. (IA?) -> Saltarse Captchas.

## Fases del ataque.
![[assets/Pasted image 20230303201403.png]]

Página muy completa:
https://securityboulevard.com/2018/10/how-scraping-attacks-can-compromise-web-security-and-impact-business-continuity/

Uso de botnets:
https://www.iebschool.com/blog/que-es-el-web-scrapping-y-como-se-utiliza-en-los-negocios-digital-business/
![[assets/Pasted image 20230303203057.png]]


---
# Legalidad.

Es una práctica **polémica**.
Los bots se diseñan para parecer humanos y pueden usar cuentas falsas.
Puede crear problemas en las páginas analizadas.

Cualquier dato disponible públicamente al que todos puedan acceder en Internet se puede extraer legalmente.

Los datos deben seguir estos 3 criterios para que se extraigan legalmente:
-   El usuario ha hecho públicos los datos
-   No se requiere una cuenta para acceder
-   No bloqueado por el archivo robots.txt
Siempre que siga estas 3 reglas, es legal.

No obstante:
La normativa señala que el hecho de que una página web sea pública, accesible o indexable **no implica, de ninguna manera, que se puedan extraer sus datos**. Esta técnica solo está permitida en los siguientes supuestos:

-   Son **fuentes de acceso público** o los datos se recaban por un fin de **interés público** general.
-   Prevalece el interés del responsable del tratamiento sobre el derecho a la protección de datos.
-   La persona rastreada lo es bajo su consentimiento.

![[assets/Pasted image 20230303200509.png]]

---
# Ejemplos de Web Scraping

¿Web Scraping == Data Leaks?
En teoría no, ya que se supone que la información es pública.

Pero...

- En abril de 2019, se descubrió que Facebook había expuesto más de **530 millones de registros de usuarios en servidores públicos sin protección**. Los datos habían sido recopilados por dos aplicaciones externas que usaban el web scraping para extraer información del perfil público de Facebook. Los datos incluían comentarios, me gusta, nombres y reacciones. Facebook dijo que había eliminado los datos y que estaba trabajando con las aplicaciones para asegurarse de que no volviera a ocurrir(https://www.bbc.com/mundo/noticias-46426990). (https://www.bleepingcomputer.com/news/security/533-million-facebook-users-phone-numbers-leaked-on-hacker-forum/) (https://www.bleepingcomputer.com/news/security/meta-fined-265m-for-not-protecting-facebook-users-data-from-scrapers/)
Entre estos datos además había 533M de números de teléfono de los usuarios, localizaciones, estado de relación y direcciones de correo electrónico. Recibieron una multa de $275.5 millones de dólares. El atacante se llamaba Tom Liner.

- En abril de 2021, se filtraron los datos de 1,3 millones de usuarios de la aplicación Clubhouse en un foro público. Los datos incluían nombres, nombres de usuario, identificadores de Twitter e Instagram y otros detalles personales. El responsable del ataque dijo que había usado el web scraping para extraer la información de la API pública de Clubhouse. Clubhouse negó que se tratara de una filtración y dijo que los datos eran públicos y accesibles para cualquiera(https://www.bbc.com/mundo/noticias-57835205)
https://fireup.pro/blog/1-3-million-database-with-clubhouse-users-available-to-the-public-its-not-a-leak-its-data-scraping
Se habla de que los cibercriminales "ganan dinero vendiendo datos" que, quizás por error, son públicos.

Clubhouse defendió que la información era pública.

- En julio de 2021, un atacante afirmó haber robado los datos de **700 millones de usuarios de LinkedIn** usando web scraping(https://www.bbc.com/mundo/noticias-57835205). El ciberdelincuente vendió la base de datos en un foro por unos 5.000 dólares. La información incluía nombres, números de teléfono, direcciones de correo electrónico y otros detalles personales. LinkedIn dijo que estaba investigando el incidente y que tomaría medidas legales contra el responsable. Múltiples ventas por $5000

El atacante dijo que tuvo que piratear la API de LinkedIn ya que si haces demasiadas solicitudes el sistema te banea.

LinkedIn dijo que no fue una filtración de datos, que los datos eran públicos, pero que su extracción era una violación de sus términos de servicio. En resumen, que se limpiaron las manos diciendo que como era público no pasaba nada, pero la realidad es que les han robado parte de la base de datos.

Artículo bastante completo:
https://www.elimparcial.com/mundo/Scraping-Robe-los-datos-de-700-millones-de-usuarios-de-LinkedIn-por-diversion-20210714-0015.html

---
# Web Scraping en Threat Intelligence
https://cyberprotection-magazine.com/web-scraping-a-critical-tool-for-threat-intelligence

La inteligencia de amenazas ayuda a los profesionales a:

- Comprender los métodos y objetivos de los ciberdelincuentes 
- Entrenar a equipos de seguridad
- Lleva a la creación de herramientas y sistemas que protejan los datos y prevengan futuros ataques.

La inteligencia de amenazas utiliza información y habilidades recopiladas de todos los niveles de la web, incluyendo foros de la darknet y otras webs con el objetivo de identificar y minimizar posibles ciberataques.

Por tanto para una inteligencia relevante y actual, se utilizan técnicas de web scraping para recorrer la web y extraer información de determinados sitios web.

Los ciberdelincuentes intentan **escapar de la detección** identificando los servidores de la empresa de ciberseguridad y **bloqueando sus direcciones IP**. Para solucionar este problema, se utilizan **proxies** residenciales y de centro de datos para mantener el anonimato, evitar restricciones de ubicación geográfica y equilibrar las solicitudes del servidor para evitar prohibiciones.

https://oxylabs.io/blog/pdf/2021/03/Guide-to-Threat-Intelligence-Data-Acquisition.pdf
Entonces, se utiliza web scraping como herramienta de recopilación de datos de fuentes públicas como noticias o blogs, pero también de fuentes privadas como foros de la dark web. 

Esto da a las empresas de ciberseguridad información fresca y actualizada en tiempo real sobre nuevas posibles amenazas.

Este procedimiento es mucho más óptimo si está automatizado con web scraping que si se hace manualmente. Construir una herramienta de web scraping es bastante sencillo. La dificultad es mantener un flujo constante de datos y sobrepasar algoritmos para detectar estas herramientas.

![[assets/Pasted image 20230304114047.png]]
Fuente: https://scholar.uc.edu/downloads/pr76f495c?locale=en

Se usan herramientas de procesamiento de lenguaje natural (NLP), o perceptrones multicapa (MLP) como clasificadores para procesar toda la información minada y extraída con estas técnicas con el objetivo de dar alertas de amenazas en tiempo real.
https://www.misp-project.org/

---
# BDNS

Créditos: https://twitter.com/JaimeObregon/status/1508880926587056128?s=20&t=RZUOY0eIfeHNAVjXutxybw

![[assets/Pasted image 20230317233001.png]]

Flujo de solicitudes:

1 - Conseguir Cookies iniciales
![[assets/Pasted image 20230321222424.png]]

2 - Actualización de la cookie:
![[assets/Pasted image 20230321222719.png]]
![[assets/Pasted image 20230321223416.png]]

Se utiliza un token CSRF para validar la sesión.

![[assets/Pasted image 20230319213952.png]]

Esa solicitud lleva un parámetro "`_csrf`" escondido en la web.
![[assets/Pasted image 20230320124305.png]]

El token CSRF (Cross-Site Request Forgery) se utiliza para evitar ataques de falsificación de solicitudes en sitios cruzados. Un ataque CSRF ocurre cuando un atacante intenta hacer que un usuario realice una acción en un sitio web sin su conocimiento o consentimiento.

Para evitar esto, se utiliza un token CSRF que se genera al inicio de una sesión de usuario y se almacena en un campo oculto en el formulario de la página. Cuando el usuario envía un formulario, el token CSRF se incluye en la solicitud y se compara con el token almacenado en el servidor para validar la solicitud.

De esta manera, si un atacante intenta falsificar una solicitud en nombre del usuario, no tendrá acceso al token CSRF y la solicitud será rechazada por el servidor. En resumen, el uso de tokens CSRF es una medida de seguridad importante para proteger los sitios web contra ataques de falsificación de solicitudes en sitios cruzados.

3- Con la cookie de sesión validada, se llama a la búsqueda:
3.1 - Respuesta válida
![[assets/Pasted image 20230321231832.png]]


3.2 - Respuesta si no se siguieron los pasos de antes y sólo se llama a la búsqueda
![[assets/Pasted image 20230321231924.png]]

No devuelve "302 Moved Temporarily", sino un 200 con 0 filas en el JSON resultado.
El 302 lo devolvería si la cookie no fuese válida, pero este 200 "falso" es porque no se aprobó el tóken CSRF en el POST.



Tenemos que recuperarlo haciendo una solicitud a la web y buscando en la respuesta.

El código:
![[assets/beautify-picture (2).png]]

![[assets/beautify-picture (3).png]]

![[assets/beautify-picture (4).png]]

![[assets/beautify-picture (5).png]]

![[assets/beautify-picture (4).png]]


![[assets/Pasted image 20230320180641.png]]


![[assets/Pasted image 20230320180723.png]]

![[assets/Pasted image 20230321231613.png]]



La web se cayó:
![[assets/Pasted image 20230318131519.png]]

# AutoUniCalendar

**Imagen AutoUniCalendar**


**Imagen calendario SIES**


**Imagen calendario en Outlook**

**Imagen Cookies en el navegador**

Las peticiones HTTP Para analizar las peticiones hechas al servidor usé burpsuite y foxyproxy. Intercepté la petición principal para cargar el calendario en el SIES, y me di cuenta de que era una petición HTTP GET que usa dos parámetros relevantes, JSESSIONID y oam.Flash.RENDERMAP.TOKEN.

Esos parámetros son la cookie de la sesión del usuario, que es un identificador temporal de su sesión, y desde un punto de vista de seguridad, solo se podría usar para suplantar la sesión, pero no tendríamos el nombre de usuario y la contraseña expuestos, y un token Flash necesario para procesar el calendario. Ambos se pueden obtener pulsando F12 en el navegador web y navegando a Aplicación --> Almacenamiento --> Cookies, y serán los parámetros del script.

**Imagen Burpsuite y explicación parámetros**

**Función para enviar la primera solicitud con las cookies**

**Extrar y procesar las cookies adicionales de la primera solicitud**

**Enviar la solicitud para obtener los datos sin procesar del calendario**

**Convertir los datos a CSV con formato de calendario**

**Proceso resumido**

**Output del proceso**



****

# Conclusiones y consideraciones
Hablar de IA + Scraping
![[assets/Pasted image 20230319105423.png]]


# ScrapingBee
TOPP
https://www.scrapingbee.com/blog/

Curl a Python
https://curlconverter.com/python-httpclient/
![[assets/Pasted image 20230321233308.png]]

ChatGPT:

![[assets/Pasted image 20230319223349.png]]

