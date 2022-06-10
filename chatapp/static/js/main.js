


        $(document).on('submit', '#social-form', function (e) {
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: "{% url 'social-update' %}",
                data: {
                   facebook: $('#facebookId').val(),
                    twitter: $('#twitterId').val(),
                    instagram: $('#instagramId').val(),
                    linkedin: $('#linkedinId').val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function (data) {
                    $('h8').html(data)
                }
            })
            document.getElementById('fbook').innerHTML = document.getElementById('facebookId').value
            document.getElementById('twi').innerHTML = document.getElementById('twitterId').value
            document.getElementById('insta').innerHTML = document.getElementById('instagramId').value
            document.getElementById('linked').innerHTML = document.getElementById('linkedinId').value
        })

var formData = new FormData();

$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();
    formData.append('first_name', $('#firstName').val())
    formData.append('last_name', $('#lastName').val())
    formData.append('dob', $('#birthDate').val())
    formData.append('number', $('#mobileNumber').val())
    formData.append('address', $('#Address').val())
    formData.append('website', $('#webSite').val())
    formData.append('email', $('#emailAddress').val())
    formData.append('picture', $('#profile-img')[0].files[0])
    formData.append('csrfmiddlewaretoken', '{{ csrf_token }}')
    $.ajax({
        type: 'POST',
        url: "{% url 'update-account' %}",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: "multipart/form-data",
        success: function (data) {
            $('h7').html(data)
        }
    })
    document.getElementById('user-name').innerHTML = document.getElementById('firstName').value
    document.getElementById('birth-date-text').innerHTML = document.getElementById('birthDate').value
    document.getElementById('phone-text').innerHTML = document.getElementById('mobileNumber').value
    document.getElementById('email-text').innerHTML = document.getElementById('emailAddress').value
    document.getElementById('website-text').innerHTML = document.getElementById('webSite').value
    document.getElementById('address-text').innerHTML = document.getElementById('Address').value
})

$(document).on('submit', '#social-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "{% url 'social-update' %}",
        data: {
           facebook: $('#facebookId').val(),
            twitter: $('#twitterId').val(),
            instagram: $('#instagramId').val(),
            linkedin: $('#linkedinId').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('h8').html(data)
        }
    })
    document.getElementById('fbook').innerHTML = document.getElementById('facebookId').value
    document.getElementById('twi').innerHTML = document.getElementById('twitterId').value
    document.getElementById('insta').innerHTML = document.getElementById('instagramId').value
    document.getElementById('linked').innerHTML = document.getElementById('linkedinId').value
})

$(document).on('submit', '#password-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "{% url 'password-change' %}",
        data: {
            old: $('#current-password').val(),
            new: $('#new-password').val(),
            confirm: $('#repeat-password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            // $('h9').html(data)
            window.location.href = "{% url 'login' %}";
        },
    })
 
})

function send_privacy () {
    $(document).on('submit', '#privacy', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "{% url 'update-privacy' %}",
            data: {
                picture_see: $('#profile-pic-see').val(),
                last_seen: $('#last-seen').val(),
                group: $('#group').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $('h9').html(data)
            },
        })
    
    })
}

$(document).on('submit', '#security', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "{% url 'update-security' %}",
        data: {
            twofac: $('#twoFactorSwitch').val(),
            device: $('#unrecognisedSwitch').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('h10').html(data)
        },
    })
 
})

$(document).on('submit', '#task-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "{% url 'add-task' %}",
        data: {
            task_name: $('#addTaskName').val(),
            task_detail: $('#addTaskDetails').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#add-task-id').html(data)
        },
    })
    $( "#todo-container1" ).load(window.location.href + " #todo-container1" );
})

$(document).on('submit', '#task-edit-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  document.getElementById('save-button').href,
        data: {
            task_name: $('#editTaskName').val(),
            task_detail: $('#editTaskDetails').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data)
        },
    });
    $( "#todo-container1" ).load(window.location.href + " #todo-container1" );
})

$(document).on('click', '#finish-button', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  document.getElementById('finish-button').href,
        data: {
            testd: 'data'
        },
        success: function (data) {
            $('#update-success').html(data)
        },
    });
    $( "#todo-container1" ).load(window.location.href + " #todo-container1" );
})

$(document).on('click', '#search-submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/search/",
        data: {
            search: $('#search-content').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            const el = document.querySelector('#search-con');
            el.style.visibility = 'visible';
            // console.log(data)
            load_tasks(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#todo-container1").empty();
    
})

$(document).on('click', '#stat', function (e) {
    // $(".todo-container").show();
    $("#tasks").empty();
    $( "#todo-container1" ).load(location.href + " #todo-container1" );    
})

$(document).on('click', '#stat2', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/filter-task/",
        data: {
            status: document.getElementById('stat2').innerHTML,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            const el = document.querySelector('#search-con');
            el.style.visibility = 'visible';
            // console.log(data)
            load_tasks(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#todo-container1").empty();
    
})

$(document).on('click', '#stat3', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/filter-task/",
        data: {
            status: document.getElementById('stat3').innerHTML,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            const el = document.querySelector('#search-con');
            el.style.visibility = 'visible';
            // console.log(data)
            load_tasks(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#todo-container1").empty();
    
})

$(document).on('submit', '#note-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:8000/add-note/",
        data: {
            note_name: $('#addNoteName').val(),
            note_detail: $('#addNoteDetails').val(),
            tag: $('#note-tag').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#add-note-id').html(data)
        },
    })
    $( "#note-container" ).load(window.location.href + " #note-container" );
})



// filter for note
// filter fot note
// 
// 
// 
// 
// 



$(document).on('click', '#note-filter1', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/get-notes/",
        data: {
            status: document.getElementById('note-filter1').innerHTML,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            // const el = document.querySelector('#search-con');
            // el.style.visibility = 'visible';
            // console.log(data)
            load_notes(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#note-container1").empty();
    
})

$(document).on('click', '#note-filter2', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/get-notes/",
        data: {
            status: document.getElementById('note-filter2').innerHTML,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            // const el = document.querySelector('#search-con');
            // el.style.visibility = 'visible';
            // console.log(data)
            load_notes(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#note-container1").empty();
    
})


$(document).on('click', '#note-filter3', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/get-notes/",
        data: {
            status: document.getElementById('note-filter3').innerHTML,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            // const el = document.querySelector('#search-con');
            // el.style.visibility = 'visible';
            // console.log(data)
            load_notes(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#note-container1").empty();
    
})

$(document).on('click', '#note-filter4', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/get-notes/",
        data: {
            status: document.getElementById('note-filter4').innerHTML,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            // const el = document.querySelector('#search-con');
            // el.style.visibility = 'visible';
            // console.log(data)
            load_notes(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#note-container1").empty();
    
})


$(document).on('click', '#note-filter5', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url:  "http://127.0.0.1:8000/get-notes/",
        data: {
            status: document.getElementById('note-filter5').innerHTML,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('#update-success').html(data.task)
            // const el = document.querySelector('#search-con');
            // el.style.visibility = 'visible';
            // console.log(data)
            load_notes(data)
        },
    });
    // $( "#todo-container" ).load(location.href + " #todo-container" );
    $("#note-container1").empty();
    
})

// $(document).on('click', '#note-search-submit', function (e) {
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url:  "http://127.0.0.1:8000/search-note/",
//         data: {
//             search: $('#search-note-input').val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         },
//         success: function (data) {
//             $('#update-success').html(data.task)
//             const el = document.querySelector('#search-con');
//             el.style.visibility = 'visible';
//             // console.log(data)
//             load_notes(data)
//         },
//     });
//     // $( "#todo-container" ).load(location.href + " #todo-container" );
//     $("#note-container1").empty();

// })

// $(document).on('Enter', '#search-note-input', function (e) {
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url:  "http://127.0.0.1:8000/search-note/",
//         data: {
//             search: $('#search-note-input').val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         },
//         success: function (data) {
//             $('#update-success').html(data.task)
//             const el = document.querySelector('#search-con');
//             el.style.visibility = 'visible';
//             // console.log(data)
//             load_notes(data)
//         },
//     });
//     // $( "#todo-container" ).load(location.href + " #todo-container" );
//     $("#note-container1").empty();

// })

document.getElementById('search-note-input').addEventListener('keypress', function(event) {
    // you could also do keyCode === 13
    if (event.key === 'Enter') {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url:  "http://127.0.0.1:8000/search-note/",
            data: {
                search: $('#search-note-input').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $('#update-success').html(data.task)
                const el = document.querySelector('#search-con');
                el.style.visibility = 'visible';
                // console.log(data)
                load_notes(data)
            },
        });
        // $( "#todo-container" ).load(location.href + " #todo-container" );
        $("#note-container1").empty();
    }
  })




