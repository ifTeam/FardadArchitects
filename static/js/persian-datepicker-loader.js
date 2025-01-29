jQuery(document).ready(function ($) {
    $(document).on('click', '.shamsi_due_date input',function() {
        let value = $("input.elementor-date-time-picker.flatpickr.elementor-control-tag-area.flatpickr-input");
        $(this).pDatepicker({
            format: 'YYYY-MM-DD HH:mm',
            autoClose: true,
            timePicker: {
                enabled: true
            },
            formatter: function (unix) {
                let date = new Date(unix);

                let year = date.getFullYear();
                let month = ('0' + (date.getMonth() + 1)).slice(-2);
                let day = ('0' + date.getDate()).slice(-2);
                let hours = ('0' + date.getHours()).slice(-2);
                let minutes = ('0' + date.getMinutes()).slice(-2);

                let formattedDate = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes;

                let element = document.getElementById(value.attr("id"));

                if (element) {
                    element.value = formattedDate;
                    // Create a new 'input' event
                    let event = new Event('input', {
                        bubbles: true,
                        cancelable: true,
                    });

                    // Dispatch the event
                    element.dispatchEvent(event);
                } else {
                    console.log('Element not found!');
                }

                return formattedDate;
            }
        });
    });
    let flt = $('.elementor-date-time-picker');
    setTimeout(function () {
        $(".flatpickr-calendar").remove();
    },2000)
    setTimeout(function () {
        $(".flatpickr-calendar").remove();
    },1000)
    if (!flt.hasClass('elementor-persian-date')) {
        $(".flatpickr-calendar").remove();
        $('#flatpickr-css').remove();
        $('#flatpickr-js').remove();
        flt.pDatepicker({
            format: 'YYYY-MM-DD HH:mm',
            autoClose: true,
            timePicker: {
                enabled: true
            },
            formatter: function (unix) {
                console.log(unix)
                let date = new Date(unix);

                let year = date.getFullYear();
                let month = ('0' + (date.getMonth() + 1)).slice(-2);
                let day = ('0' + date.getDate()).slice(-2);
                let hours = ('0' + date.getHours()).slice(-2);
                let minutes = ('0' + date.getMinutes()).slice(-2);

                let formattedDate = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes;

                return formattedDate;
            }
        });
    }
    $(document).on('click','.elementor-persian-datepicker-editor,.elementor-persian-date',function () {
        $('.flatpickr-calendar').removeClass('open');
        let options = {
            format: "YYYY-MM-DD",
            initialValue: true,
            autoClose: true,

        };

        if ($(this).is('[min]')) {
            let dateString = $(this).attr('min');
            options.minDate = Date.parse(dateString);
            console.log(options.minDate);
        }

        if ($(this).is('[max]')) {
            let dateString = $(this).attr('max');
            options.maxDate = Date.parse(dateString);
            console.log(options.maxDate);
        }

        $(this).pDatepicker(options);
        $(".flatpickr-calendar").remove();
        $('#flatpickr-css').remove();
        $('#flatpickr-js').remove();
    });

    let pdatepicker = $('.elementor-persian-date');

    if (pdatepicker.length) {
        let options = {
            format: "YYYY-MM-DD",
            initialValue: true,
            autoClose: true,

        };

        if (pdatepicker.is('[min]')) {
            let dateString = pdatepicker.attr('min');
            options.minDate = Date.parse(dateString);
            console.log(options.minDate);
        }

        if (pdatepicker.is('[max]')) {
            let dateString = pdatepicker.attr('max');
            options.maxDate = Date.parse(dateString);
            console.log(options.maxDate);
        }

        pdatepicker.pDatepicker(options);
        $(".flatpickr-calendar").remove();
        $('#flatpickr-css').remove();
        $('#flatpickr-js').remove();
    }
});

