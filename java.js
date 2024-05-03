// path -- string specifying URL to which data request is sent
// callback -- function called by JavaScript when response is recieved
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

// path -- string specifying URL to ywhich data request is sent
// data -- JSON blob being sent to the server
// callback -- function called by JavaScript when response is received
function ajaxPostRequest(path, data, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
      callback(this.response);
    }
  };
  request.open("POST", path);
  request.send(data);
}

function getData(){
  ajaxGetRequest("/pie_chart", showPieChart);
  ajaxGetRequest("/line_graph", showLineGraph);
  ajaxPostRequest("/line_graph2", PostLineGraph);
}


function showLineGraph(lineGraph){
  let response = JSON.parse(lineGraph);
  let data = [{
    x: Object.keys(response),
    y: Object.values(response),
    type: "scatter"
  }];
  let layout = {
    title: "Deaths By Date",
    xaxis: { title: "Year"},
    yaxis: { title: "# of Deaths"}
  };
  Plotly.newPlot("line_graph", data, layout);
}


function showPieChart(pieChart) {
  let response = JSON.parse(pieChart);
  let data = [{
    x: Object.values(response),
    labels: Object.keys(response),
    type: "pie"
  }];
  let layout = {
    height: 400,
    width: 500
  };
  Plotly.newPlot("pie_chart", data, layout);
}


function PostLineGraph(lineGraph){
  let response = JSON.parse(lineGraph);
  let data = [{
    x: Object.keys(response),
    y: Object.values(response),
    type: "scatter"
  }];
  let layout = {
    title: "Deaths By Date",
    xaxis: { title: "Year"},
    yaxis: { title: "# of Deaths"}
  };
}
Plotly.newPlot("line_graph2", data, layout);

