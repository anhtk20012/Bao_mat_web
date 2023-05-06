const convertBtn =  document.getElementById("convert-button");
const webFrameContainer =  document.getElementById("web-frame-container");
const webFrame =  document.getElementById("web-destination-frame");


convertBtn.addEventListener("click", (e) => {
  e.preventDefault()
  const urlDestination = document.getElementById('url-destination').value;
  webFrameContainer.innerHTML = `
    <iframe src="${urlDestination}"></iframe>
  `
})