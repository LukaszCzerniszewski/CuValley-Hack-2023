if ($("#water-state")) {
    var start = moment().subtract(1, "days");
    var end = moment().subtract(1, "days");
    var cb = function(start, end) {
      $("#water-state .date-range-report span").html(
        start.format("ll") + " - " + end.format("ll")
      );
    };

  
    $("#water-state .date-range-report").daterangepicker(
      {
        startDate: start,
        endDate: end,
        opens: 'left',
        ranges: {
          Today: [moment(), moment()],
          Yesterday: [
            moment().subtract(1, "days"),
            moment().subtract(1, "days")
          ],
          "Last 7 Days": [moment().subtract(6, "days"), moment()],
          "Last 30 Days": [moment().subtract(29, "days"), moment()],
          "This Month": [moment().startOf("month"), moment().endOf("month")],
          "Last Month": [
            moment()
              .subtract(1, "month")
              .startOf("month"),
            moment()
              .subtract(1, "month")
              .endOf("month")
          ]
        }
      },
      cb
    );
    cb(start, end);
  }





/*======== 16. ANALYTICS - ACTIVITY CHART ========*/
var activity = document.getElementById("activity");
if (activity !== null) {
  var activityData = [
    {
      first: result,
      second: [600,600,600,600,600,600,600],
      third: [400,400,400,400,400,400,400,400],
      fourth: [333,333,333,333,333,333,333],
      fifth: [147,147,147,147,147,147,147]
    }
  ]
  // document.addEventListener('calendarReady', function() {
  //   let startDate = calendar.getStartDate();
  //   let endDate = calendar.getEndDate();
  // });
  // let labels=[]
  // for (let date = startDate; date <= endDate; date.setDate(date.getDate() + 1)) {
  //   let label = getLabelForDate(date);
  //   setLabelForDate(date, label);
  //   labels.push(label);
  // }
  // function callRainfall() {
  //   $.ajax({
  //     url:'/api/get-rainfall',
  //     type: 'GET',
  //     success: function(response) {
  //       console.log(respone)
  //     }
  //   });
  // }
  var config = {
    // The type of chart we want to create
    type: "line",
    // The data for our dataset
    data: {
      labels: [
        "4 Jan",
               "5 Jan",
                "6 Jan",
                "7 Jan",
                "8 Jan",
                "9 Jan",
                "10 Jan"
      ],
      datasets: [
        {
          label: "Trend",
          backgroundColor: "transparent",
          borderColor: "rgb(0,204,0)",
          data: activityData[0].first,
          lineTension: 0,
          pointRadius: 5,
          pointBackgroundColor: "rgba(255,255,255,1)",
          pointHoverBackgroundColor: "rgba(255,255,255,1)",
          pointBorderWidth: 2,
          pointHoverRadius: 7,
          pointHoverBorderWidth: 1
        },
        {
          label: "Alarm state",
          backgroundColor: "transparent",
          borderColor: "rgb(255, 0, 0)",
          data: activityData[0].second,
          lineTension: 0,
          borderWidth: 5,
          pointRadius: 0,
          pointBorderWidth: 5,
          pointHoverRadius: 0,
          pointHoverBorderWidth: 5
         
        },
        {
            label: "Warning state",
            backgroundColor: "transparent",
            borderColor: "rgb(255, 128, 0)",
            data: activityData[0].third,
            lineTension: 0,
          borderWidth: 5,
          pointRadius: 0,
          pointBorderWidth: 5,
          pointHoverRadius: 0,
          pointHoverBorderWidth: 5
          },
          {
            label: "Low state",
            backgroundColor: "transparent",
            borderColor: "rgb(51, 153, 255)",
            data: activityData[0].fourth,
            lineTension: 0,
          borderWidth: 5,
          pointRadius: 0,
          pointBorderWidth: 5,
          pointHoverRadius: 0,
          pointHoverBorderWidth: 5
          },
          {
            label: "High state",
            backgroundColor: "transparent",
            borderColor: "rgb(255, 255, 0)",
            data: activityData[0].fifth,
            lineTension: 0,
            borderWidth: 5,
            pointRadius: 0,
            pointBorderWidth: 5,
            pointHoverRadius: 0,
            pointHoverBorderWidth: 5
          }
      ]
    },
    
    // Configuration options go here
    options: {
      responsive: true,
      maintainAspectRatio: false,
      legend: {
        display: true,
        position: 'top'
      },
      scales: {
        xAxes: [
          {
            gridLines: {
              display: false,
            },
            ticks: {
              fontColor: "#8a909d", // this here
            },
          }
        ],
        yAxes: [
          {
            gridLines: {
              fontColor: "#8a909d",
              fontFamily: "Roboto, sans-serif",
              display: true,
              color: "#eee",
              zeroLineColor: "#eee"
            },
            ticks: {
              // callback: function(tick, index, array) {
              //   return (index % 2) ? "" : tick;
              // }
              stepSize: 50,
              fontColor: "#8a909d",
              fontFamily: "Roboto, sans-serif"
            }
          }
        ]
      },
      tooltips: {
        mode: "index",
        intersect: false,
        titleFontColor: "#888",
        bodyFontColor: "#555",
        titleFontSize: 12,
        bodyFontSize: 15,
        backgroundColor: "rgba(256,256,256,0.95)",
        displayColors: true,
        xPadding: 10,
        yPadding: 7,
        borderColor: "rgba(220, 220, 220, 0.9)",
        borderWidth: 2,
        caretSize: 6,
        caretPadding: 5
      }
    }
  };

  var ctx = document.getElementById("activity").getContext("2d");
  var myLine = new Chart(ctx, config);

  var items = document.querySelectorAll("#water-state .nav-tabs .nav-item");
  items.forEach(function(item, index){
    item.addEventListener("click", function() {
      config.data.datasets[0].data = activityData[index].first;
      config.data.datasets[1].data = activityData[index].second;
      config.data.datasets[2].data = activityData[index].third;
      config.data.datasets[3].data = activityData[index].fourth;
      config.data.datasets[4].data = activityData[index].fifth;
      myLine.update();
    });
  });
}