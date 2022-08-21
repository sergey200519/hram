// function substringSearch(s, sear) {
//   const n = s.length
//   let nsear = sear.length
//   let i = 0
//   while (i + nsear <= n) {
//     if (s[i] == sear[0]) {
//       let time = 0
//       let j = 0
//       while (j < nsear) {
//         if (s[i] == sear[j]) {
//           time++
//         }
//         i++
//         j++
//       }
//       if (time == nsear) {
//         return true
//       }
//     }
//     i++
//   }
//   return false
// }
//
// let href = window.location.href
// function funTheme() {
//   let time = new Date();
//   console.log(time.getHours());
//   let theme = document.querySelector(".theme");
//   if (!substringSearch(href, "pages/")) {
//     if (time.getHours() <= "8" && time.getHours() <= "20") {
//       console.log("if");
//       theme.href = "style/dark-style.css";
//     } else {
//       console.log("else");
//       theme.href = "style/style.css";
//     }
//   } else {
//     if (time.getHours() <= "8" && time.getHours() <= "20") {
//       console.log("if");
//       theme.href = "../style/dark-style.css";
//     } else {
//       console.log("else");
//       theme.href = "../style/style.css";
//     }
//   }
// }
// funTheme()
// setInterval(funTheme, 60 * 1000)
//




// window.location.href
//
//
// setInterval(function() {
//   ......
// }, 5 * 60 * 1000)
// let time = new Date();
// console.log(time.getHours());
// let theme = document.getElementById("theme");
// let old = document.getElementById("old");
// if (time.getHours() < 10 || true) {
//   console.log("link");
//   window.location.href
//   theme.href = "/style/dark-style.css";
//
//
//  let theme = document.querySelector("#theme");






// * {
//   transition: 0s all;
// }
// :root {
//   --conteiner-background: #67646a;
//   --background-img: url(../img/dark-bac.jpg);
//   --main-color-for-text: white;
//   --header_section-color: #00abff;
// }
//
// html * {
//     transition: inherit;
// }
//
// js white dark
// let html =
// html.style.transition = 'all 5s'
//
// k index.html style => ... pages => ... js
//
// setInterval(function() {
//   ......
// }, 5 * 60 * 1000)
// let time = new Date();
// console.log(time.getHours());
// let theme = document.querySelector("#theme > div");
// let old = document.getElementById("old");
// html {
//     --xxx: white;
// }
// html.dark {
//     --xxx: black;
// }
//
// @media (prefers-color-scheme: dark) {
//   .day.dark-scheme   { background:  #333; color: white; }
//   .night.dark-scheme { background: black; color:  #ddd; }
// }
//
// let html = document.querySelector('html')
// html.classList.add('dark')
// if (time.getHours() < 10 || true) {
//   console.log("link");
//   window.location.href
//   theme.href = "/style/dark-style.css";
// } else {
//   theme.href = "";
// }
