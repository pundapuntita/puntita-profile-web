// Prevent browser scroll hijacking and force start at top
if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}
window.scrollTo(0, 0);

// Reveal Animation on Scroll
document.addEventListener('DOMContentLoaded', () => {
    window.scrollTo(0, 0);

    // Deferred Iframe Loading to prevent autofocus scroll-hijacking
    const appIframe = document.getElementById('appIframe');
    if (appIframe) {
        const loadIframe = () => {
            const dataSrc = appIframe.getAttribute('data-src');
            if (dataSrc && !appIframe.src) {
                appIframe.src = dataSrc;
            }
        };

        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        loadIframe();
                        observer.disconnect();
                    }
                });
            }, { rootMargin: '300px' });
            observer.observe(appIframe);
        } else {
            setTimeout(loadIframe, 1000);
        }
    }

    const reveals = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        reveals.forEach(reveal => {
            const revealTop = reveal.getBoundingClientRect().top;
            if (revealTop < windowHeight - revealPoint) {
                reveal.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger immediately on load

    // Mobile Menu Toggle
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenu && navLinks) {
        mobileMenu.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            
            // Toggle icon between menu and close
            const icon = mobileMenu.querySelector('ion-icon');
            if (navLinks.classList.contains('active')) {
                icon.setAttribute('name', 'close-outline');
            } else {
                icon.setAttribute('name', 'menu-outline');
            }
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                mobileMenu.querySelector('ion-icon').setAttribute('name', 'menu-outline');
            });
        });
    }

    // 3D Tilt Effect on Cards
    const cards = document.querySelectorAll('.card-3d');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; // x position within the element
            const y = e.clientY - rect.top; // y position within the element

            // Calculate rotation values (subtle effect: +/- 2.5 degrees)
            const rotateX = ((y / rect.height) - 0.5) * -5;
            const rotateY = ((x / rect.width) - 0.5) * 5;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.01)`;
        });

        card.addEventListener('mouseleave', () => {
            // Reset transform when mouse leaves
            card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)`;
            card.style.transition = 'transform 0.5s ease';
        });

        card.addEventListener('mouseenter', () => {
            // Remove transition when interacting for instant response
            card.style.transition = 'none';
        });
    });
});

// Modal Gallery Logic
const eventData = {
    japan: {
        title: "Visiting Researcher",
        desc: "Niigata University, Japan | Under Professor Tamaki Tanaka",
        images: ["1.JPG", "2.JPG", "3.JPG"],
        folder: "Japan"
    },
    taiwan: {
        title: "Visiting Researcher",
        desc: "National Sun Yat-sen University, Taiwan | Under Professor Jen-Chih Yao",
        images: ["1.JPG", "2.JPEG", "3.JPG", "4.JPEG", "5.JPEG", "6.JPG", "7.JPG", "8.JPG", "9.JPG", "10.JPG"],
        folder: "Taiwan"
    },
    uttaradit: {
        title: "Invited Speaker",
        desc: "Workshop on “Using AI as an Assistant for Developing Textbooks and Teaching Materials”",
        images: ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"],
        folder: "Uttaradit Rajabhat "
    }
};

window.openModal = function(eventId) {
    const modal = document.getElementById('galleryModal');
    const title = document.getElementById('modalTitle');
    const desc = document.getElementById('modalDesc');
    const gallery = document.getElementById('modalGallery');
    
    const data = eventData[eventId];
    if (!data) return;
    
    title.textContent = data.title;
    desc.textContent = data.desc;
    
    // Clear existing images
    gallery.innerHTML = '';
    
    // Append new images
    data.images.forEach(imgName => {
        const img = document.createElement('img');
        img.src = `${data.folder}/${imgName}`;
        img.alt = `${data.title} Image`;
        img.loading = "lazy";
        gallery.appendChild(img);
    });
    
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent scrolling
};

window.closeModal = function() {
    const galleryModal = document.getElementById('galleryModal');
    if (galleryModal) galleryModal.style.display = 'none';
    document.body.style.overflow = 'auto'; // Re-enable scrolling
};

// Paper Spotlight Modal Logic
window.openPaperModal = function() {
    const modal = document.getElementById('paperModal');
    if (modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
};

window.closePaperModal = function() {
    const modal = document.getElementById('paperModal');
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
};

// Close when clicking outside modal logic
window.onclick = function(event) {
    const galleryModal = document.getElementById('galleryModal');
    const paperModal = document.getElementById('paperModal');
    if (event.target == galleryModal) {
        closeModal();
    }
    if (event.target == paperModal) {
        closePaperModal();
    }
};

// Close modal on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
        closePaperModal();
    }
});
