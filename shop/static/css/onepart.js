console.log("если читаешь, значит работает* ");

const header = document.querySelector("#pol");

window.addEventListener("scroll", function(){
    console.log("Наверное");
    let scrollPols = window.scrollY;
    if(scrollPols>0){
      header.classList.add("red");
  }
    else{
      header.classList.remove("red");
  }
});
