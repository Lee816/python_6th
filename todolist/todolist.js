(
    function() {
        if (!(localStorage.getItem('data'))){
            var data = {}; 
            var index = 1;
            localStorage.setItem('data',JSON.stringify(data));
            localStorage.setItem('index',index);
        }
        else{
            var contentlist = document.getElementById('contentlist'); 
            var data = Object.values(JSON.parse(localStorage.getItem("data")));
            
            for(var i=0; i<data.length;i++){
                var newcontentbox = '<div class="contentbox"><span class="d-none">'+index+'</span><p class="content">'+data[i]+'</p><button class="btn btn-success" onclick="doneTodo()">완료</button><button class="btn btn-danger" onclick="delTodo()">삭제</button></div>'

                contentlist.insertAdjacentHTML('afterbegin', newcontentbox);
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
    var index = localStorage.getItem('index'); 
    var data = JSON.parse(localStorage.getItem("data")); 

    var newcontentbox = '<div class="contentbox"><span class="d-none">'+index+'</span><p class="content">'+content+'</p><button class="btn btn-success" onclick="doneTodo()">완료</button><button class="btn btn-danger" onclick="delTodo()">삭제</button></div>'

    if (content != '' && content != null){
        contentlist.insertAdjacentHTML('afterbegin', newcontentbox); 

        data[index] = content;
        index++;
        localStorage.setItem('data',JSON.stringify(data)); 
        localStorage.setItem('index',index);
        document.getElementById("addcontent").innerHTML = '';
        localStorage.setItem('maintain','');
    }
}

function doneTodo(){
    if (Object.values(event.currentTarget.parentNode.children[1].classList).includes('done')){
        event.currentTarget.parentNode.children[1].classList.remove('done');
    } else {
        event.currentTarget.parentNode.children[1].classList.add('done');
    }
}

function delTodo(){
    event.currentTarget.parentNode.remove();
    var data = JSON.parse(localStorage.getItem("data"));

    delete data[event.currentTarget.parentNode.children[0].innerHTML];
    localStorage.setItem('data',JSON.stringify(data));
}