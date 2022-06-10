const links = document.getElementsByClassName("link");
console.log(links)


for (let link of links){
   link.addEventListener("click", e => {
      e.preventDefault()
      alert(e.target)
      const current = document.querySelector(".active");
      current.classList.remove('active');
      console.log(current)
      e.target.classList.add('active')
   });
}


