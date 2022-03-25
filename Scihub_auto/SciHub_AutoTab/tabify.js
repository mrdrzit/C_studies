var current_domain = window.location.hostname;
var domains = ["sci-hub.st", "sci-hub.ru", "sci-hub.se", "sci-hub.ren", "sci-hub.nz", "sci-hub.cn", "sci-hub.hk", "sci-hub.tw", "sci-hub.ws", "sci-hub.org", "sci-hub.cc", "sci-hub.ac", "sci-hub.io", "sci-hub.mn", "sci-hub.tv", "sci-hub.biz", "sci-hub.is", "sci-hub.nu", "sci-hub.ga", "sci-hub.gq"];


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

//TODO #4

// *EXAMPLE OF DOMAIN ERROR HANDLING USING PYTHON* \\

// import requests
// import os

// os.system('cls')

// s = ["sci-hub.st", "sci-hub.ru", "sci-hub.se", "sci-hub.ren", "sci-hub.nz", "sci-hub.cn", "sci-hub.hk", "sci-hub.tw", "sci-hub.ws",
//      "sci-hub.org", "sci-hub.cc", "sci-hub.ac", "sci-hub.io", "sci-hub.mn", "sci-hub.tv", "sci-hub.biz", "sci-hub.is", "sci-hub.nu", "sci-hub.ga", "sci-hub.gq"]
// with requests.Session() as req:
//   for r in range(0, len(s)):
//     try:
//       secure = req.get("https://" + s[r])
//     except:
//       print("The domain " + str(s[r]) + " doesn't work!")
//       continue

//     if secure.status_code == 200:
//       print("The domain " + str(s[r]) + " works!")
//     else:
//       print("The domain " + str(s[r]) + " doesn't work!")