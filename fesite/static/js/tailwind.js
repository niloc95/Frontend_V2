document.getElementById('menu-toggle').addEventListener('click', function () {
    document.getElementById('mobile-menu').classList.toggle('hidden');
});

// Close mobile menu
document.getElementById('close-menu').addEventListener('click', function () {
    document.getElementById('mobile-menu').classList.add('hidden');
});

window.addEventListener('scroll', function () {
    var navbar = document.getElementById('navbar');

    if (window.scrollY > 0) {
        navbar.classList.add('fixed', 'top-0', 'w-full');
    } else {
        navbar.classList.remove('fixed', 'top-0', 'w-full');
    }
});