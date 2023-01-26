var acquisition = document.getElementById("acquisition");
  if (acquisition !== null) {
    var acqData = [
      {
        first: [100, 180, 44, 75, 150, 66, 70],
        second: [144, 44, 177, 76, 23, 189, 12],
        third: [44, 167, 102, 123, 183, 88, 134]
      },
      {
        first: [144, 44, 110, 5, 123, 89, 12],
        second: [22, 123, 45, 130, 112, 54, 181],
        third: [55, 44, 144, 75, 155, 166, 70]
      },
      {
        first: [134, 80, 123, 65, 171, 33, 22],
        second: [44, 144, 77, 76, 123, 89, 112],
        third: [156, 23, 165, 88, 112, 54, 181]
      }
    ];

    var configAcq = {
      // The type of chart we want to create
      type: "line",

      // The data for our dataset
      data: {
        labels: [
          "4 kokoszka",
          "5 Jan",
          "6 Jan",
          "7 Jan",
          "8 Jan",
          "9 Jan",
          "10 Jan"
        ],
        datasets: [
          {
            label: "Referral",
            backgroundColor: "rgb(76, 132, 255)",
            borderColor: "rgba(76, 132, 255,0)",
            data: acqData[0].first,
            lineTension: 0.3,
            pointBackgroundColor: "rgba(76, 132, 255,0)",
            pointHoverBackgroundColor: "rgba(76, 132, 255,1)",
            pointHoverRadius: 3,
            pointHitRadius: 30,
            pointBorderWidth: 2,
            pointStyle: "rectRounded"
          },
          {
            label: "Direct",
            backgroundColor: "rgb(254, 196, 0)",
            borderColor: "rgba(254, 196, 0,0)",
            data: acqData[0].second,
            lineTension: 0.3,
            pointBackgroundColor: "rgba(254, 196, 0,0)",
            pointHoverBackgroundColor: "rgba(254, 196, 0,1)",
            pointHoverRadius: 3,
            pointHitRadius: 30,
            pointBorderWidth: 2,
            pointStyle: "rectRounded"
          },
          {
            label: "Social",
            backgroundColor: "rgb(41, 204, 151)",
            borderColor: "rgba(41, 204, 151,0)",
            data: acqData[0].third,
            lineTension: 0.3,
            pointBackgroundColor: "rgba(41, 204, 151,0)",
            pointHoverBackgroundColor: "rgba(41, 204, 151,1)",
            pointHoverRadius: 3,
            pointHitRadius: 30,
            pointBorderWidth: 2,
            pointStyle: "rectRounded"
          }
        ]
      },

      // Configuration options go here
      options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              gridLines: {
                display: false
              }
            }
          ],
          yAxes: [
            {
              gridLines: {
                display: true,
                color: "#eee",
                zeroLineColor: "#eee"
              },
              ticks: {
                beginAtZero: true,
                stepSize: 50,
                max: 200
              }
            }
          ]
        },
        tooltips: {
          mode: "index",
          titleFontColor: "#888",
          bodyFontColor: "#555",
          titleFontSize: 12,
          bodyFontSize: 15,
          backgroundColor: "rgba(256,256,256,0.95)",
          displayColors: true,
          xPadding: 20,
          yPadding: 10,
          borderColor: "rgba(220, 220, 220, 0.9)",
          borderWidth: 2,
          caretSize: 10,
          caretPadding: 15
        }
      }
    };

    var ctx = document.getElementById("acquisition").getContext("2d");
    var lineAcq = new Chart(ctx, configAcq);
    document.getElementById("acqLegend").innerHTML = lineAcq.generateLegend();

    var items = document.querySelectorAll(
      "#user-acquisition .nav-tabs .nav-item"
    );
    items.forEach(function (item, index) {
      item.addEventListener("click", function() {
        configAcq.data.datasets[0].data = acqData[index].first;
        configAcq.data.datasets[1].data = acqData[index].second;
        configAcq.data.datasets[2].data = acqData[index].third;
        lineAcq.update();
      });
    });
  }
