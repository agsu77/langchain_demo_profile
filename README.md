# langchain_demo_profile

Esta demo es construida siguiendo el curso [LangChain- Develop LLM powered applications with LangChain](https://www.udemy.com/course/langchain).

El objetivo de esta demo es poder conseguir un Summary de una persona partiendo desde su nombre, para esto lo primero que hacemos es consultar Tavily con un nombre, de este obtenemos una URL para Scrappear y con esa informacion alimentamos al modelo para que genere el summary.

Para ejecutar esta demo es necesario:
-
- Crear el archivo `.env`
```python
PROXYCURL_API_KEY=...
TAVILY_API_KEY=...
#Configuracion para Langchain
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=...
LANGCHAIN_PROJECT=DEMO-LINKEDIN
```

- Levantar OLLAMA localmente para interacturar con el modelo, en este caso el `LLAMA3.2`
- Generar una API Key en [TAVILY](https://app.tavily.com) : Esta plataforma recibe un nombre y nos devuelve una lista de perfiles de linkedin, puede ser usada para consultar otro tipos de perfiles tambien...
- Generar una API Key en [ProxyCurl](https://nubela.co/proxycurl) : Esta plataforma se encarga de screpear la URL de linkedIn.
- **[Optional]** Configurar LangSmith, logearse y generar la API Key para poder tener el trace la app.
