/**
 * Scroll Animation Core
 * Handles image preloading, canvas rendering, and GSAP integration.
 */

const canvas = document.getElementById("animation-canvas");
const context = canvas.getContext("2d");
const progressBar = document.getElementById("progress-bar");
const loadingText = document.getElementById("loading-text");
const loader = document.getElementById("loader");

// Configuration
const frameCount = 132;
const currentFrame = index => (
  `/static/img/${(index + 1).toString().padStart(5, '0')}.png`
);

const images = [];
const animationData = {
  frame: 0
};

// 1. Initial Setup: Resize Canvas
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    render(); // Redraw current frame on resize
}

window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// 2. Preload Images
function preloadImages() {
    let loadedCount = 0;

    return new Promise((resolve) => {
        for (let i = 0; i < frameCount; i++) {
            const img = new Image();
            img.src = currentFrame(i);
            img.onload = () => {
                loadedCount++;
                const progress = Math.round((loadedCount / frameCount) * 100);
                progressBar.style.width = `${progress}%`;
                loadingText.innerText = `Loading Experience ${progress}%`;

                if (loadedCount === frameCount) {
                    resolve();
                }
            };
            images.push(img);
        }
    });
}

// 3. Render Loop
function render() {
    if (!images[animationData.frame]) return;

    const img = images[animationData.frame];
    
    // Maintain aspect ratio (Object-fit: cover logic for canvas)
    const imgRatio = img.width / img.height;
    const canvasRatio = canvas.width / canvas.height;
    
    let drawWidth, drawHeight, offsetX, offsetY;

    if (imgRatio > canvasRatio) {
        drawHeight = canvas.height;
        drawWidth = canvas.height * imgRatio;
        offsetX = (canvas.width - drawWidth) / 2;
        offsetY = 0;
    } else {
        drawWidth = canvas.width;
        drawHeight = canvas.width / imgRatio;
        offsetX = 0;
        offsetY = (canvas.height - drawHeight) / 2;
    }

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img, offsetX, offsetY, drawWidth, drawHeight);
}

// 4. Initialization
async function init() {
    // Wait for images to load
    await preloadImages();

    // Hide loader
    gsap.to(loader, {
        opacity: 0,
        duration: 1,
        ease: "power2.inOut",
        onComplete: () => loader.classList.add("hidden")
    });

    // Reveal main content
    gsap.from("#main-container", {
        opacity: 0,
        duration: 2,
        ease: "power2.out"
    });

    // Initial render
    render();

    // Setup GSAP ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);

    gsap.to(animationData, {
        frame: frameCount - 1,
        snap: "frame",
        ease: "power1.inOut", // User requested easing for smooth transitions
        scrollTrigger: {
            trigger: ".scroll-spacer",
            start: "top top",
            end: "bottom bottom",
            scrub: 1.5, // Added slight delay for "extra smooth" feel, 1:1 scrubbing would be scrub: true
            onUpdate: render
        }
    });

    // Subtle parallax for depth (optional enhancement)
    gsap.to(".canvas-wrapper", {
        scale: 1.1,
        scrollTrigger: {
            trigger: ".scroll-spacer",
            start: "top top",
            end: "bottom bottom",
            scrub: true
        }
    });

    // --- New Storytelling & Cinematic Logic ---
    
    // 1. Text Chapter Timelines
    const storyTl = gsap.timeline({
        scrollTrigger: {
            trigger: ".scroll-spacer",
            start: "top top",
            end: "bottom bottom",
            scrub: 1 // Slightly faster than the image scrub for crisp text feel
        }
    });

    // Chapter 1: 5% - 25% (Down to Up feel: +40 to -40)
    storyTl.fromTo("#chapter-1", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 1 }, 0.05)
           .to("#chapter-1", { opacity: 0, y: -40, duration: 1 }, 0.25);

    // Chapter 2: 35% - 55%
    storyTl.fromTo("#chapter-2", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 1 }, 0.35)
           .to("#chapter-2", { opacity: 0, y: -40, duration: 1 }, 0.55);

    // Chapter 3: 65% - 85%
    storyTl.fromTo("#chapter-3", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 1 }, 0.65)
           .to("#chapter-3", { opacity: 0, y: -40, duration: 1 }, 0.85);

    // 2. Background Fade to Black (80% -> End)
    gsap.to("#cinematic-overlay", {
        opacity: 1,
        scrollTrigger: {
            trigger: ".scroll-spacer",
            start: "75% top",
            end: "95% top",
            scrub: true
        }
    });

    // 3. Staggered Footer Reveal (Down to Up)
    gsap.to(".footer-content .slide-up", {
        opacity: 1,
        y: 0,
        stagger: 0.2,
        duration: 1,
        ease: "power2.out",
        scrollTrigger: {
            trigger: ".scroll-spacer",
            start: "90% top",
            end: "bottom bottom",
            scrub: 1
        }
    });

    // 4. Header Animation
    gsap.to(".main-header", {
        backgroundColor: "rgba(0,0,0,0.8)",
        padding: "15px 60px",
        scrollTrigger: {
            trigger: ".scroll-spacer",
            start: "10% top",
            end: "20% top",
            scrub: true
        }
    });

    // Initial Guidance Animation
    gsap.from(".main-header", { y: -100, opacity: 0, duration: 1.5, delay: 0.5 });
    gsap.from(".story-container", { scale: 0.8, opacity: 0, duration: 2, delay: 1 });
}

// Start the sequence
init();
