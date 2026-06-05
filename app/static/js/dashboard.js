
// GRÁFICO DE PIZZA


const pizza = document.getElementById("graficoPizza");

new Chart(pizza, {
    type: "pie",

    data: {
        labels: [
            "Entradas",
            "Saídas",
            "Cofre"
        ],

        datasets: [{
            data: [
                6000,
                1200,
                300
            ]
        }]
    },

    options: {
        responsive: true
    }
});


// GRÁFICO DE LINHA

const linha = document.getElementById("graficoLinha");

new Chart(linha, {
    type: "line",

    data: {
        labels: [
            "Jan",
            "Fev",
            "Mar",
            "Abr",
            "Mai",
            "Jun"
        ],

        datasets: [{
            label: "Saldo Mensal",

            data: [
                1000,
                2500,
                1800,
                4000,
                3700,
                4500
            ],

            tension: 0.4
        }]
    },

    options: {
        responsive: true
    }
});