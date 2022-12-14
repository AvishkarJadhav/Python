let NamasteBT=document.querySelector('button');
NamasteBT.addEventListener('click', inputMsg);

function inputMsg()
{
    let name=prompt("Enter your name");
    NamasteBT.textContent= 'Roll No.1 :'+name;
}

