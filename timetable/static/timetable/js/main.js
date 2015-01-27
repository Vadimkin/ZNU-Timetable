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
        currentSubgroup = $(this).val();
        $('.subgroup').not('.subgroup__' + currentSubgroup).slideUp();
        $('.subgroup__' + currentSubgroup).slideDown();

        $('.timetable-subGroupInfo').hide();

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
            if(subGroupIP != null) {
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
    $modalWindow = $('.modal')
    $modalWindow.find('.modal-title').html(title);
    $modalWindow.find('.modal-body p').html(text);
    $modalWindow.modal('show')
}