// Function to make balls bounce on click
function bounceBall(ball) {
    ball.style.transform = 'scale(1.2)';
    setTimeout(function () {
        ball.style.transform = 'scale(1)';
    }, 200);
}

// Function to make balls draggable
function makeBallDraggable(ball) {
    let isMouseDown = false;
    let offsetX, offsetY;

    ball.addEventListener('mousedown', function (e) {
        isMouseDown = true;
        offsetX = e.clientX - ball.offsetLeft;
        offsetY = e.clientY - ball.offsetTop;
        document.addEventListener('mousemove', moveBall);
        document.addEventListener('mouseup', function () {
            isMouseDown = false;
            document.removeEventListener('mousemove', moveBall);
        });
    });

    function moveBall(e) {
        if (!isMouseDown) return;
        ball.style.left = e.clientX - offsetX + 'px';
        ball.style.top = e.clientY - offsetY + 'px';
    }
}

// Apply draggable behavior to all balls
const balls = document.querySelectorAll('.ball');
balls.forEach(ball => makeBallDraggable(ball));
