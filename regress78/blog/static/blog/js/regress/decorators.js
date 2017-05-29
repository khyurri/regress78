(function(W, D, undefined) {
    "use strict";
    var $ = jQuery;

    function ViewDecorator() {
        moment.locale("ru");
        function ajaxifyCb(cb) {
            setInterval(function() {
                cb();
            }, 100);
        };
        return {
            /**
             *  Установка относительного времени
             */
            addMoment: function() {
                var f = function() {
                    var $sel = $(".momentjs");
                    if ($sel.length) {
                        $sel.each(function(k, v) {
                            var $v = $(v);
                            $v.removeClass("momentjs");
                            $v.text(
                                moment($v.text().trim(), "YYYY-MM-DD HH:mm").fromNow()
                            );
                        });
                    }
                }
                ajaxifyCb(f);
            }
        }
    }
    var viewDecorator = ViewDecorator();
    viewDecorator.addMoment();

})(window, document);
