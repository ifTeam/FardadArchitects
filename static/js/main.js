document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mainMenu = document.querySelector('.main-menu');

    mobileMenuToggle.addEventListener('click', () => {
        mobileMenuToggle.classList.toggle('active');
        mainMenu.classList.toggle('active');
    });

    // Initialize Swiper
    const projectsSwiper = new Swiper('.projects-grid', {
        loop: true,
        slidesPerView: 1,
        spaceBetween: 30,
        autoplay: {
            delay: 5000,
        },
        breakpoints: {
            768: {
                slidesPerView: 2,
            },
            1024: {
                slidesPerView: 3,
            }
        }
    });

    // Lazy Loading
    const lazyLoad = () => {
        const lazyElements = document.querySelectorAll('[loading="lazy"]');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const element = entry.target;
                    element.src = element.dataset.src;
                    element.classList.add('fade-in');
                    observer.unobserve(element);
                }
            });
        });

        lazyElements.forEach(element => observer.observe(element));
    };

    lazyLoad();

    // Video AutoPlay
    const backgroundVideo = document.querySelector('.background-video');
    if (backgroundVideo) {
        backgroundVideo.play().catch(error => {
            // Handle autoplay restrictions
            const playButton = document.createElement('button');
            playButton.innerHTML = 'Play Video';
            playButton.classList.add('video-play-button');
            backgroundVideo.parentElement.appendChild(playButton);
            
            playButton.addEventListener('click', () => {
                backgroundVideo.play();
                playButton.remove();
            });
        });
    }

    // Window Resize Handler
    let resizeTimer;
    window.addEventListener('resize', () => {
        document.body.classList.add('resize-animation-stopper');
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            document.body.classList.remove('resize-animation-stopper');
        }, 400);
    });
});