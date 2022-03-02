let changeColor = document.getElementById("changeColor");

chrome.storage.sync.get("color", ({ color }) => {
  changeColor.style.backgroundColor = color;
});

// When the button is clicked, inject setPageBackgroundColor into current page
changeColor.addEventListener("click", async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: fuction_alert,
    });
  });
  
  // The body of this function will be executed as a content script inside the
  // current page

  function fuction_alert(){
    links = document.links;
    for (var i = 0; i < links.length; i++){
      let tmp = links[i].toString()
      if (tmp.includes("doi.org/")){
        let store_link = links[i].getAttribute("href");
        console.log(store_link);
        let newURL = "https://sci-hub.se/"+store_link;
        chrome.tabs.create({ url: newURL });
        break
      }
    }
  }

  chrome.browserAction.onClicked.addListener(function(activeTab)
{
    var newURL = "http://www.youtube.com/watch?v=oHg5SJYRHA0";
    chrome.tabs.create({ url: newURL });
});
