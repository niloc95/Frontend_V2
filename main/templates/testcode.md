<link rel="stylesheet" type="text/css" href="{% static '/css/logo.css' %}"/>
<link rel="stylesheet" type="text/css" href="{% static '/css/nav.css' %}"/>
<link rel="stylesheet" type="text/css" href="{% static '/css/styles.css' %}"/>
<nav class="navbar navbar-expand-md navbar-dark fixed-top">
  <div class="container-fluid heading-padding">
      <a class="navbar-brand" href="{% url 'home' %}"><span class="logo-type">frontend </span><span class="icon-fav">Fe.<span><span class="logo-type-sub-type br"> Software Engineering</span></a>
      <button class="navbar-toggler shadow-none border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="mx-auto"></div>
        <ul class="navbar-nav">
          <li class="nav-item">
            {% comment %} <a class="nav-link active" aria-current="page" href="{% url 'bookings' %}">Bookings</a> {% endcomment %}
          </li>
          <li class="nav-item">
            <a class="nav-link navlinks-type navlinks-hover" href="{% url 'about' %}#career">Work Experience</a>
          </li>
          <li class="nav-item">
            <a class="nav-link navlinks-type navlinks-hover" href="{% url 'home' %}#my_projects">Professional Services</a>
          </li>
          <li class="nav-item">
            <a class="nav-link navlinks-type navlinks-hover" href="{% url 'home' %}#my_projects">Insights</a>
          </li>
          <li class="nav-item">
            <a class="nav-link navlinks-type navlinks-hover" href="{% url 'about' %}">About</a>
          </li>
          <li class="nav-item">
            {% comment %} <a class="nav-link" href="{% url 'contact' %}">Contact</a> {% endcomment %}
          </li>
          {% comment %} <li class="nav-item">
            <a class="nav-link" href="{% url 'blog' %}">Blog</a>
          </li> {% endcomment %}
          {% comment %} <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li> {% endcomment %}
          {% comment %} <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>{% endcomment %}
        </ul> 
        {% comment %} <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form> {% endcomment %}
      </div>
    </div>
  </nav>


  <!-- <section id="hero-section" class="hero-nilo">
  
  <video autoplay loop muted playsinline><source src="{% static 'images/Landing_page.mp4' %}"></video>
  <div class="container-fluid hero-text-home">
    <h1 class="headings-h1">{{home_hero_h1}}<span> 👋</span></h1>
    <p class="sub-heading_p700">{{home_hero_p}}</p><p class='sub-heading-p'> {{home_hero_p2}} </p>
    {% comment %} <a href="{% url 'send_email' %}"> {% endcomment %}
      <a href="{% url 'contact' %}">
        <button class="btn btn-outline-light btn-lg">Contact</button>
      </a>
  </div>
  <div class="bottom-right-text">
    <p class="sub-heading-p">Engineered with Django and Bootstrap <a href="https://github.com/niloc95/Frontend" target="blank" alt="Nilo Cara - Software Engineer"><i class="bi bi-github"></i></a></p>
  </div>
</section> -->
{% comment %}<!-- End Hero Section -->{% endcomment %}




<section id="aboutme">
  <div class="container-fluid">
    <div class="align-items-center justify-content-center d-md-flex">
      <div>
        <h2 class="headings-h1" style="color: black;">Me</h2>
        <p class="paragragh-text">{{Section2_P1}}</p>
        {% comment %} <p class="paragragh-text">Being a web developer, I find immense satisfaction in harnessing my meticulous attention to detail, unwavering passion for creation, and a resolute commitment to my mission to actively contribute to global transformation. This is precisely why I am eagerly looking forward to making a substantial mark within a rapidly expanding organization.</p> {% endcomment %}
        <div>
          <p class="paragragh-text"><strong>Current Focus:</strong> Python || Django || Frontend Engineering || Frontend Libraries</p>
        </div>
      </div>
      <img class="img-fluid pb-5" src="{% static 'images/400x400_NO_BG.png'%}"  alt="" />
    </div>
  </div>
  {% comment %} <!-- Anchor point for Accordion section--> {% endcomment %}
  <div id="career"></div>
  {% comment %} <!-- End Anchor point for Accordion section--> {% endcomment %}
</section>



{% comment %} <!-- Start FAQ Section Accordion --> {% endcomment %}
<section id="my_projects" class="section-padding">
    <div class="container">
      <h2 class="text-dark">Experience</h2>
      <div class="accordion accordion-flush">
        <!-- Item 1 -->
        <div class="accordion-item border-0 ">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed "
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-one"
            >
            <span class="lead">Software Engineering</span>
            </button>
          </h2>
          <div
            id="question-one"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body lead">
                <strong>A</strong> For our Accelerated and Part Time Program, we offer a flexible payment installment plan that does not require credit approval or interest. We require a deposit and will automatically deduct monthly payments each month until you are paid in full. The payment plan does include a R5000.00 maintenance fee. Us today to get started setting up your flexible payment plan.
            </div>
              <img src="{% static 'images/Fe-logo-black.png'%}" class="img-fluid" alt="" />
          </div>
        </div>
        <!-- Item 2 -->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-two"
            >
            <span class="lead">Web Development</span>
            </button>
          </h2>
          <div
            id="question-two"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
                <strong>A.</strong> No, we do not. All Intro classes and private lessons must be paid in full at the time of registration.
            </div>
          </div>
        </div>
        
        {% comment %}<!-- Item 3 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-three"
            >
              <span class="lead">Project Management</span>
            </button>
          </h2>
          <div
            id="question-three"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}
        
        {% comment %}<!-- Item 4 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-four"
            >
              <span class="lead">Bettaway - August 2021 // Bryanston, South Africa</span>
            </button>
          </h2>
          <div
            id="question-four"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}

        {% comment %}<!-- Item 5 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-five"
            >
              <span class="lead">VitaForce - September 2021 // Bryanston, South Africa</span>
            </button>
          </h2>
          <div
            id="question-five"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}

        {% comment %}<!-- Item 6 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-six"
            >
              <span class="lead">Studio Merkmann - May 2022 // Johannesburg, South Africa</span>
            </button>
          </h2>
          <div
            id="question-six"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}

        {% comment %}<!-- Item 7 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-seven"
            >
              <span class="lead">StanLib - April 2020 // Melrose Arch, South Africa</span>
            </button>
          </h2>
          <div
            id="question-seven"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}

        {% comment %}<!-- Item 8 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-eight"
            >
              <span class="lead">Chavda International - April 2020 // Sandton, South Africa</span>
            </button>
          </h2>
          <div
            id="question-eight"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}

        {% comment %}<!-- Item 9 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-nine"
            >
              <span class="lead">Suitable Inspired Living - April 2017 // Sandton, South Africa</span>
            </button>
          </h2>
          <div
            id="question-nine"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}

        {% comment %}<!-- Item 10 -->{% endcomment %}
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-ten"
            >
              <span class="lead">about.frontend.co.za - April 2021 // Johannesburg, South Africa</span>
            </button>
          </h2>
          <div
            id="question-ten"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        {% comment %}<!-- End Item-->{% endcomment %}

        <!-- Item 11 -->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-eleven"
            >
              <span class="lead">WebScheduler - November 2019 // Johannesburg, South Africa</span>
            </button>
          </h2>
          <div
            id="question-eleven"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
        <!-- Item 12 -->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#question-twelve"
            >
              <span class="lead">Washington County - March 2020 // Maryland, USA</span>
            </button>
          </h2>
          <div
            id="question-twelve"
            class="accordion-collapse collapse"
            data-bs-parent="#questions"
          >
            <div class="accordion-body">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam
              beatae fuga animi distinctio perspiciatis adipisci velit maiores
              totam tempora accusamus modi explicabo accusantium consequatur,
              praesentium rem quisquam molestias at quos vero. Officiis ad
              velit doloremque at. Dignissimos praesentium necessitatibus
              natus corrupti cum consequatur aliquam! Minima molestias iure
              quam distinctio velit.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
{% comment %} <!-- End FAQ--> {% endcomment %}
{% comment %}<!-- Call to action Section --> 
 <section class="bg-primary text-light p-5">
    <div class="container">
        <div class="d-md-flex justify-content-between align-content-center">
            <h3 class=" mb-3 mb-md-0">Get the latest Gigs</h3>
            <div class="input-group mb-3 news-input">
                <input type="text" class="form-control" placeholder="Your email please ">
                <button class="btn btn-dark btn-lg" type="button">Submit</button>
            </div>
        </div>
    </div>
</section> 
<!-- End Call to action Section -->{% endcomment %}

{% comment %}<!-- Boxes -->
 <section class="p-5">
    <div class="container">
        <div class="row text-center">
            <div class="col-md">
                <div class="card bg-dark text-light">
                  <div class="card-body text-center">
                    <div class="h1 mb-3">
                      <i class="bi bi-calendar4-event"></i>
                    </div>
                    <h3 class="card-title mb-3">Live Gigs</h3>
                    <p class="card-text">
                        The revolutionary way of booking live entertainment for events!
                    </p>
                    <a href="#" class="btn btn-primary">More News</a>
                  </div>
                </div>
              </div> 
            <div class="col-md">
                <div class="card bg-secondary text-light">
                    <div class="card-body text-center">
                      <div class="h1 mb-3">
                        <i class="bi bi-emoji-laughing"></i>
                      </div>
                      <h3 class="card-title mb-3">Virtual DJ</h3>
                      <p class="card-text">
                        Real time, live stream DJ's <span class="text-warning">Online</span>
                      </p>
                      <a href="#" class="btn btn-dark">Enquire Now</a>
                    </div>
                  </div>
            </div>
              
            <div class="col-md">
                <div class="card bg-dark text-light">
                    <div class="card-body text-center">
                      <div class="h1 mb-3">
                        <i class="bi bi-journal-check"></i>
                      </div>
                      <h3 class="card-title mb-3">Hire Us</h3>
                      <p class="card-text">
                        SA's best musicians, superstars, DJ's, comedians, celebrities.
                      </p>
                      <a href="#" class="btn btn-primary">Book Now</a>
                    </div>
                  </div>
            </div>

        </div>
    </div>
</section> 
<!-- End Boxes -->{% endcomment %}

{% comment %} <!-- Learn More Section --> {% endcomment %}
<section id="learn-1" class="py-5">
    <div class="container">
      <div class="row align-items-center justify-content-between">
        <div class="col-md">
          <img src="{% static '/images/Fe-logo-black.png'%}" class="img-fluid" alt="" />
        </div>
        <div class="col-md p-lg-0">
          <h2>My Experience </h2>
          <p class="lead p-lg-0">
            With over 15 years of experience in the technology industry, I began as a junior support analyst at Standard Bank Group and progressed to become a Group Operations Manager. However, in November of 2017, I opted to take a hiatus from my professional career to undertake a personal project.
            Upon completing my personal project, I re-entered the market in 2019 as a freelance software developer. 
            <br />My extensive experience and expertise with 
            Python, Javascript, HTML, CSS, MySQL, AWS, and I am constantly exploring and learning new frameworks and languages. This has led me to be a well-rounded front-end developer utilizing JavaScript and various web development tools, with occasional forays into backend solutions using Node or Python.
            To further advance my career as a software engineer, I have recently joined Hyperion Dev with Stellenbosch University and Harvard University's CS50.
          </p>
          
          {% comment %} <a href="#" class="btn btn-light mt-3">
            <i class="bi bi-chevron-right"></i> Read More
          </a> {% endcomment %}
        </div>
      </div>
    </div>
  </section>

  <section id="learn-2" class=" py-5 bg-dark text-light ">
    <div class="container">
      <div class="row align-items-center justify-content-between">
        <div class="col-md p-lg-0">
          <h2>ST: </h2>
          <p class="lead p-lg-0">
            As a frontend software lead, I have a lot of experience in creating websites and web
            applications using different programming languages and tools such as HTML, PHP, CSS,
            MySQL, JavaScript, and Python.
            I am also well-versed in using page builders like Elementor and Oxygen Build, Visual
            Composer, and plugins like ACF, Meta Box, and Crocoblock to create websites efficiently.
            In addition, I have knowledge of hosting services such as AWS LightSail, EC2 and S3 buckets,
            LightSail DNS and AWS Route 53, hosted zone, Domains, AWS Workmail, Plesk, and Cpanel. I
            am also familiar with cloud platforms like Google Cloud Platform and Microsoft AZURE, as
            well as Office365 and Office 365 Admin.
            I have a strong understanding of design and design systems, and I am proficient in using
            design tools like AdobeXd, Figma, Sketch, Photoshop, and Illustrator.
          </p>
          
          <a href="#" class="btn btn-light mt-3">
            <i class="bi bi-chevron-right"></i> Read More
          </a>
        </div>
        <div class="col-md">
          <img src="" class="img-fluid" alt="" />
        </div>
      </div>
    </div>
  </section>
{% comment %} <!-- End Learn More Section --> {% endcomment %}



{% comment %} <section id="instructors" class="p-5 bg-primary">
    <div class="container">
      <h2 class="text-center text-white">Our Instructors</h2>
      <p class="lead text-center text-white mb-5">
        Our instructors all have 5+ years working as a web developer in the
        industry
      </p>
      <div class="row g-4">
        <div class="col-md-6 col-lg-3">
          <div class="card bg-light">
            <div class="card-body text-center">
              <img
                src="https://randomuser.me/api/portraits/men/11.jpg"
                class="rounded-circle mb-3"
                alt=""
              />
              <h3 class="card-title mb-3">John Doe</h3>
              <p class="card-text">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Assumenda accusamus nobis sed cupiditate iusto? Quibusdam.
              </p>
              <a href="#"><i class="bi bi-twitter text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-facebook text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-linkedin text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-instagram text-dark mx-1"></i></a>
            </div>
          </div>
        </div>

        <div class="col-md-6 col-lg-3">
          <div class="card bg-light">
            <div class="card-body text-center">
              <img
                src="https://randomuser.me/api/portraits/women/11.jpg"
                class="rounded-circle mb-3"
                alt=""
              />
              <h3 class="card-title mb-3">Jane Doe</h3>
              <p class="card-text">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Assumenda accusamus nobis sed cupiditate iusto? Quibusdam.
              </p>
              <a href="#"><i class="bi bi-twitter text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-facebook text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-linkedin text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-instagram text-dark mx-1"></i></a>
            </div>
          </div>
        </div>

        <div class="col-md-6 col-lg-3">
          <div class="card bg-light">
            <div class="card-body text-center">
              <img
                src="https://randomuser.me/api/portraits/men/12.jpg"
                class="rounded-circle mb-3"
                alt=""
              />
              <h3 class="card-title mb-3">Steve Smith</h3>
              <p class="card-text">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Assumenda accusamus nobis sed cupiditate iusto? Quibusdam.
              </p>
              <a href="#"><i class="bi bi-twitter text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-facebook text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-linkedin text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-instagram text-dark mx-1"></i></a>
            </div>
          </div>
        </div>

        <div class="col-md-6 col-lg-3">
          <div class="card bg-light">
            <div class="card-body text-center">
              <img
                src="https://randomuser.me/api/portraits/women/12.jpg"
                class="rounded-circle mb-3"
                alt=""
              />
              <h3 class="card-title mb-3">Sara Smith</h3>
              <p class="card-text">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Assumenda accusamus nobis sed cupiditate iusto? Quibusdam.
              </p>
              <a href="#"><i class="bi bi-twitter text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-facebook text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-linkedin text-dark mx-1"></i></a>
              <a href="#"><i class="bi bi-instagram text-dark mx-1"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section> {% endcomment %}

{% comment %} <!-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ --> {% endcomment %}
    
    

    <div id="carouselExampleIndicators" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="https://source.unsplash.com/random/1920x1080/?computer" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="https://source.unsplash.com/random/1920x1080/?code" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="https://source.unsplash.com/random/1920x1080/?software" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>


<section class="bg-gray-50 dark:bg-gray-700">
  <div class="flex z-20 flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
          <img class="w-8 h-8 mr-2" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" alt="logo">
          Flowbite    
      </a>
      <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                  Contact Us
              </h1>
              <form class="space-y-4 md:space-y-6" action="#">
                  <div>
                      <label for="Name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Full Name</label>
                      {% render_field form.name type="name" name="name" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Your name Please" required=""%}
                  </div>
                  <div>
                      <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email</label>
                      {% render_field form.email type="email" name="email" id="email" placeholder="name@company.com" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""%}
                  </div>
                  <div>
                    <label for="phone_number" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone Number</label>
                    {% render_field form.phone_number type="phone" name="phone_number" id="phone_number" placeholder="Phone Number" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="True"%}
                </div>
                  
                  <button type="submit" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Send</button>
                  
              </form>
          </div>
      </div>
  </div>
</section>

{% extends 'base.html' %}
{%load static%}
{% block content %}


<div class="container-form bg-dark ">
  <div class="row align-items-center g-lg-5 py-5 mt-auto">
    <div class="col-lg-7 text-center text-lg-start">
      <h1 class="display-4 fw-bold lh-1 text-body-emphasis mb-3">Vertically centered hero sign-up form</h1>
      <p class="col-lg-10 fs-4">Below is an example form built entirely with Bootstrap’s form controls. Each required form group has a validation state that can be triggered by attempting to submit the form without completing it.</p>
    </div>
    <div class="col-md-10 mx-auto col-lg-5">
      <!-- <form method="post" action="">
        {% csrf_token %}
        {{ form.as_p }}
        <button class="btn btn-outline-light btn-lg" type="submit">Contact me</button>
    </form> -->
      <form class="p-4 p-md-5 border rounded-3 bg-body-tertiary" method="post" action="">
        {% csrf_token %}
        {{ form.media }}
        <div>
          {{ form.name.label_tag }}
          {{ form.name }}
        </div>
        <div>
          {{ form.email.label_tag }}
          {{ form.email }}
        </div>
        <div>
          {{ form.phone_number.label_tag }}
        {{ form.phone_number }}
        </div>
        <div>
          {{ form.message.label_tag }}
        {{ form.message }}
        </div>
        
        <button class="w-100 btn btn-lg btn-primary" type="submit">Contact me</button>
        <hr class="my-4">
        <small class="text-body-secondary">By clicking Sign up, you agree to the terms of use.</small>
      </form>
    </div>
  </div>
</div>


    
      </section>
{%  endblock content%}


<footer class="bg-light text-dark pt-2 font-monospace footer-padding">
  <div class="container">
    <div class="row justify-content-center"> <!-- Add justify-content-center class here -->
      <div class="col-md-8">
        <p>&copy; 2023 Nilo Cara: Designed & Coded <img width="25" height="25" src="https://img.icons8.com/color/48/python--v1.png" alt="python--v1"/>, <img width="25" height="25" src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/25/external-django-a-high-level-python-web-framework-that-encourages-rapid-development-logo-color-tal-revivo.png" alt="external-django-a-high-level-python-web-framework-that-encourages-rapid-development-logo-color-tal-revivo"/>, <img width="25" height="25" src="https://img.icons8.com/color/48/bootstrap--v2.png" alt="bootstrap--v2"/>, <img width="25" height="25" src="https://img.icons8.com/color/48/webpack.png" alt="webpack"/>, <img width="25" height="25" src="https://img.icons8.com/fluency/25/javascript.png" alt="javascript"/>, <img width="25" height="25" src="https://img.icons8.com/color/25/amazon-web-services.png" alt="amazon-web-services"/> ||
          <a href="https://github.com/niloc95/my_django" target="blank" class="text-reset text-muted px-2">Source Code
            <i class="bi bi-github"></i>
          </a>
          <a href="https://www.linkedin.com/in/nilo-cara/" class="me-4 text-reset">Connect 
            <i class="bi bi-linkedin"></i>
          </a>
        </p>
      </div>
      <div class="col-md-4 text-md-end">
        <p><a class="text-reset text-muted" href="#">Privacy Policy</a> || <a class="text-reset text-muted" href="#">Terms of Use</a></p>
      </div>
    </div>
  </div>
</footer>