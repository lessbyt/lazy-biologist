# lazzy-biologist

Este script fue creado con el objetivo de analizar imágenes de cámaras trampa de una forma más rápida (y perezosa) con ayuda de python y [google vision](https://cloud.google.com/vision).

Este script carga las imágenes a procesar, y con ayuda de la API de Google, trata de identificar que objeto se encuentra en la imagen, después por cada categoría va creando una carpeta para ordenar las imágenes…. Se crean dos carpetas por defecto: “NPI” donde se colocan las imágenes que Google no pudo identificar y se crea la carpeta “Otro” donde se guardan las imágenes que tienen menos de un 70% de coincidencia

El script no es del todo perfecto pero al menos sirve para hacer una limpieza inicial. Se recomienda validar de forma manual los resultados.

# Setup

## [Python](https://pypi.org/project/google-cloud-vision/)

Para poder comenzar se crea un ambiente aislado en Python donde se instalará lo necesario para trabajar, en este caso google-cloud-vision


    pip install virtualenv

    virtualenv <your-env>

    source <your-env>/bin/activate
    
    <your-env>/bin/pip install google-cloud-vision


Ejemplo:


    pip install virtualenv

    virtualenv lazzy_biologist

    source lazzy_biologist/bin/activate

    lazzy_biologist/bin/pip install google-cloud-vision


## [Google](https://codelabs.developers.google.com/codelabs/cloud-vision-api-python/index.html?index=..%2F..index#0)

Se necesita tener una cuenta en:
    
    https://console.cloud.google.com
    
Una vez dentro, es necesario crear un proyecto. Se necesita agregar un método de pago para usar la API, pero si eres nuevo te regalan $300. (Yo coloqué una tarjeta en la cual no tengo dinero y hasta la fecha llevo 3487 imágenes procesadas y no me han cobrado nada, incluso tengo el crédito que me regalaron intacto. No sé cómo funcione)

Una vez creado el proyecto es necesario habilitar la API, para esto es necesario navegar a la sección  ``APIs & Services``, se selecciona ``Library`` y se busca ``Cloud Vision API``

Tras quedar habilitada la API, es necesario dar los permisos necesarios para poder hacer consultas. Desde la consola, en el apartado de APIs & Services , seleccionar “Credentials” y crear una cuenta para el servicio, el rol que se le dará es a nivel “Project” solo lectura. En mi caso, estoy corriendo el Python de forma local por lo que es necesario descargar el archivo con las llaves (.json)

Para poder utilizar este archivo al autenticarse con la API. Es necesario crear una variable de entorno que cargue este archivo

    export GOOGLE_APPLICATION_CREDENTIALS=~/key.json


#UPDATE
Encontré esto con respecto al pago:

``While many Google APIs can be used without fees, use of GCP (products & APIs) is not free. When enabling the Vision API (as described above), you may be asked for an active billing account. The Vision API's pricing information should be referenced by the user before enabling. Keep in mind that certain Google Cloud Platform (GCP) products feature an "Always Free" tier for which you have to exceed in order to incur billing. For the purposes of the codelab, each call to the Vision API counts against that free tier, and so long as you stay within its limits in aggregate (within each month), you should not incur any charges.``
``Some Google APIs, i.e., G Suite, has usage covered by a monthly subscription, so there's no direct billing for use of the Gmail, Google Drive, Calendar, Docs, Sheets, and Slides APIs, for example. Different Google products are billed differently, so be sure to reference your API's documentation for that information.``




    
