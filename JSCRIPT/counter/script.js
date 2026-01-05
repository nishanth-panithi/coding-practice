function decr(){
    let board=document.getElementById("disp")
    let num=parseInt(board.textContent)
    board.textContent=num-1



    let value=parseInt(board.textContent)
    if(value>0)
    {
        board.style.color="green"
    }
    else if(value<0)
    {
        board.style.color="red"
    }
    else 
    {
        board.style.color="black"
    }
}
function incr(){
    let board=document.getElementById("disp")
    let num=parseInt(board.textContent)
    board.textContent=num+1



    let value=parseInt(board.textContent)
    if(value>0)
    {
        board.style.color="green"
    }
    else if(value<0)
    {
        board.style.color="red"
    }
    else 
    {
        board.style.color="black"
    }
}
function clea(){
    let board=document.getElementById("disp")
    board.textContent=0
    board.style.color="black"



   
}