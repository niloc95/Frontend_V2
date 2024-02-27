document.addEventListener("DOMContentLoaded", function() {
    let revealElement = document.getElementById('reveal');

    window.addEventListener('scroll', revealOnScroll);

    function revealOnScroll() {
        let revealPosition = revealElement.getBoundingClientRect().top;
        let windowHeight = window.innerHeight;

        if (revealPosition < windowHeight / 1.5) {
            revealElement.classList.add('opacity-100', 'translate-y-0');
            window.removeEventListener('scroll', revealOnScroll);
        }
    }
});