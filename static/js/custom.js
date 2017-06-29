d3.json("/api/data/data.json", function(error, json) {
    if (error) return console.log(error);
    d3.select("#vis").append("svg")
      .data(json)
      .text(function(d){
          return d.MovieName;
      });
});
var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status == 200) {
        callback(null, xhr.response);
      } else {
        callback(status);
      }
    };
    xhr.send();
};
getJSON('/api/data/data.json',
function(err, data) {
  if (err != null) {
    alert('Something went wrong: ' + err);
  } else {
    window.data = data; // For debugging
    document.getElementById("entryamount").innerHTML = data.length;
    
  }
});