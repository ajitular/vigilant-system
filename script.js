// Highlight Text
var highlight = document.getElementById("highlight");

highlight.addEventListener("click", function() {
this.classList.toggle("highlight");
});

// Smooth Scroll
var links = document.querySelectorAll("nav ul li a");

for (var i = 0; i < links.length; i++) {
links[i].addEventListener("click", function(event) {
event.preventDefault();
var target = this.getAttribute("href");
var targetElement = document.querySelector(target);
var targetPosition = targetElement.offsetTop;

window.scrollTo({
    top: targetPosition,
    behavior: "smooth"
});
});
}