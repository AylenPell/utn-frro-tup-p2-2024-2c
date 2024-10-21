// 1. programa de una sola línea: alert que diga “Hello World”
alert("Hello Mundo!");
// 2. programa de una sola línea: escriba en la pantalla un texto que diga “Hello World” (document.write)
document.write("Hello Mundo!");
// 3. programa de una sola línea: escriba en la pantalla el resultado de sumar 3 + 5.
document.write("<br>El resultado de la suma entre 3 y 5 es: ", 3 + 5);
// 4. dos lineas: que pida el nombre del usuario con un prompt y escriba un texto que diga “Hola nombreUsuario”
var nombre = prompt("Ingresa tu nombre", " ");
document.write("<br>Hello " + nombre + "! How are you?");
// 5. tres líneas que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
var num1 = parseInt(prompt("Ingresa un número:", " "));
var num2 = parseInt(prompt("Ingresa otro número:", " "));
document.write("<br>La suma de los números ingresados es: ", num1 + num2);
// 6. Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor
if (num1 > num2) {
    document.write("<br>El primer número ingresado (", num1, ") es mayor al segundo (", num2, ")");
    num_ganador = num1;
} else {
    document.write("<br>El segundo número ingresado (", num2, ") es mayor al primero (", num1, ")");
    num_ganador = num2;
}
// 7. Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
var num3 = parseInt(prompt("Ingresa un tercer número:", " "));
if (num3 > num_ganador) {
    document.write("<br>El tercer número es el más grande de todos");
} else {
    document.write("<br>El más grande es ", num_ganador);
}
// 8. Escribe un programa que pida un número y diga si es divisible por 2
// VER ABAJO CON EL 13
// 9. Escribe un programa que pida una frase y escriba cuantas veces aparece la letra a
var frase = prompt("Decime una frase:");
document.write("<br>La frase '<span class=\"fr_style\">", frase);
frase = frase.toLowerCase();
// 10. Escribe un programa que pida una frase y escriba las vocales que aparecen
// 11. Escribe un programa que pida una frase y escriba cuántas de las letras que tiene son vocales
// 12. Escribe un programa que pida una frase y escriba cuántas veces aparecen cada una de las vocales
cont_a = 0;
cont_e = 0;
cont_i = 0;
cont_o = 0;
cont_u = 0;
for (var i = 0; i < frase.length; i++) {
    if (frase[i] == "a"){
        cont_a++;
    } else if (frase[i] == "e"){
        cont_e++;
    } else if (frase[i] == "i"){
        cont_i++;
    } else if (frase[i] == "o"){
        cont_o++;
    } else if (frase[i] == "u"){
        cont_u++;
    }
}
cant_vocales = cont_a + cont_e + cont_i + cont_o + cont_u;
document.write("</span>' tiene ", cont_a, " letras 'a'");
document.write("<br>Tiene ", cant_vocales, " vocales: ", cont_e, " letras e, ", cont_i, " letras i, ", cont_o, " letras o y ", cont_u, " letras u.");
// 13. Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
// 14. Añadir al ejercicio anterior que nos diga por cual de los cuatro es divisible (hay que decir todos por los que es divisible)
document.write("<br>El número ", num3, "...");
if(num3 % 2 == 0){
    document.write("<br>- Es divisible por 2.");
}else{
    document.write("<br>- NO es divisible por 2.");
}
for (let i = 3; i < 8; i = i + 2) {
    if(num3 % i == 0){
        document.write("<br>- Es divisible por ", i);
    } else {
        document.write("<br>- NO es divisible por ", i);
    }  
}