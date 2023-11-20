


// let a=0

// function com(){
//     if (a===0){
//         a+=1
//         document.getElementById("comments_box").style.display="block"
        
      
        
//     }else{
//         a=0
//         document.getElementById("comments_box").style.display="none"
        
        
//     }
    

   
// }



function toggleComments(postId) {
    var commentsBox = document.getElementById('comments_box_' + postId);
    if (commentsBox.style.display === 'none' || commentsBox.style.display === '') {
        commentsBox.style.display = 'block';
    } else {
        commentsBox.style.display = 'none';
    }
}
