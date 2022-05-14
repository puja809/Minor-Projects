showNotes();
// When an end-user adds a note add it to local storage:
console.log('My Notes');

let addBtn=document.getElementById('addBtn');
addBtn.addEventListener("click",function(e){
    let text=document.getElementById('textArea');
    let title=document.getElementById('addTitle');
    let notesObj=[];
    let notes=localStorage.getItem("notes");
    if(notes==null){
        notesObj==[];
    }
    else{
        notesObj=JSON.parse(notes);
    }
    let MynotesObj={
        title: title.value,
        text: text.value
    };
    notesObj.push(MynotesObj);
    localStorage.setItem("notes",JSON.stringify(notesObj));
    text.value="";
    title.value="";
    console.log(notesObj);
    showNotes();
})
// Fucntion to add the notes. This will show the elements from local storage in form of notes
function showNotes(){
    // let notesObj=[];
    let notes=localStorage.getItem("notes");
    if(notes==null){
        notesObj=[];
    }
    else{
        notesObj=JSON.parse(notes);
    }
    let html="";
    notesObj.forEach(function(element,index) {
        html+=`<div class="cardNotes my-3 mx-3" style="width: 18rem;">
        <div class="card-body my-3 mx-3" style="border:0.5px solid grey; border-radius:9px;">
          <h5 class="card-title" style="font-weight: bold;"> ${element.title}</h5>
          <p class="card-text">
          ${element.text}
          </p>
          <button id="note-${index+1}" 
          onclick="deleteNotes(this.id)"
          class="btn btn-primary">Delete Notes</button>
        </div>
      </div>
        `
    });
    let cardElm= document.getElementById("notes");
    if(notesObj.length!=0){
       cardElm.innerHTML=html;
    }
    else{
        cardElm.innerHTML=`Please add your Notes here!!!`
    }
}

// Function to delete the notes
function deleteNotes(index){
    // console.log("Delete",index);
    let notes=localStorage.getItem("notes");
    if(notes==null){
        notesObj==[];
    }
    else{
        notesObj=JSON.parse(notes);
    }
    notesObj.splice(index,1);
    localStorage.setItem("notes",JSON.stringify(notesObj));
    showNotes();
}


// Function to search content in the notes
let search=document.getElementById('searchTxt');
search.addEventListener("input",function(){
    let inputVal=search.value.toLowerCase();
    // console.log('input event',inputVal);
    let notecards=document.getElementsByClassName('cardNotes');
    // console.log(notecards);
    Array.from(notecards).forEach(function(element){
        let crdTxt=element.getElementsByTagName("p")[0].innerText.toLocaleLowerCase();
        // console.log(crdTxt);
        if(crdTxt.includes(inputVal)){
            element.style.display="block";
        }
        else{
            element.style.display="none";
        }
    })
})