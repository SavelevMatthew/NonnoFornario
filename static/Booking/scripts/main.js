// Perverting animation on resize
let resizeTimer;
window.addEventListener('resize', () => {
    document.body.classList.toggle('resize-animation-stopper');
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        document.body.classList.remove('resize-animation-stopper');
    }, 400)
})
// Checking menu on resize
const hider = window.matchMedia('(min-width: 871px)')
hider.addEventListener('change', uncheckMenu)
uncheckMenu(hider)
// Adding events after page load
window.addEventListener('load', pageLoaded)

function uncheckMenu(hider) {
    const checkbox = document.getElementById('menu-check')
    if (checkbox) {
        if (hider.matches) {
            checkbox.checked = false;
        }
    }
}
let mouseX = 0;
let mouseY = 0;
let hover;
let hover_bg;
let home_text;
let menu;
let home;
let about;

function recolorOnMove(e) {
    mouseX= e.clientX;
    mouseY = e.clientY;
    recolor(mouseX, mouseY)
}
function recolor(x, y) {
    hover_bg.style.clipPath = `circle(150px at ${x}px ${y - 90 + pageYOffset}px)`
    hover_bg.style.transformOrigin = `${x}px ${y - 90 + pageYOffset}px`
    hover_bg.style.transform = 'scale(1.1)'
}

function pageLoaded() {
    hover = document.querySelector('.home');
    hover_bg = document.querySelector('.home__hover');
    home_text = document.querySelector('.home__text');
    menu = document.querySelector('.menu');
    home = document.getElementById('home');
    about = document.getElementById('about');

    if (CSS.supports('clip-path: circle(200px at 100px 100px)') && hover && hover_bg) {
        window.addEventListener('mousemove', recolorOnMove)
        window.addEventListener('scroll', function() {
            recolor(mouseX, mouseY)

        })
        hover.addEventListener('mouseover', function() {
            hover_bg.style.display = 'block';
        })
        hover.addEventListener('mouseout', function(e) {
            if (e.toElement === null || (e.toElement !== home_text && e.toElement.parentElement !== home_text)) {
                hover_bg.style.display = 'none';
            }
        })
    }

    let menu_items = menu.querySelectorAll('.menu__item');
    for (const item of menu_items) {
        item.addEventListener('click', processMenuClick)
    }
    window.addEventListener('scroll', processScroll)
    prepareMap()
    insertMap()
    window.addEventListener('resize', prepareMap)
    // Adding glider
    const glider = new Glide('.images', {
        type: 'carousel',
        perView: 4,
        focusAt: 'center',
        gap: 40,
        breakpoints: {
            1399: {
                perView: 3
            },
            1100: {
                perView: 2
            },
            720: {
                perView: 1
            }

        }
    })
    glider.mount()
    attachMenuComponents()
}
// Process menu clicking
function processMenuClick(e) {
    if (!e.target.classList.contains('menu__item_active')) {
        let active = document.querySelector('.menu__item_active');
        active.classList.toggle('menu__item_active');
        e.target.classList.toggle('menu__item_active');
    }
    const checkbox = document.getElementById('menu-check')
    if (checkbox) {
        checkbox.checked = false;
    }
    let id = e.target.id;
    // SLIDE SCROLL
    if (id === 'home-section') {
        scrollTo(document.documentElement, 0, 800)
    }
    else if (id === 'about-section') {
        scrollTo(document.documentElement, document.getElementById('about').offsetTop - 90, 800)
    }
    else if (id === 'menu-section') {
        scrollTo(document.documentElement, document.getElementById('menu').offsetTop - 90, 800)
    }
}
function scrollTo(element, to, duration) {
    let start = element.scrollTop,
        change = to - start,
        currentTime = 0,
        increment = 20;

    let animateScroll = function(){
        currentTime += increment;
        element.scrollTop = Math.easeInOutQuad(currentTime, start, change, duration);
        if(currentTime < duration) {
            setTimeout(animateScroll, increment);
        }
    };
    animateScroll();
}
//t = current time
//b = start value
//c = change in value
//d = duration
Math.easeInOutQuad = function (t, b, c, d) {
  t /= d/2;
	if (t < 1) return c/2*t*t + b;
	t--;
	return -c/2 * (t*(t-2) - 1) + b;
};
function processScroll() {
    let home = document.getElementById('home')
    let about = document.getElementById('about')
    let menu = document.getElementById('menu')
    if (pageYOffset + 90 < home.offsetHeight) {
        setActive(document.getElementById('home-section'))
    }
    else if (pageYOffset + 90 < about.offsetHeight + about.offsetTop) {
        setActive(document.getElementById('about-section'))
    }
    else if (pageYOffset + 90 < menu.offsetHeight + menu.offsetTop){
        setActive(document.getElementById('menu-section'))
    }
    else {
        setActive(document.getElementById('booking-section'))
    }
}
function setActive(e) {
    let active = menu.querySelector('.menu__item_active')
    if (active && active !== e) {
        active.classList.remove('menu__item_active')
        e.classList.add('menu__item_active')
    }
}

// MAP INSERT
function prepareMap() {
    const mapBox = document.getElementById('map-box')
    if (mapBox) {
        mapBox.removeAttribute('style')
        const w = mapBox.offsetWidth;
        const h = mapBox.offsetHeight;
        if (w > h) {
            mapBox.style.width = `${h}px`
        }
        else {
            mapBox.style.height = `${w}px`
        }

    }
}
function insertMap() {
    const mapBox = document.getElementById('map-box')
    if (mapBox) {
        const w = mapBox.offsetWidth;
        const h = mapBox.offsetHeight;
        const st = window.getComputedStyle(mapBox);
        const p = parseInt(st.paddingTop, 10);
        const b = parseInt(st.border.split(' ')[0], 10);
        let s = Math.min(w, h) - (p + b) * 2;
        const map = `<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2182.2721955186958!2d60.61287581597316!3d56.84127478085842!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x43c16e87d375bcc3%3A0xe766fda4ad15582c!2z0JjQvdGB0YLQuNGC0YPRgiDQvNCw0YLQtdC80LDRgtC40LrQuCDQuCDQutC-0LzQv9GM0Y7RgtC10YDQvdGL0YUg0L3QsNGD0Log0KPRgNCk0KM!5e0!3m2!1sru!2sru!4v1610487790767!5m2!1sru!2sru" width="${s}" height="${s}" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>`
        mapBox.innerHTML = map;
    }
}
function attachMenuComponents() {
    const cards = document.querySelectorAll('.pizza-card')
    if (cards) {
        for (const card of cards) {
            let btn = card.querySelector('.pizza-card__btn');
            let dsc = card.querySelector('.pizza-card__description')
            if (btn && dsc) {
                btn.addEventListener('click', function () {
                    dsc.classList.toggle('pizza-card__description_moved');
                })
            }
        }
    }
}

function hideMessages() {
    $('#message-box').css('display', 'none')
    console.log('asdasd')
}