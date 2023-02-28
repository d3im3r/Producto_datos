![](https://medellin.unal.edu.co/templates/unal/images/escudoUnal_black.png)
# **Producto de Datos**
## **_Entrega #1_**

## Uso:

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

3. **Procesamiento**
* Para ejecutar la simulación de los datos y el procesamiento con días predeterminados (21 días) ejecute el siguiente código:
```sh
make -C ./Flujo processing 
```

* Para ejecutar la simulación de los datos y el procesamiento especificando lso días a procesar ejecute el siguiente código:
```sh
make -C ./Flujo processing n_days=##
```
> Nota: `##` Se reemplaza por los días a procesar.


## License

Free 

**Free Software, Hell Yeah!** 8-)__

[//]: # (Comentarios ocultos)

   [dill]: <https://github.com/joemccann/dillinger>
