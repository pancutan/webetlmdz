# Propuesta de Web Estática para ETLMdz

Página web realizada con [Pelican](https://getpelican.com/).

## Despliegue

### Requisitos

La web se puede desplegar en Ubuntu trusty, pero puede también ser desarrollada en otros sistemas.

Se necesita virtualenv y otros paquetes (a adocumentar).

### Instalar pelican en virtualenv

	cd /directorio/favorito/
	mkdir webetlmdz
	virtualenv webetlmdz
	cd webetlmdz/
	source bin/activate
	pip install pelican Markdown

### Instalar este repositorio

	git clone --recursive https://github.com/etlmdz/webetlmdz.git #(este repositorio)
	cd webetlmdz/

### Generar la web estática

	make html

### Ver presentacion html

	make devserver
	sensible-browser http://localhost:8000.

Para detener el server web

	make stopserver

## Realizar cambios

El contenido del sitio está en el directorio `content/`. La configuración de
maquetado se ajusta en `pelicanconf.py`.

Los archivos de salida estarán en `output/` y no serán registrados por este repositorio.

## Más info

Ver http://docs.getpelican.com
