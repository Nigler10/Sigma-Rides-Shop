console.log("Javascript here")

document.getElementById("image").addEventListener("mouseover", function() {
    var gifPath = document.getElementById("gifPath").value;
    this.src = gifPath;
});

document.getElementById("image").addEventListener("mouseout", function() {
    var imagePath = document.getElementById("imagePath").value;
    this.src = imagePath;
});
