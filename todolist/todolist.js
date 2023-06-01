(
    function() {
        if (!(localStorage.getItem('data'))){
            var data = [];
            localStorage.setItem('data',JSON.stringify(data));
        }
        else{
            var data = JSON.parse(localStorage.getItem("data"));
            for(var i=0; i<data.length;i++){
                var newcontentbox = '<div class="contentbox"><p class="content">'+data[i]+'</p><span class="donedate"></span><button class="btn btn-success" onclick="doneTodo()">완료</button><button class="btn btn-danger" onclick="delTodo()">삭제</button></div>'

                contentlist.insertAdjacentHTML('beforeend', newcontentbox);
            }
        }
    }
)();

function text(){
    var newContent = document.getElementById("addcontent").innerHTML;
    localStorage.setItem('maintain',newContent);
}
document.getElementById("addcontent").innerHTML = localStorage.getItem('maintain')

function addTodo(){
    var contentlist = document.getElementById('contentlist');
    var content = localStorage.getItem('maintain');
    var data = JSON.parse(localStorage.getItem("data"));

    var newcontentbox = '<div class="contentbox"><p class="content">'+content+'</p><span class="donedate"></span><button class="btn btn-success" onclick="doneTodo()">완료</button><button class="btn btn-danger" onclick="delTodo()">삭제</button></div>'

    contentlist.insertAdjacentHTML('beforeend', newcontentbox);
    data.push(content);
    localStorage.setItem('data',JSON.stringify(data));
}

function doneTodo(){
    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2);
    var day = ('0' + today.getDate()).slice(-2);
    var dateString = year + '-' + month  + '-' + day;

    if (Object.values(event.currentTarget.parentNode.children[0].classList).includes('done')){
        event.currentTarget.parentNode.children[0].classList.remove('done');
        event.currentTarget.parentNode.children[1].innerHTML = '';
    } else {
        event.currentTarget.parentNode.children[0].classList.add('done');
        event.currentTarget.parentNode.children[1].innerHTML = dateString;
    }
}

function delTodo(){
    event.currentTarget.parentNode.remove();
    var data = JSON.parse(localStorage.getItem("data"));
    
    localStorage.setItem('data',JSON.stringify(data.filter((element) => element != event.currentTarget.parentNode.children[0].innerHTML)));
}