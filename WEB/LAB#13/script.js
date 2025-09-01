// Loader Screen Timeout
window.onload = function() {
    setTimeout(function() {
        document.getElementById("loader").style.display = "none";
    }, 2000); // Hide loader after 2 seconds
};

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
