document.addEventListener("DOMContentLoaded", function() {
    const cookieNotice = document.getElementById('cookie-notice');
    const acceptCookiesBtn = document.getElementById('accept-cookies');

    acceptCookiesBtn.addEventListener('click', function() {
        cookieNotice.style.display = 'none';
        // Set a cookie to remember user's choice
        document.cookie = 'cookies_accepted=true; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/';
    });

    // Check if the user has already accepted cookies
    const cookiesAccepted = document.cookie.split(';').some((item) => item.trim().startsWith('cookies_accepted='));
    if (cookiesAccepted) {
        cookieNotice.style.display = 'none';
    }
});