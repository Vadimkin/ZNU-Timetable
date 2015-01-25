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