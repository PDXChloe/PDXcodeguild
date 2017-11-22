// clock stuff


let wrapper = document.getElementById('wrapper');
let clock_interval = 0;
let clock_demo = document.getElementById('clock_demo');
let clock = document.getElementById('clock');
let date = null;
// let overlay = document.getElementById('overlay');

// overlay.addEventListener("load", loadOverlay);

// function loadOverlay() {
//     overlay.style.display = 'block';
// }


clock.addEventListener('click', function() {
    clearInterval(clock_interval);
    clock_interval = setInterval(function() {
        date = new Date(2017, 11, 20, 7, 0, 0, 0);
        // date = new Date(2017, 11, 20, 8, 0, 0, 0);
        // date = new Date(2017, 11, 20, 11, 0, 0, 0);
        // date = new Date(2017, 11, 20, 12, 0, 0, 0);
        // date = new Date(2017, 11, 20, 15, 0, 0, 0);
        // date = new Date(2017, 11, 20, 16, 0, 0, 0);
        // date = new Date(2017, 11, 20, 17, 0, 0, 0);
        // date = new Date(2017, 11, 20, 18, 0, 0, 0);
        // date = new Date(2017, 11, 20, 21, 0, 0, 0);
        date = new Date();
        clock_demo.innerText = date.toLocaleTimeString();

        let greetingBox = document.getElementById('greeting_box');
        let greeting = document.getElementById('greeting');
        let wakeUpTime = 7;
        let coffeeTime = 8;
        let almostLunchTime = 11;
        let lunchTime = 12;
        let napTime = 14;
        let cookieTime = 16;
        let quitingTime = 17;
        let dinnerTime = 18;
        let sleepyTime = 21;
        let animate_directions = 'moveInLeft 3s ease-out';
        let wrapper_animate_directions = 'phaseIn 2s ease-out';
        
        let current_hours = date.getHours();
        // let current_minutes = date.getMinutes();

        if (current_hours >= wakeUpTime) {
          wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(255, 153, 51, 0.7),' +
                'rgba(1, 78, 180, 0.7)), url("sunrisewindow.jpg")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'Wakey!!! Wakey!!!';
            greetingBox.style.animation = animate_directions;
        }

        if (current_hours >= coffeeTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(255, 255, 0, 0.7),' +
                'rgba(1, 78, 180, 0.7)), url("full-background-netarts2.png")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'Coffee, NOW!!!!';
            greetingBox.style.animation = animate_directions;
            if (current_hours >= coffeeTime + 1) {
                greeting.innerText = 'Time for cup #2!!';
            }
        }

        if (current_hours >= almostLunchTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(255, 255, 51, 0.7),' +
                'rgba(204, 255, 255, 0.7)), url("sunrisewindow.jpg")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = "Is it Lunch Time yet?";
            greetingBox.style.animation = animate_directions;
        }

        if (current_hours >= lunchTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(255, 51, 51, 0.7),' +
                'rgba(204, 255, 255, 0.7)), url("lemons.jpg")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'So Hangry! Let\'s Do lunch!';
            greetingBox.style.animation = animate_directions;
            if (current_hours >= lunchTime + 1) {
                greeting.innerText = 'Lunchtime is a good time!';
            }
        }

        if (current_hours >= napTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(0,0,0, 0.8),' +
                'rgba(255, 51, 51, 0.5)), url("skytrees.jpg")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'Is it Naptime yet?!';
            greetingBox.style.animation = animate_directions;
            if (current_hours >= napTime + 1) {
                greeting.innerText = 'Yaaaawn!';
            }
        }

        if (current_hours >= cookieTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(255, 153, 51, 0.8),' +
                'rgba(51, 26, 0, 0.6)), url("cookietime.jpg")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'Where are the cookies?!';
            greetingBox.style.animation = animate_directions;
        }

        if (current_hours >= quitingTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(255, 255, 255, 0.8),' +
                'rgba(51, 26, 0, 0.6)), url("quittime.jpg")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'What a great day!';
            greetingBox.style.animation = animate_directions;

        }

        if (current_hours >= dinnerTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(0, 0, 0, 0.5),' +
                'rgba(128, 0, 0, 0.8)), url("cookingbooks.jpg")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'Time to dine...';
            greetingBox.style.animation = animate_directions;

        }
        if (current_hours >= sleepyTime) {
            wrapper.style.backgroundImage = 'linear-gradient(to right bottom,' + 'rgba(242, 242, 242, 0.1),' +
                'rgba(0, 0, 0, 0.9)), url("full-background-netarts2.png")';
            clock_demo.style.animation = wrapper_animate_directions;
            greeting.innerText = 'Shhhhh.....Snooozing!';
            greeting.style.color = 'yellow';
            greetingBox.style.animation = animate_directions;
        }
        //clock_demo.innerText = date.getFullYear()+':'+(date.getMonth()+1) + ':' + date.getDate() + ' ' + date.getHours() + ':' + date.getMinutes()+':'+date.getSeconds();

    }, 1000);

});

// stopwatch stuff
let start_btn = document.getElementById("start_btn");
let stop_btn = document.getElementById("stop_btn");
let stopwatch_date = new Date();


let stopwatch_interval = 0;
start_btn.addEventListener('click', function() {
    clearInterval(clock_interval);
    stopwatch_date.setHours(0,0,0,0);
    stopwatch_interval = setInterval(function () {
        let seconds = stopwatch_date.getSeconds();
        stopwatch_date.setSeconds(seconds + 1);
        clock_demo.innerText = stopwatch_date.getHours() + ':' + stopwatch_date.getMinutes() + ':' + stopwatch_date.getSeconds();
    }, 1000);
});

stop_btn.addEventListener('click', function() {
    clearInterval(stopwatch_interval);
});



