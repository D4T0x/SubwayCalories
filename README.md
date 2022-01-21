# SubwayCalories
#  Diseño Sistema Inteligente

En este proyecto se va a construir un software basado en algoritmos de computación evolutiva.

La finalidad del software supone en base a una lista de ingredientes proporcionados mediante un documento de tipo texto, que se genere una combinación de alimentos para generar un plato en este caso un bocadillo (se implementa pensando en que se puedan cambiar los datos para otros ejemplos como puede ser una pizza u otros platos combinados), y este ofrezca la mejor combinación que se puede realizar teniendo en cuenta como función *fitness* las kilocalorías que debe tener como máximo el plato.

Para el proyecto, como se ha mencionado antes, se va a utilizar como *datasheet* datos proporcionados por la [web de Subway](https://www.subway.com/es-US/MenuNutrition/Menu/Product?ProductId=4261&MenuCategoryId=1) y [calculadora nutrición Subway](https://www.nutritionix.com/subway/nutrition-calculator). Se han recopilado manualmente de estos servicios web, y se han copiado a un fichero de tipo .txt, con el formato <nombre_alimento> : <kilocalorías> .

Su implantación se va a realizar en un código en Python, por su portabilidad y por mi gusto por adentrarme más en este lenguaje con tanto potencial. Se utiliza una interfaz gráfica que nos va a permitir interactuar con el software de una manera mas sencilla e intuitiva.

El menú utilizado es el de Subway España:

![Menu Subway España](![image](https://user-images.githubusercontent.com/75228166/150454390-accd282d-24cc-4a0f-8973-865c8dd5a8b5.png))

La combinación a realizar se compone de los pasos destacados en el menú:

- 4 Bases

- 13 Proteínas

- 3 Quesos

- 4 Extras

- 8 Vegetales

- 11 Salsas

- 5 topping

Lo que generaría las suficientes combinaciones para que una inteligencia artificial nos ayudara a realizar una selección de la mejor solución.e 
