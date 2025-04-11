from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Plan de Estudio: HTML, CSS y JavaScript (2 meses)", ln=True, align='C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", 'B', 12)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", '', 11)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

weeks = [
    {
        "title": "Semana 1 – HTML, estructura y semántica + fundamentos CSS",
        "body": """Objetivo: Dominio completo de etiquetas, estructura y estilo básico

Lunes: Revisión de etiquetas HTML5 semánticas (header, main, article, section, footer). Crea una estructura básica.
Martes: CSS Selectores, propiedades básicas, colores, unidades (px, em, %). Hoja de estilo externa.
Miércoles: Maquetación con display, inline, posicionamiento.
Jueves: Mini-proyecto 1 – Página personal: info, hobbies y contacto.
Viernes: Buenas prácticas HTML + metaetiquetas (viewport, description, Open Graph).
Sábado: Subir proyecto a GitHub con README.

Recursos:
- https://www.freecodecamp.org/
- https://developer.mozilla.org/es/docs/Web/HTML"""
    },
    {
        "title": "Semana 2 – CSS avanzado: Flexbox, Grid, Media Queries",
        "body": """Objetivo: Dominar diseño adaptable

Lunes: Flexbox (justify-content, align-items, gap, order).
Martes: CSS Grid (grid-template, fr, repeat, auto-fit, gap).
Miércoles: Media Queries + diseño responsivo.
Jueves: Mini-proyecto 2 – Landing page responsiva con 3 secciones.
Viernes: Revisión con DevTools (modo móvil, accesibilidad).
Sábado: Subir a GitHub, código limpio y documentado.

Recursos:
- https://flexboxfroggy.com/
- https://cssgridgarden.com/
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/"""
    },
    {
        "title": "Semana 3 – JavaScript: Fundamentos",
        "body": """Objetivo: Comprender variables, funciones, condicionales y eventos

Lunes: let, const, var, tipos de datos, operadores.
Martes: Condicionales, bucles, funciones.
Miércoles: DOM – getElementById, querySelector, eventos.
Jueves: Mini-proyecto 3 – Menú hamburguesa + dark mode toggle.
Viernes: Validación básica de formularios con JS.
Sábado: Subir proyecto a GitHub.

Recursos:
- https://javascript.info/
- https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"""
    },
    {
        "title": "Semana 4 – JavaScript intermedio: Arreglos, objetos, eventos",
        "body": """Objetivo: Manipular datos y mejorar interactividad

Lunes: Arrays – map, filter, forEach, push, splice.
Martes: Objetos y desestructuración.
Miércoles: Eventos – click, input, keydown.
Jueves: Mini-proyecto 4 – Galería de imágenes con filtrado dinámico.
Viernes: Uso de localStorage y JSON básico.
Sábado: Subir a GitHub + revisión final."""
    }
]

for week in weeks:
    pdf.chapter_title(week["title"])
    pdf.chapter_body(week["body"])

pdf.output("Plan_HTML_CSS_JS_2_meses.pdf")
