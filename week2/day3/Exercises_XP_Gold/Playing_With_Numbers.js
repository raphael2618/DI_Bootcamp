let age = [20,5,12,43,98,55];
let sum=0
for(let i=0;i<age.length;i++) {

    sum=sum+age[i]
}
console.log(sum)

function MyMax(myarr){
    let al = myarr.length;
    maximum = myarr[al-1];
    while (al--){
        if(myarr[al] > maximum){
            maximum = myarr[al]
        }
    }
    return maximum;
};