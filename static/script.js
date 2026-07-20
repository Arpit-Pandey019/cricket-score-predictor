document.addEventListener("DOMContentLoaded",()=>{

    const form=document.querySelector("form");

    form.addEventListener("submit",()=>{

        const btn=document.querySelector("button");

        btn.innerHTML="Predicting...";

        btn.disabled=true;

    });

});