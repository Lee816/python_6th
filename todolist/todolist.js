(
    function() {
        // 초기 데이터 객체 설정
        if (!(localStorage.getItem('data'))){
            var data = {}; 
            var index = 0;
            localStorage.setItem('data',JSON.stringify(data));
            localStorage.setItem('index',index);
        }
        // 로컬스토리지에 데이터가 있을경우 데이터 반환
        else{
            var contentlist = document.getElementById('contentlist');
            var datakeys = Object.keys(JSON.parse(localStorage.getItem("data")));
            var datavalues = Object.values(JSON.parse(localStorage.getItem("data")));

            // contentbox 자식요소중 제일 앞에 생성 하나씩 생성
            for(var i=0; i<datakeys.length;i++){
                var newcontentbox = '<div class="contentbox"><span class="d-none">'+datakeys[i]+'</span><p class="content">'+datavalues[i]+'</p><button class="btn btn-success" onclick="doneTodo()">완료</button><button class="btn btn-danger" onclick="delTodo()">삭제</button></div>'

                contentlist.insertAdjacentHTML('afterbegin', newcontentbox);
            }
        }
    }
)();
// 입력창 내용 유지
function text(){
    var newContent = document.getElementById("addcontent").innerHTML;
    localStorage.setItem('maintain',newContent);
}
document.getElementById("addcontent").innerHTML = localStorage.getItem('maintain')

// 새로운 todo 생성
function addTodo(){
    var content = localStorage.getItem('maintain');
    var index = localStorage.getItem('index'); 
    var data = JSON.parse(localStorage.getItem("data")); 

    var newcontentbox = '<div class="contentbox"><span class="d-none">'+index+'</span><p class="content">'+content+'</p><button class="btn btn-success" onclick="doneTodo()">완료</button><button class="btn btn-danger" onclick="delTodo()">삭제</button></div>'

    if (content != '' && content != null){
        // contentbox 자식요소중 제일 앞에 생성
        contentlist.insertAdjacentHTML('afterbegin', newcontentbox); 

        document.getElementById("addcontent").innerHTML = '';
        data[index] = content;
        index++;

        localStorage.setItem('data',JSON.stringify(data)); 
        localStorage.setItem('index',index);
        localStorage.setItem('maintain','');
    }
}

// 완료한 todo 표시
function doneTodo(){
    var contentClassList = event.currentTarget.parentNode.children[1].classList; // content의 classlist를 반환

    if (Object.values(contentClassList).includes('done')){
        contentClassList.remove('done');
    } else {
        contentClassList.add('done');
    }
}

// todo 삭제
function delTodo(){
    event.currentTarget.parentNode.remove();
    var data = JSON.parse(localStorage.getItem("data"));
    console.log(event.currentTarget.parentNode.children[0].innerHTML);
    delete data[event.currentTarget.parentNode.children[0].innerHTML];
    localStorage.setItem('data',JSON.stringify(data));
}