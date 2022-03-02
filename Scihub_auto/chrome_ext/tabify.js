links = document.links;
for (var i = 0; i < links.length; i++) {
    let tmp = links[i].toString()
    if (tmp.includes("doi.org/")) {
    let store_link = links[i].getAttribute("href");
    console.log(store_link);
    let newURL = "https://sci-hub.se/" + store_link;
    chrome.runtime.sendMessage(newURL);
    break
    }
}