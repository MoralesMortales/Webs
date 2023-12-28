
// let nombrevariables = document.querySelector;

// const button = document.querySelector("button");

//  button.onclick = function () {
// //   let name = prompt("¿Cuál es tu nombre?");
// //   alert("¡Hola " + name + ", encantado de verte!");
// const miTitulo = document.querySelector("h1");
// miTitulo.textContent = "¡Hola mundo!";
// };

// let helado = "chocolate";
// if (helado === "chocolate") {
//   alert("¡Sí, amo el helado de chocolate!");
// } else {
//   alert("Awwww, pero mi favorito es el de chocolate...");
// }

// document.querySelector("p").onclick = function () {
//     alert("¡Ouch! ¡Deja de pincharme!");
//   };
  
// let miHTML = document.querySelector("html");
// miHTML.onclick = function () {
//     alert("¡Ouch! ¡Deja de pincharme!");
// };

let miImage = document.querySelector("img");
miImage.onclick = function () {
    
  let miSrc = miImage.getAttribute("src");
  if (miSrc === "rcs/12.png") {
      miImage.setAttribute("src", "rcs/24.png");
    } else {
      miImage.setAttribute("src", "rcs/12.png");
  }
};
