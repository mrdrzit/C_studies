chrome.runtime.onMessage.addListener(function(message){
  if (message){
     chrome.tabs.create({ url: message });
  }
});

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: {tabId: tab.id},
    files: ['tabify.js']
  });
});
