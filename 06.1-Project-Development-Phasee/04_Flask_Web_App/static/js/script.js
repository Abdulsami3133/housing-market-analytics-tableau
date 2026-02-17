document.addEventListener("DOMContentLoaded", function () {

    console.log("Housing Dashboard Loaded Successfully");

    // Simple animation effect
    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        card.style.opacity = 0;
        card.style.transform = "translateY(20px)";

        setTimeout(() => {
            card.style.transition = "0.6s ease";
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }, 200 * index);
    });

    // Example interactive feature
    const header = document.querySelector("header");
    header.addEventListener("click", () => {
        alert("Housing Market Dashboard - Data Powered by Flask & Pandas");
    });
});
