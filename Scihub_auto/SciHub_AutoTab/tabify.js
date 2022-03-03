var current_domain = window.location.hostname;

if (current_domain != "www.nature.com") {
    links = document.links;
    for (var i = 0; i < links.length; i++) {
        let tmp = links[i].toString()
        if (tmp.includes("doi.org/")) {
            let store_link = links[i].getAttribute("href")
            let newURL = "https://sci-hub.se/" + store_link
            chrome.runtime.sendMessage(newURL);
            break
        }
    }
} else {
    let links = document.getElementsByClassName("c-bibliographic-information__value");
    for (var i = 0; i < links.length; i++) {
        let tmp = links[i].innerHTML
        if (tmp.includes("doi.org")) {
            let store_link = links[i].innerHTML
            let newURL = "https://sci-hub.se/" + store_link
            chrome.runtime.sendMessage(newURL);
            break
        }
    }
}