  // Get the Navbar element
  const navbar = document.querySelector('nav');

  // Function to toggle the 'sticky' class
  function toggleSticky() {
      if (window.scrollY > 800) {
          navbar.classList.add('sticky');
      } else {
          navbar.classList.remove('sticky');
      }
  }

  // Listen for scroll events and call toggleSticky()
  window.addEventListener('scroll', toggleSticky);

  const navLinks = document.querySelectorAll('.nav-link');

    // Add a click event listener to each link
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Check if the mobile menu is open
            const mobileMenu = document.querySelector('.navbar-collapse.show');
            if (mobileMenu) {
                // If it's open, close the menu
                mobileMenu.classList.remove('show');
            }
        });
    });
