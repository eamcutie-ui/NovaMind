
let currentTool = "chat";

function setTool(tool){
    currentTool = tool;
}

async function sendMessage(){
    const msgInput = document.getElementById("msg");
    const chatContainer = document.getElementById("chat-container");
    const msg = msgInput.value.trim();
    if(!msg) return;

    const userBubble = document.createElement("div");
    userBubble.classList.add("bubble","user");
    userBubble.innerText = msg;
    chatContainer.appendChild(userBubble);

    const loaderBubble = document.createElement("div");
    loaderBubble.classList.add("bubble","ai");
    const loader = document.createElement("span");
    loader.classList.add("loader");
    loaderBubble.appendChild(loader);
    chatContainer.appendChild(loaderBubble);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    msgInput.value = "";

    try{
        const userId = "default";
        let res = await fetch(`/chat?user_id=${userId}&message=${encodeURIComponent(msg)}&tool=${currentTool}`);
        res = await res.json();
        loaderBubble.innerText = currentTool === "image" ? "" : res.response;
        if(currentTool === "image"){
            const img = document.createElement("img");
            img.src = res.response;
            img.style.width="200px";
            loaderBubble.appendChild(img);
        }
    }catch(e){
        loaderBubble.innerText="Error: Cannot reach backend.";
    }
}
