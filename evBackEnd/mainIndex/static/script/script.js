
const labels = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'June',
  'July',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec'
];

const data = {
  labels: labels,
  datasets: [{
    label: 'Power Consumption From Grid (Monthly)',
    backgroundColor: 'rgb(202, 30, 139))',
    hoverBackgroundColor:'rgb(204, 75, 75)',
    pointHoverBorderWidth: 4,
    pointHoverRadius:8,
    tension:0.5,
    borderColor: 'rgb(202, 30, 139))',
    data: [0, 10, 5, 2, 20, 30, 45, 0, 0, 0, 0, 0, 0],
  }]
};

const config = {
  type: 'bar',
  data: data,
  options: {

  }
};

const mySolarChart = new Chart(
  document.getElementById('powerConsumptionGridMonthly'),
  config
  );

//-----------------------------------------------------------------//
//================= Power consumption Now =========================//
//-----------------------------------------------------------------//

const labelsLive = [
  {% for data in liveDataTime %}{{data}}, {% endfor %}
  ];

const dataLive = {
labels: labelsLive,
datasets: [{
  label: 'Power Consumption From Grid Live',
  backgroundColor: 'rgb(202, 30, 139))',
  hoverBackgroundColor:'rgb(204, 75, 75)',
  pointHoverBorderWidth: 4,
  pointHoverRadius:8,
  tension:0.5,
  borderColor: 'rgb(0, 200, 160)',
  data: [{% for data in liveDataPower %}{{data}}, {% endfor %}],
}]
};

const configLive = {
type: 'line',
data: dataLive,
options: {

}
};

const myLiveChart = new Chart(
document.getElementById('powerConsumptionfromGridLive'),
configLive
);


//-----------------------------------------------------------------//
//================= Power consumption Now =========================//
//-----------------------------------------------------------------//