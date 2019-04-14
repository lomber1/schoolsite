var lineChartWeek = $("#usersThisWeekChart");
var lineChartMonth = $("#usersThisMonthChart");

// var colors = [, '#28a745', '#057bff', 'hsl(211, 100% , 85% )', '#dc3545', '#6c757d'];
var colors = {
    backgroundColor: "hsl(211, 100%, 85%)",
    borderColor: '#007bff',
    pointBackgroundColor: "#007bff"
}

var weekData = {
    labels: ["Pn.", "Wt.", "Śr.", "Czw.", "Pt.", "Sob.", "Niedz."],
    datasets: [
        {
            data: Array.from({length: 7}, () => Math.floor(Math.random() * 40)),
            backgroundColor: colors["backgroundColor"],
            borderColor: colors["borderColor"],
            borderWidth: 3,
            pointBackgroundColor: colors["pointBackgroundColor"]
        }
    ]
};

var labels = [31];

for (let i = 0; i < 31; i++) {
    labels[i] = i+1;
}

var monthData = {
    labels: labels,
    datasets: [{
        data: Array.from({
            length: 31
        }, () => Math.floor(Math.random() * 40)),
        backgroundColor: colors["backgroundColor"],
        borderColor: colors["borderColor"],
        borderWidth: 3,
        pointBackgroundColor: colors["pointBackgroundColor"]
    }]
};

if (lineChartWeek) {
    new Chart(lineChartWeek, {
        type: "line",
        data: weekData,
        options: {
            legend: {
                display: false
            },
        }
    });
}

if (lineChartMonth) {
    new Chart(lineChartMonth, {
        type: "line",
        data: monthData,
        options: {
            legend: {
                display: false
            },
        }
    });
}