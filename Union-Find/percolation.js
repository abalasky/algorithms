'using strict';

$(document).ready(function() {
    //Anon function as callback to jquery on webpage ready listener

    console.log('Running function')

    let CANVAS = document.querySelector('#grid');
    let CTX = CANVAS.getContext('2d');
    let DIMENSION = 25;
    let WIDTH = CANVAS.width;
    let HEIGHT = CANVAS.height;
    let PIXELSIZE = WIDTH / DIMENSION;

    CTX.strokeStyle = 'lightgrey';

    for (let i = 0; i < DIMENSION; i++) {
        x = Math.floor(i * WIDTH/DIMENSION);
        CTX.beginPath();
        CTX.moveTo(x,0);
        CTX.lineTo(x, HEIGHT);
        CTX.stroke();

        y = Math.floor(i * HEIGHT / DIMENSION);
        CTX.beginPath();
        CTX.moveTo(0,y);
        CTX.lineTo(WIDTH, y);
        CTX.stroke();
    }

    CANVAS.addEventListener('mousedown', mouseFill);
    CANVAS.addEventListener('mousedrag', mouseFill);

    function mouseFill(e) {

        console.log(e);

        let offsetX = e.offsetX;
        let offsetY = e.offsetY;

        pixel = [Math.floor(offsetX / PIXELSIZE), Math.floor(offsetY / PIXELSIZE)];
        fillPixel(pixel);
    }

    function fillPixel(pixel) {
        CTX.fillStyle = 'black';

        CTX.fillRect(pixel[0] * PIXELSIZE, pixel[1] * PIXELSIZE, PIXELSIZE - 1, PIXELSIZE - 1);
    }


});

