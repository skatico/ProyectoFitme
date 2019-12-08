var x;
x=$(document);  //objeto que recupera el contenido de un document
x.ready(inicializarEventos);  // ready: lee o invoca funcion principal

function inicializarEventos()
{
var x;
x=$("#titulo1"); //recuperamos selector
x.click(presionTitulo1) //a través del método click invocamos la función.

x=$("#titulo2");
x.click(presionTitulo2)

x=$("td");  //recuperamos el selector de la fila que queremos modificar
x.click(presionFila); //invocamo al metodo presionfila

x=$("#boton1");
x.click(cambiaColor);
}

//modificando elementos web en base a jquery

function presionTitulo1() //definición de la función, modificamos estilo
{
var x;
x=$("#titulo1");
x.css("color","#BA4A00");
x.css("font-family","Courier");
$("#titulo1").text("Pues claro que si bb ♥♥♥");
}

function presionTitulo2()
{
var x;
x=$("#titulo2");
x.css("color","#ffff00");
x.css("font-family","Arial");
$("#titulo2").text("Profe Viviana La Mejor 👌");
}

// aspecto de una fila de una tabla

function presionFila()
{
    var x;
    x=$(this); //Recuperamos la fila actual
    x.css("background-color","#D6EAF8");
}

function cambiaColor()
{
    var x;
    x=$(".resaltado");
    x.css("background-color","#0049FF");
}




