<p align="center">
  <img src="https://minas.medellin.unal.edu.co/images/noticias/logoUN.gif">
</p>

# **Producto de Datos**
## **_Entrega #1_**

## Uso: <br>

1. **Clone el repositorio a su carpeta de trabajo**
1. **Estando en la carpeta de trabajo abra un terminal de comandos o shell**
1. **Simulación:**
* Para ejecutar la simulación con días predeterminados (21 días) ejecute el siguiente código:

```sh
make -C ./Flujo simulation
```
* Para ejecutar la simulación especificando los días a procesar ejecute el siguiente código:

```sh
make -C ./Flujo simulation n_days=##
```
> Nota: `##` Se reemplaza por los días a procesar.

4. **Procesamiento**
* Para ejecutar la simulación de los datos y el procesamiento con días predeterminados (21 días) ejecute el siguiente código:
```sh
make -C ./Flujo processing 
```

* Para ejecutar la simulación de los datos y el procesamiento especificando los días a procesar ejecute el siguiente código:
```sh
make -C ./Flujo processing n_days=##
```
> Nota: `##` Se reemplaza por los días a procesar.

5. **Reinicio**
* Para reiniciar el entorno de archivos de procesamiento o simulación ejecute el siguiente código:
```sh
make -C ./Flujo reset
```
> Nota: Elimina el contenido de la ruta: `/Data/Preprocessing`

## **License**

**Free Software, Hell Yeah!**

[//]: # (Comentarios ocultos)


   [dill]: <br>

