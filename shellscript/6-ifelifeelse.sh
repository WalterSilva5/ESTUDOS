#!/bin/bash
    
function a(){
    a=3
    b=5
    if((a==b))
    then
        echo "a = b"
    elif((a!=b))
    then 
        echo "a != b"
    else
        echo "erro"
    fi
}    


function b(){
    for i in [1,2,3,4];
    do
        echo "$i"
    done;
}

function c(){
    x=0
    while($x<3);
        echo $x;
        x++;
}

a
b
c
