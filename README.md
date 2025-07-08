# curso-hacking-etico-m5-leccion-5-actividad-1
Entrega módulo 5 lección 5: actividad 1 portafolio.

## Descripción
1. Usa Python y la librería BeautifulSoup junto con requests.​
2.​ Conéctate a una URL pública que contenga al menos un formulario (por ejemplo,
https://httpbin.org/forms/post).​
3. Extrae todos los formularios del DOM.​
4. Por cada formulario, muestra:​
   - El valor del atributo method (GET/POST)​
   - El valor del atributo action (ruta de envío)
   - Los nombres (name) y tipos (type) de todos los campos <input>.
5. Identifica y comenta qué formularios podrían ser críticos si no estuvieran validados

### Creación del ambiente
- Creación: `python3 -m venv .venv`
- Activación: `source .venv/bin/activate`
- Desactivación: `deactivate`

### Instalación de dependencias
`pip install -r requirements.txt`

### Ejecución
`python form-analyzer.py "[URL]"`

Salida
```
[Info] Quering 'https://some-web-site.com/link-to-form/'
[Info] User-Agent: Random-Generated-User-Agent

Form attributes:
- action: /contact-us/#wpcf7-f2069-p2071-o1
- method: post
- novalidate: novalidate
- Input attributes: 
-- type: hidden
-- name: _wpcf7
-- value: 2069
- Input attributes: 
-- type: hidden
-- name: _wpcf7_version
-- value: 5.1.4
- Input attributes: 
-- type: hidden
-- name: _wpcf7_locale
-- value: en_US
- Input attributes: 
-- type: hidden
-- name: _wpcf7_unit_tag
-- value: wpcf7-f2069-p2071-o1
- Input attributes: 
-- type: hidden
-- name: _wpcf7_container_post
-- value: 2071
- Input attributes: 
-- type: hidden
-- name: g-recaptcha-response
-- value: 
- Input attributes: 
-- type: text
-- name: your-name
-- value: 
- Input attributes: 
-- type: email
-- name: your-email
-- value: 
- Textarea attributes: 
-- name: your-message
- Input attributes: 
-- type: submit
-- value: Send
```
