from fpdf import FPDF

# Crear una instancia de FPDF
pdf = FPDF()
pdf.add_page()

# Agregar una fuente que soporte UTF-8 (DejaVu Sans)
# La fuente se debe tener en el directorio de las fuentes de Windows, por ejemplo:
pdf.add_font('DejaVu', '', 'C:/Users/Bertis/Desktop/dejavu-sans/DejaVuSans.ttf', uni=True)  # Asegúrate de que el path sea correcto
pdf.set_font('DejaVu', '', 12)

# Añadir título
pdf.cell(0, 10, "Plan Intensivo: HTML, CSS, JavaScript, APIs y React (2 meses)", ln=True, align="C")

# Secciones con contenido
sections = [
    {
        "title": "Objetivo General",
        "content": """Crear una página web completa, limpia, responsive e interactiva aplicando buenas prácticas de HTML, CSS y JavaScript.
Subir todos los avances a GitHub. Aprender a consumir APIs y cómo trabajar con React para crear aplicaciones frontend dinámicas.
Este plan te prepara para un rol como frontend developer o junior JavaScript developer."""
    },
    {
        "title": "Horario Diario (Lunes a Sábado – 12:00pm a 5:00pm)",
        "content": """De lunes a sábado:
12:00 - 12:50  Teoría del día (video, lectura)
12:50 - 01:00  Pausa corta
01:00 - 02:30  Práctica guiada (ejercicios, código)
02:30 - 03:30  Mini proyecto del día
03:30 - 03:50  Pausa
03:50 - 05:00  Refuerzo / ejercicios extra / repaso"""
    },
    {
        "title": "Mes 1: HTML, CSS y JavaScript",
        "content": """Semana 1 – HTML + CSS + Estructura básica:
Lunes: HTML semántico, metadatos, OG y Twitter Cards.
Martes: CSS básico (Box Model, Selectores, Tipografías).
Miércoles: Flexbox, Grid y Media Queries.
Jueves: Accesibilidad básica + SEO.
Viernes: Proyecto: Página personal (subir a GitHub).

Semana 2 – Formularios + Tablas + Responsive:
Lunes: Formularios HTML + validación.
Martes: Tablas y su estilización con CSS.
Miércoles: Responsive design (usando Flexbox, Grid y Media Queries).
Jueves: Animaciones CSS y transiciones.
Viernes: Proyecto: Formulario y tabla responsiva (subir a GitHub).

Semana 3 – JavaScript Básico + DOM:
Lunes: Variables, operadores, funciones y tipos de datos.
Martes: Condicionales, ciclos y arrays.
Miércoles: Manipulación del DOM (selectores, eventos).
Jueves: Uso de clases dinámicas, localStorage.
Viernes: Proyecto de JavaScript: "To-Do List" o "Adivina el número" (subir a GitHub).

Semana 4 – Proyecto Final:
Crear un **portfolio básico** con HTML, CSS y JavaScript:
- Secciones de presentación.
- Galería de proyectos.
- Formulario de contacto.
- Responsive para móvil, tablet y desktop.
Subir a GitHub y hacer una revisión para mejorar la accesibilidad y SEO."""
    },
    {
        "title": "Mes 2: APIs y React",
        "content": """Semana 5 – APIs en JavaScript:
Lunes: Introducción a APIs.
Martes: Uso de **Fetch API** para obtener datos.
Miércoles: Manejo de respuestas JSON y errores.
Jueves: Peticiones POST (enviar datos a un servidor).
Viernes: Proyecto: Conectar una API externa (ej. OpenWeather, JSONPlaceholder) y mostrar datos.

Semana 6 – Proyecto Intermedio con APIs:
Proyecto de **clima** o **noticias** usando APIs externas.
Consumo de datos, manejo de errores y carga de contenido dinámico.
Subir a GitHub y revisar buenas prácticas.

Semana 7 – Introducción a React:
Lunes: Instalación de React, JSX y componentes.
Martes: Props y State en React.
Miércoles: Uso de **useState** y **useEffect** en React.
Jueves: Conexión de React con una API externa.
Viernes: Proyecto: "Todo App" en React (subir a GitHub).

Semana 8 – Proyecto Final en React:
Crear un **portfolio interactivo** con React:
- Mostrar datos desde una API.
- Componentes dinámicos y manejo de estado.
Subir a GitHub."""
    },
    {
        "title": "Meta Final",
        "content": """- Tener un **portfolio profesional** con:
  - Sección de presentación y habilidades.
  - Galería de proyectos con enlaces a tu código.
  - Formulario de contacto.
  - Blog o proyectos dinámicos con APIs.
  - Diseño responsive.
  - **React** para manejar el estado y componentes dinámicos.
  
  - Publicar tu portfolio en Netlify y subir todo el código a GitHub."""
    },
    {
        "title": "Próximo Mes (Backend)",
        "content": """El siguiente mes puedes comenzar a aprender sobre backend con **Python y C#** para complementar tu formación como full-stack developer.
Recursos para aprender:
- **Python**: Django/Flask.
- **C#**: .NET Core.

Dedica entre 2 y 3 horas al día para repasar bases de datos y trabajar con tecnologías de backend después de finalizar estos dos meses de frontend."""
    }
]

# Crear el PDF
for section in sections:
    pdf.set_font("DejaVu", '', 14)
    pdf.ln(10)
    pdf.cell(0, 10, section["title"], ln=True)
    pdf.set_font("DejaVu", '', 12)
    pdf.multi_cell(0, 10, section["content"])

# Guardar el PDF
pdf_output_path = "Plan_2_Meses_HTML_CSS_JS_APIs_React.pdf"
pdf.output(pdf_output_path)

print("PDF generado correctamente.")
