// $(function() {
//     "use strict";
    
//     var dataBar = {
//         labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
//         series: [
//             [9, 5, 3, 7, 5, 10, 3],
//             [6, 3, 9, 5, 4, 6, 4]
//         ]
//     };

    
//     var totalValuesBar = dataBar.series[0].map(function (_, colIndex) {
//         return dataBar.series.reduce(function (accumulator, series) {
//             return accumulator + series[colIndex];
//         }, 0);
//     });

//     var percentageSeriesBar = dataBar.series.map(function (series) {
//         return series.map(function (value, index) {
//             return ((value / totalValuesBar[index]) * 100).toFixed(2);
//         });
//     });

//     var chart2 = new Chartist.Bar('.amp-pxl', {
//         labels: dataBar.labels,
//         series: percentageSeriesBar
//     }, {
//         axisX: {
            
//             position: 'end',
//             showGrid: false
//         },
//         axisY: {
            
//             position: 'start',
//             labelInterpolationFnc: function(value) {
//                 return value + '%'; 
//             }
//         },
//         high: '100', 
//         low: '0',
//         plugins: [
//             Chartist.plugins.tooltip()
//         ]
//     });

    

//     chart2.on('draw', function(data) {
//         if (data.type === 'line' || data.type === 'area') {
//             data.element.animate({
//                 d: {
//                     begin: 500 * data.index,
//                     dur: 500,
//                     from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
//                     to: data.path.clone().stringify(),
//                     easing: Chartist.Svg.Easing.easeInOutElastic
//                 }
//             });
//         }
//         if (data.type === 'bar') {
//             data.element.animate({
//                 y2: {
//                     dur: 500,
//                     from: data.y1,
//                     to: data.y2,
//                     easing: Chartist.Svg.Easing.easeInOutElastic
//                 },
//                 opacity: {
//                     dur: 500,
//                     from: 0,
//                     to: 1,
//                     easing: Chartist.Svg.Easing.easeInOutElastic
//                 }
//             });
//         }
//     });

    

//     var dataPie = {
//         columns: [
//             ['Other', 30],
//             ['Desktop', 10],
//             ['Tablet', 40],
//             ['Mobile', 50],
//         ]
//     };

    
//     var totalValuesPie = dataPie.columns.slice(1).map(function (value) {
//         return parseFloat(value[1]);
//     }).reduce(function (sum, value) {
//         return sum + value;
//     }, 0);

//     var percentageDataPie = dataPie.columns.map(function (column, index) {
//         if (index === 0) {
//             return column;
//         }
//         var percentage = ((parseFloat(column[1]) / totalValuesPie) * 100).toFixed(2);
//         return [column[0] + ' (' + percentage + '%)', parseFloat(column[1])];
//     });

//     var chart = c3.generate({
//         bindto: '#visitor',
//         data: {
//             columns: percentageDataPie,
//             type: 'donut',
//             onclick: function(d, i) { console.log("onclick", d, i); },
//             onmouseover: function(d, i) { console.log("onmouseover", d, i); },
//             onmouseout: function(d, i) { console.log("onmouseout", d, i); }
//         },
//         donut: {
//             label: {
//                 show: false
//             },
//             title: "Our visitor",
//             width: 20,
//         },
//         legend: {
//             hide: true
//         },
//         color: {
//             pattern: ['#eceff1', '#745af2', '#26c6da', '#1e88e5']
//         }
//     });
// });
