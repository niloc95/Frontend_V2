async function loadGtag() {
    const script = document.createElement('script');
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=G-3TRXL4Y5B5";
    document.head.appendChild(script);
  
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('js', new Date());
    gtag('config', 'G-3TRXL4Y5B5');
  }
  
  loadGtag();
