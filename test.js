export const equivalentKeyPresses=(arr)=>{
    const firstKeys=returnOnlyKeys(arr[0].split(','))
    const secondKeys=returnOnlyKeys(arr[1].split(','))

    console.log(firstKeys);
    console.log(secondKeys);
    

    return firstKeys===secondKeys ? true :false
}

const returnOnlyKeys=(strArr) =>{
    if(strArr.indexOf("-B") === -1) return strArr.join(',')

    for(let i=0;i<strArr.length;i++){
        if(
            strArr[i] === "-B" &&
            strArr[i-1] != "-B" &&
            strArr[i-1 ] != undefined
        ) strArr.splice(i-1,2)
    }
    return strArr.filter((key)=>{return key !="-B"}).join(',')
}