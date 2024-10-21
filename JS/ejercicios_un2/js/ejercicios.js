// 1. Realizar una función, a la que se le pase como parámetro un número N, y muestre por consola N veces, el siguiente mensaje: “Bienvenidos al curso Full Stack”
let nro = prompt("Ingresá un número:");
mostrarMsj(nro);

function mostrarMsj(n){
    for(let i=1; i<=n; i++){
        console.log("Bienvenidos al curso Full Stack");
    }
}

// 29. escriba una función de JavaScript que busque la palabra más larga de una frase. 
//Por ejemplo, si x = "Tutorial de desarrollo web", el resultado debería ser "Desarrollo"
let frase = prompt("Ingresá una frase:");
let palabras = frase.split(' ');

function busquedaPalabraLarga(palabras){
    let palabraLarga = ' ';

    for (let palabra of palabras) {
        if (palabra.length > palabraLarga.length) {
            palabraLarga = palabra;
        }
    }
    return palabraLarga;
}
document.write("La palabra más larga de la frase es: ", busquedaPalabraLarga(palabras));
console.log(palabras);

// 28.  escriba una función de JavaScript que convierta la primera letra de cada palabra a mayúsculas. Por ejemplo, si x = "prince of persia", la salida debería ser "Prince Of Persia".
function tipoTitulo(palabras){
    for (const palabra of palabras) {
        palabra.laprimerletra
    }
}
document.write("<br>Tuneada Tipo Título: ", tipoTitulo(palabras));