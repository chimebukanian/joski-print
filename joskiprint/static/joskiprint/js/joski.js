function anim(){
    
    let serv=document.getElementById("service");
    serv.style.left=0;
    serv.style.opacity=0;
    let n=0;
    let opaq=0.9;
    let id = setInterval(move, 50)

    function move(){
    if (n != 30){
        n=n+1;
        serv.style.left=n+'px';
        if (serv.style.opacity<1){   
            serv.style.opacity=Number((1-opaq).toFixed(1))
       
            opaq=opaq-0.1;
            console.log(opaq)
        }
        
        }else{
            clearInterval(id);
        }
    }
}

function formanim(){

    let forms=document.getElementsByTagName('form');
    for (let form of forms){
        form.style.opacity=0
        let opaq=0.9;
        let id = setInterval(fade, 107)
        function fade(){
            if (form.style.opacity<1){   
                form.style.opacity=Number((1-opaq).toFixed(1))               
                opaq=opaq-0.1;
                console.log(opaq)
            }else{
                    clearInterval(id);
            }
        }
            
    }
}

/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }