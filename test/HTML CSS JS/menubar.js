window.addEventListener("load",()=>{
  for (const bar of document.getElementsByClassName("menubar")){
    for(const a of bar.getElementsByTagName("a")){
      if(a.href == window.location.href){
        a.className = "active";
      }
    }
  }
});
