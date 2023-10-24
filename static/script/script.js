const mobileMenu = document.querySelector(".mobile-menu");
mobileMenu.addEventListener("click", () => {
    document.querySelector(".menu").classList.toggle("show");
});

setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);
