function findpath(){
    console.log("findpath!");
    $.ajax({
        url: "/getpath",
        type: 'GET',
        success: function (response) {
            console.log(response)
            jsonresp = JSON.stringify(response)
            document.getElementsByName('mapdata')[0].innerHTML = jsonresp
        },
        error: function (response) {
            console.log('fail')
        }
    });
}

function searchstart(){
    console.log("searchstart!");
    start = document.getElementsByName('start')[0].value
    $.ajax({
        url: "/searchstart",
        type: 'POST',
        data: {
            startname: start
        },
        success: function (response) {
            console.log(response)
            document.getElementsByName('start')[0].value = response.data
        },
        error: function (response) {
            console.log('fail')
        }
    });
}

function searchdest(){
    console.log("searchdest!");
    dest = document.getElementsByName('destination')[0].value
    $.ajax({
        url: "/searchdest",
        type: 'POST',
        data: {
            destname: dest
        },
        success: function (response) {
            console.log(response)
            document.getElementsByName('destination')[0].value = response.data
        },
        error: function (response) {
            console.log('fail')
        }
    });
}