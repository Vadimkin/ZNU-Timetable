$(document).ready(function() {
    if($('.js-subgroup').get(0)) {
        subgroups = [];
        $('.subgroup').each(function() {
            subgroupID = $(this).data('subgroup');
            if(subgroups.indexOf(subgroupID) == -1) {
                subgroups.push(subgroupID);
            }
        });
        subgroups = subgroups.sort();

        $.each(subgroups, function(key, value) {
             $('.js-subgroup')
                 .append($("<option></option>")
                 .attr("value",value)
                 .text("Підгрупа №" + value));
        });
        if(subgroups.length > 0) {
            $('.js-subgroup').show();
        }
    };

    $('.js-subgroup').on('change', function() {
        currentSubgroup = parseInt($(this).val());
        if(currentSubgroup > 0) {
            $('.subgroup').not('.subgroup__' + currentSubgroup).slideUp();
            $('.subgroup__' + currentSubgroup).slideDown();

            $('.timetable-subGroupInfo').hide();
        } else {
            $('.subgroup').slideDown();
            $('.timetable-subGroupInfo').show();
        }


        cookieData = getCookie('groupInfo')
        if(cookieData) {
            data = JSON.parse(cookieData);
            groupID = $('.js-myGroup').data('group');
            if(data['group_id'] == groupID) {
                data = {'group_id': data['group_id'], 'subgroup_id': currentSubgroup};
                setCookie('groupInfo', JSON.stringify(data), {'path': '/', 'expires': 60*60*24*365});
            }
        }
    });

    if($('.js-myGroup').get(0)) {
        cookieData = getCookie('groupInfo')
        if(cookieData) {
            data = JSON.parse(cookieData);
            groupID = $('.js-myGroup').data('group');
            subGroupIP = data['subgroup_id'];
            if(data['group_id'] != groupID) {
                $('.js-myGroup').show();
            }
            if(subGroupIP != null && subGroupIP != 0 && data['group_id'] == groupID) {
                $(".js-subgroup").val(subGroupIP);
                $('.timetable-subGroupInfo').hide();
                $('.subgroup').not('.subgroup__' + subGroupIP).hide();
                $('.subgroup__' + subGroupIP).show();
            }

        } else {
            $('.js-myGroup').show();
        }
    }

    $('.js-myGroup').on('click', function() {
        // TODO Track events on GA
        data = {'group_id': $(this).data('group')};
        currentSubgroup = $('.js-subgroup').val();
        if(currentSubgroup !== undefined) {
            data['subgroup_id'] = currentSubgroup;
        }

        $(this).hide();
        setCookie('groupInfo', JSON.stringify(data), {'path': '/', 'expires': 60*60*24*365});
        showModal('Збережено', 'Тепер при вході на головну сторінку сайту буде відображатись Ваш розклад.');
    });

    $('.js-sendReport').on('click', function() {
        $('.timetable-lesson').addClass('timetable-lesson__reportMode');
        groupID = $(this).data('group');
        groupName = $(this).data('readablegroup');

        $modalWindow = $('#modalReport');
        $modalWindow.find('#group_id').val(groupID);
        $modalWindow.find('#group').val(groupName);

        $('.alert-report').show();

        $('#modalReport #message-text').on('keyup keydown', function() {
            if($(this).val() == "") {
                $(this).parent().addClass('has-error');
            } else {
                $(this).parent().removeClass('has-error');
            }
        })
    });


    if(getQueryVariable('mode') == "report") {
        $('.js-sendReport').click();
    }

    $('.js-sendReportClose').on('click', function(e) {
        $('.alert-report').slideUp();
        $('.timetable-lesson').removeClass('timetable-lesson__reportMode');
        e.preventDefault();
    });

    $('.js-sendReportMessage').on('click', function(e) {
        showModalReport();
        e.preventDefault();
    });

    $('.js-formReportSend').on('click', function() {
        data = $('#formReport').serialize();
        if($('#modalReport #message-text').val() == "") {
            $('#modalReport #message-text').focus().parent().addClass('has-error');
            return false;
        }
        $.ajax({
            method: "POST",
            url: "/report/",
            data: data
        })
          .done(function( msg ) {
            if(msg.status == 1) {
                $('#modalReport').modal('hide');
                showModal("Результат", "Дякуємо! Ваше повідомлення успішно відправлено");
                $('.js-sendReportClose').click();
            } else {
                alert("Виникла помилка — " + msg.text);
            }
          });
    });

    $('body').on('click', '.timetable-lesson__reportMode .js-lesson', function() {
        timetableID = $(this).data('timetableid');
        lesson = $(this).find(".timetable-info").text();
        $('#modalReport #timetable_id').val(timetableID);
        $('#modalReport #lesson').val(lesson);
        showModalReport();
    });
});

function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
}

function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options) {
  options = options || {};

  var expires = options.expires;

  if (typeof expires == "number" && expires) {
    var d = new Date();
    d.setTime(d.getTime() + expires*1000);
    expires = options.expires = d;
  }
  if (expires && expires.toUTCString) {
  	options.expires = expires.toUTCString();
  }

  value = encodeURIComponent(value);

  var updatedCookie = name + "=" + value;

  for(var propName in options) {
    updatedCookie += "; " + propName;
    var propValue = options[propName];
    if (propValue !== true) {
      updatedCookie += "=" + propValue;
     }
  }

  document.cookie = updatedCookie;
}

function showModal(title, text) {
    $modalWindow = $('#modal');
    $modalWindow.find('.modal-title').html(title);
    $modalWindow.find('.modal-body p').html(text);
    $modalWindow.modal('show');
}

function showModalReport() {
    $modalWindow = $('#modalReport');
    $modalWindow.find('#group_id').val();
    $modalWindow.find('#group').val();
    $modalWindow.modal('show');
}