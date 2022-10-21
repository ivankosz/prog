var contador = 1;
var numero;
var acumulador = 0;
var usuario = 'ivan'
var clave = 1234;

var otroNombre = prompt ("Ingrese su usario", "Usuario");
var id = prompt("Ingrese su clave: ");

var idnumero = parseInt(id)

if (idnumero === clave && otroNombre === usuario){
    alert("Bienvenido usuario: " + usuario);
    document.writeln("Bienvenido usuario: " + usuario);
    console.log("Bienvenido usuario: " + usuario);
}else{
    alert("Usuario o Clave incorrecta");
    document.writeln("Usuario o Clave incorrecta");
    console.log("Usuario o Clave incorrecta");
}