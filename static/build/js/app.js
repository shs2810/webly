$(function () {
    console.debug('App start');

    /**
     * Chart default
     * http://www.chartjs.org
     * */
    var charts = $('.wb-chart');
    charts.each(function(){

        var chartCanvas = $(this);
        var ctx = $(this)[0].getContext('2d');
        var type = chartCanvas.data('type');
        var label = chartCanvas.data('label');
        var value = chartCanvas.data('value');
        var bg = chartCanvas.data('bg');

        console.debug(type)
        console.debug(label)
        console.debug(value)
        console.debug(bg)

        var chart = new Chart(ctx, {

            // The type of chart we want to create
            type: type,

            // The data for our dataset
            data: {
                labels: label,
                datasets: [{
                    label: "",
                    data: value,
                    backgroundColor: bg,
                    borderColor: 'transparent'
                }]
            },

            // Configuration options go here
            options: {
            }
        });
    });

});
$(function () {
    $("#owl-subscribe-editor").owlCarousel({
        items: 5,
        autoplay: false,
        loop: false,
        nav: true,
        navText: ['<i class="icon-ep-left-open-big"></i>', '<i class="icon-ep-right-open-big"></i>'],
        dots: false,
        responsive: {
            0: {
                items: 1,
            },
            400: {
                items: 2,
            },
            480: {
                items: 3,
            },
            550: {
                items: 4,
            },
            600: {
                items: 5,
            },
            768: {
                items: 6,
            },
            992: {
                items: 11,
            },
            1200: {
                items: 14,
            },
        }
    });
});
$(function () {

    // 메뉴 클릭 시 닫기 방지.
    $('.nav-underline').find('.dropdown-menu').on('click', function (e) {
        e.stopPropagation();
    });

});
// Preloader
var delayFunc = function (callback, time) {

    if (time === undefined) {
        time = 0;
    }

    var startTime = new Date().valueOf();

    setTimeout(function () {

        var endTime = new Date().valueOf();

        if ((endTime - startTime) > (time + 10)) {
            delayFunc(callback, time);
        } else {
            callback();
        }
    }, time);
};

// For Mozilla, Opera, Webkit
if (document.addEventListener) {
    document.addEventListener("DOMContentLoaded", function () {
        document.removeEventListener("DOMContentLoaded", arguments.callee, false);
        delayFunc(function () {
            $("#page-preloader").fadeOut(500);
            $('body').css('overflow', 'auto');
        }, 100);
    }, false);
}
// For Internet Explorer
else if (document.attachEvent) {
    document.attachEvent("onreadystatechange", function () {
        if (document.readyState === "complete") {
            document.detachEvent("onreadystatechange", arguments.callee);
            delayFunc(function () {
                $("#page-preloader").fadeOut(500);
                $('body').css('overflow', 'auto');
            }, 100);
        }
    });
}
$(function(){
    $.fn.serializeObject = function () {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function () {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };
});
