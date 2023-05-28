function showReport() {
    var date1Input = document.getElementById("date1");
    var date2Input = document.getElementById("date2");

    var date1Value = date1Input.value;
    var date2Value = date2Input.value;

    console.log("Date 1:", date1Value);
    console.log("Date 2:", date2Value);

    fetch("/api/order_endpoint")
        .then(res => res.json())
        .then(res => {
            console.log(res);
            var reportElement = document.getElementById("report");
            reportElement.innerHTML = "";

            var paragraphInfo = document.createElement("p");
            paragraphInfo.textContent = "This report contains all orders form " + date1Value + " to " + date2Value + ".";
            reportElement.appendChild(paragraphInfo);
            reportElement.classList.toggle("show");

            buttonDescriptionElement = document.getElementById("buttonDescription")
            buttonDescriptionElement.textContent = reportElement.classList.contains("show") ? "Hide" : "Submit";
        })
}