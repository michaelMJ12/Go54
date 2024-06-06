$(function () {
  "use strict";

  // Get initial student data from the script tag
  var initialStudentData = JSON.parse(
    document.getElementById("students-data").textContent
  );

  // Function to transform student data into monthly format
  function transformStudentData(data) {
    let transformedData = {
      months: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
      ],
      counts: new Array(12).fill(0),
    };

    Object.keys(data).forEach((month) => {
      let index = transformedData.months.indexOf(month);
      if (index !== -1) {
        transformedData.counts[index] = data[month];
      }
    });

    return transformedData;
  }

  // Function to initialize the bar chart
  function initializeBarChart(studentData) {
    // Transform data
    let { months, counts } = transformStudentData(studentData);

    // Check if there is any data to display
    if (!counts || counts.length === 0 || counts.every((item) => item === 0)) {
      console.log("No data available to display on the chart.");
      return; // Exit the function if there is no data
    }

    // Initialize the chart if there is data
    var chart2 = new Chartist.Bar(
      ".amp-pxl",
      {
        labels: months,
        series: [counts],
      },
      {
        axisX: {
          position: "end",
          showGrid: false,
        },
        axisY: {
          position: "start",
        },
        high: Math.max(...counts), // Set the highest value dynamically
        low: 0,
        plugins: [Chartist.plugins.tooltip()],
      }
    );

    // Animation
    chart2.on("draw", function (data) {
      if (data.type === "line" || data.type === "area") {
        data.element.animate({
          d: {
            begin: 500 * data.index,
            dur: 500,
            from: data.path
              .clone()
              .scale(1, 0)
              .translate(0, data.chartRect.height())
              .stringify(),
            to: data.path.clone().stringify(),
            easing: Chartist.Svg.Easing.easeInOutElastic,
          },
        });
      }
      if (data.type === "bar") {
        data.element.animate({
          y2: {
            dur: 500,
            from: data.y1,
            to: data.y2,
            easing: Chartist.Svg.Easing.easeInOutElastic,
          },
          opacity: {
            dur: 500,
            from: 0,
            to: 1,
            easing: Chartist.Svg.Easing.easeInOutElastic,
          },
        });
      }
    });
  }

  // Function to initialize the pie chart
  function initializePieChart(studentData) {
    // Convert student data to pie chart format
    var pieData = Object.entries(studentData);

    // Check if there is any data to display
    if (
      !pieData ||
      pieData.length === 0 ||
      pieData.every((item) => item[1] === 0)
    ) {
      console.log("No data available to display on the pie chart.");
      return; // Exit the function if there is no data
    }

    // Initialize the pie chart if there is data
    var chart = c3.generate({
      bindto: "#visitor",
      data: {
        columns: pieData,
        type: "pie",
      },
      legend: {
        show: true,
      },
      color: {
        pattern: [
          "#745af2",
          "#26c6da",
          "#1e88e5",
          "#ff9800",
          "#4caf50",
          "#f44336",
          "#9c27b0",
          "#ff5722",
          "#607d8b",
          "#795548",
          "#e91e63",
          "#00bcd4",
        ],
      },
    });
  }

  // Initialize charts with initial data
  initializeBarChart(initialStudentData);
  initializePieChart(initialStudentData);

  // Function to update charts with new data
  function updateCharts() {
    $.ajax({
      url: dashboardUrl, // Use Django's url template tag to generate the URL
      method: "GET",
      success: function (data) {
        // Convert data into an array format for compatibility
        var studentData = data;

        // Initialize and render the bar chart
        initializeBarChart(studentData);

        // Initialize and render the pie chart
        initializePieChart(studentData);
      },
      error: function (error) {
        console.error("Error:", error);
      },
    });
  }

  // Check for updates periodically or based on a specific trigger
  setInterval(updateCharts, 60000); // Check for updates every 60 seconds
});
