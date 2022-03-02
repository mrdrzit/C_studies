chrome.runtime.onMessage.addListener(function(message){
  if (message){
     chrome.tabs.create({ url: message });
  }
});