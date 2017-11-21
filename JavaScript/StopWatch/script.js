// clock stuff
let wrapper = document.getElementById('wrapper');
let clock_interval = 0;
let clock_demo = document.getElementById('clock_demo');
let clock = document.getElementById('clock');
let date = null;

clock.addEventListener('click', function() {
    clearInterval(clock_interval);
    clock_interval = setInterval(function() {
        // date = new Date(2017, 11, 20, 7, 0, 0, 0);
        // date = new Date(2017, 11, 20, 8, 0, 0, 0);
        // date = new Date(2017, 11, 20, 12, 0, 0, 0);
        // date = new Date(2017, 11, 20, 15, 0, 0, 0);
        // date = new Date(2017, 11, 20, 16, 0, 0, 0);
        // date = new Date(2017, 11, 20, 18, 0, 0, 0);
        // date = new Date(2017, 11, 20, 21, 0, 0, 0);
        date = new Date();
        clock_demo.innerText = date.toLocaleTimeString();


        let greeting = document.getElementById('greeting');
        let wakeUpTime = 7;
        let coffeeTime = 8;
        let lunchTime = 12;
        let napTime = 15;
        let unwindTime = 16;
        let quitingTime = 17;
        let dinnerTime = 18;
        let sleepyTime = 21;
        let animate_directions = 'moveInLeft 5s ease-out';
        let wrapper_animate_directions = 'phaseIn 3s ease-in';
        
        let current_hours = date.getHours();

        if (current_hours >= wakeUpTime) {
            let pic1 = 'linear-gradient(to right bottom,' + 'rgba(255, 153, 51, 0.7),' +
                'rgba(1, 78, 180, 0.7)), url("sunrisewindow.jpg")';
            wrapper.style.backgroundImage = pic1;
            greeting.innerText = 'Wakey!!! Wakey!!!';
        }

        if (current_hours >= coffeeTime) {
            let pic2 = 'linear-gradient(to right bottom,' + 'rgba(255, 255, 0, 0.7),' +
                'rgba(1, 78, 180, 0.7)), url("full-background-netarts2.png")';
            wrapper.style.backgroundImage = pic2;
            greeting.innerText = 'Coffee, NOW!!!!';
        }

        if (current_hours >= lunchTime) {
            greeting.innerText = 'So Hangry! Let us lunch!';
        }

        if (current_hours >= napTime) {
            greeting.innerText = 'Naptime!';
        }

        if (current_hours >= unwindTime) {
            greeting.innerText = 'It is almost the end of the day! Horray!';
        }

        if (current_hours >= quitingTime) {
            greeting.innerText = 'What a great day!';
        }
        if (current_hours >= dinnerTime) {
            greeting.innerText = 'Time to dine...';

        }
        if (current_hours >= sleepyTime) {
            let pic8 = 'linear-gradient(to right bottom,' + 'rgba(242, 242, 242, 0.1),' +
                'rgba(0, 0, 0, 0.9)), url("full-background-netarts2.png")';
            wrapper.style.backgroundImage = pic8;
            wrapper.style.animation = wrapper_animate_directions;
            greeting.innerText = 'Shhhhh.....Snooozing!';
            greeting.style.color = 'yellow';
            greeting.style.animation = animate_directions;
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



