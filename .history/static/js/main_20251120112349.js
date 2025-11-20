document.addEventListener('DOMContentLoaded', () => {
    const skipButton = document.querySelector('.Skip');
    if(skipButton){
        skipButton.addEventListener('click', () => {
            window.location = '/skip';
        });
    }
});

const skip_showButton=document.querySelector('.Skip_Show');
if(skip_showButton){
    skip_showButton.addEventListener('click',()=>{
        window.location ='/skip_show';
    });
}

const skip_delete


const addButton = document.querySelector('.Add');


addButton.addEventListener('click', () => {
    
    window.open('/add_page', '_blank'); 
});



addButton.addEventListener('click', () => {
    
    window.open('/add_page', '_blank'); 
});



const deletButton= document.querySelector('.Delete');

deletButton.addEventListener('click' , () => {
window.open('/delete_page','_blank')
});





const ubdateButton = document.querySelector('.Update')
ubdateButton.addEventListener('click', ()=> {
window.open('/update_page','_blank')

});








const showButton = document.querySelector('.Show')
showButton.addEventListener('click',()=>{
window.open('/show_page','_blank')
});




