queue()
.defer(d3.json, "/api/data/data.json")
.await(makeGraphs);

function makeGraphs(error, movieList) {
       
    var ndx = crossfilter(movieList);
    var genreDim = ndx.dimension(function (movieRecord){
        return movieRecord.Genre;
    });
    var moviesPerGenre = genreDim.group().reduceCount();

    
   var piechart = dc.pieChart("#pieChart");
   piechart
    .ordinalColors(["#F44336", "#3F51B5", "#2196F3", "#009688", "#FF5722", "#795548"])
    .height(250)
    .width(250)
    .radius(125)
    .innerRadius(40)
    .transitionDuration(1500)
    .dimension(genreDim)
    .group(moviesPerGenre);

  dc.renderAll(); 
}