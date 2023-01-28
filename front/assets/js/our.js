var selected_STATIONCODE = "151160060";
var startDate = "30/09/2012";
var endDate = "30/10/2012";
let select = document.getElementById("dropdown");
let selectedOption = select.options[select.selectedIndex].value;

var second=600
var third=400
var fourth=333
var fifth=147

function changeaa() {
  selectedOption = select.options[select.selectedIndex].value;
  if(selectedOption=="150180060"){
    second=600
    third=400
    fourth=333
    fifth=147
  }
  if(selectedOption=="151160060"){
      second=450
      third=400
      fourth=247
      fifth=148
  }
}


function datefor(today) {
  const yyyy = today.getFullYear();
  let mm = today.getMonth() + 1; // Months start at 0!
  let dd = today.getDate();

  if (dd < 10) dd = '0' + dd;
  if (mm < 10) mm = '0' + mm;

  const formattedToday = dd + '/' + mm + '/' + yyyy;

  return formattedToday;
}

var start = moment(startDate, 'DD-MM-YYYY').subtract(1, "days");
var end = moment(endDate, 'DD-MM-YYYY').subtract(7, "days");
var cb = function(start, end) {
  startDate = datefor(new Date(start));
  endDate = datefor(new Date(end));
  $("#water-state .date-range-report span").html(
    start.format("ll") + " - " + end.format("ll")
  );
  request_data();
  changeaa();
  config.data.labels = [];
  dd = [];
  dd1 = [];
  dd2 = [];
  dd3 = [];
  for (let i = 0; i < res.length; i++) {
    config.data.labels.push(moment(startDate, 'DD-MM-YYYY').subtract(i, "days").format("ll"));
    dd.push(second);
    dd1.push(third);
    dd2.push(fourth);
    dd3.push(fifth);
  }
  config.data.labels = config.data.labels.reverse();
  config.data.datasets[0].data = res;
  config.data.datasets[1].data = dd;
  config.data.datasets[2].data = dd1;
  config.data.datasets[3].data = dd2;
  config.data.datasets[4].data = dd3;
  myLine.destroy();
  myLine = new Chart(ctx, config);
  // redraw();
};

$("#user-activity .date-range-report").daterangepicker(
  {
    startDate: start,
    endDate: end,
    opens: 'left',
    // ranges: {
    //   Today: [moment(), moment()],
    //   Yesterday: [
    //     moment().subtract(1, "days"),
    //     moment().subtract(1, "days")
    //   ],
    //   "Last 7 Days": [moment().subtract(6, "days"), moment()],
    //   "Last 30 Days": [moment().subtract(29, "days"), moment()],
    //   "This Month": [moment().startOf("month"), moment().endOf("month")],
    //   "Last Month": [
    //     moment()
    //       .subtract(1, "month")
    //       .startOf("month"),
    //     moment()
    //       .subtract(1, "month")
    //       .endOf("month")
    //   ]
    // }
  },
  cb
);

$("#dropdown").on('change', function() {
  selected_STATIONCODE = this.value;
  request_data();
  changeaa();
  config.data.labels = [];
  dd = [];
  dd1 = [];
  dd2 = [];
  dd3 = [];
  for (let i = 0; i < res.length; i++) {
    config.data.labels.push(moment(startDate, 'DD-MM-YYYY').subtract(i, "days").format("ll"));
    dd.push(second);
    dd1.push(third);
    dd2.push(fourth);
    dd3.push(fifth);
  }
  config.data.labels = config.data.labels.reverse();
  config.data.datasets[0].data = res;
  config.data.datasets[1].data = dd;
  config.data.datasets[2].data = dd1;
  config.data.datasets[3].data = dd2;
  config.data.datasets[4].data = dd3;
  myLine.destroy();
  myLine = new Chart(ctx, config);

  moment(startDate, 'DD-MM-YYYY').subtract(1, "days");
  // redraw();
});

var res = [];

function request_data() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    res = JSON.parse(this.responseText);
  }
  
  xhttp.open("POST", "/api/get_waterstates", false);
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.setRequestHeader("kkey_y", "c9f53a7a0657ed8769098ad48074709cbd0bf0ad83e41e67164a9316605b86b0bdd81f0b16fd8b1a4a3dc7c0194f9bcb50cc29c16bfd73ef42c07e81b35026ef");
  xhttp.send(JSON.stringify({
    "STATIONCODE": selected_STATIONCODE,
    "DDATE_FROM": startDate,
    "DDATE_TO": endDate
  }));
}
request_data();

var activity = document.getElementById("activity");
if (activity !== null) {
  var activityData = [
    {
      first: res,
      second: [],
      third: []
    }
  ]
  var config = {
    // The type of chart we want to create
    type: "line",
    // The data for our dataset
    data: {
      labels: [],
      datasets: [
        {
          label: "Trend",
          backgroundColor: "transparent",
          borderColor: "rgb(0,204,0)",
          data: res,
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

  // function redraw() {
  //   var items = document.querySelectorAll("#water-state .nav-tabs .nav-item");
  //   items.forEach(function(item, index){
  //     item.addEventListener("click", function() {
  //       config.data.datasets[0].data = activityData[index].first;
  //       config.data.datasets[1].data = activityData[index].second;
  //       config.data.datasets[2].data = activityData[index].third;
  //       config.data.datasets[3].data = activityData[index].fourth;
  //       config.data.datasets[4].data = activityData[index].fifth;
  //       myLine.update();
  //     });
  //   });
  // }
  // redraw();

  cb(start, end);
}