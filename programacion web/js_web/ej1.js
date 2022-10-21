
var edad = prompt("INGRESE SU EDAD: ");
var edad_int = parseInt(edad);
if(edad_int>=18){
    alert ("ES MAYOR DE EDAD");
    document.writeln("ES MAYOR DE EDAD");
    console.log ("ES MAYOR DE EDAD");
}else{
    alert ("ACCESO DENEGADO. ES MENOR DE EDAD");
    document.writeln ("ACCESO DENEGADO. ES MENOR DE EDAD");
    console.log ("ACCESO DENEGADO. ES MENOR DE EDAD");
}