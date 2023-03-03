<p align="center">
  <img src="https://minas.medellin.unal.edu.co/images/noticias/logoUN.gif">
</p>

# **Producto de Datos**
## **_Entrega #1_**

## Uso: <br>

1. **Clone el repositorio a su carpeta de trabajo**
1. **Estando en la carpeta de trabajo abra un terminal de comandos o shell**
1. **Simulación:**
* Para ejecutar la simulación con una fecha predeterminada (2015-08-01) ejecute el siguiente código:

```sh
make -C ./Flujo simulation
```
* Para ejecutar la simulación especificando la fecha ejecute el siguiente código:

```sh
make -C ./Flujo simulation deadline={fecha:YYYY-MM-DD}
```
> Nota: `YYYY-MM-DD` debe estar entre el 1 de julio de 2015 y el 31 de agosto de 2017.

4. **Procesamiento**
* Para ejecutar la simulación de los datos y el procesamiento con fecha predeterminada (2015-08-01) ejecute el siguiente código:
```sh
make -C ./Flujo processing 
```

* Para ejecutar la simulación de los datos y el procesamiento especificando  la fecha a procesar ejecute el siguiente código:
```sh
make -C ./Flujo processing deadline={fecha:YYYY-MM-DD}
```
> Nota: `YYYY-MM-DD` debe estar entre el 1 de julio de 2015 y el 31 de agosto de 2017.

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

