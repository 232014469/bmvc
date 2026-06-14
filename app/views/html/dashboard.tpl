<!DOCTYPE html>
<html lang="pt-BR">

<head>

    <meta charset="UTF-8">

    <title>Dashboard Financeiro</title>

    <link rel="stylesheet" href="/static/css/dashboard.css">

</head>

<body>

    <div class="topbar">

        <h1>Controle Financeiro</h1>

        <a href="/logout" class="btn-logout">
            Sair
        </a>

    </div>

    <!-- PRIMEIRA LINHA -->
    <div class="dashboard">

        <!-- ENTRADAS -->
        <div class="card entradas">

            <h2>Entradas</h2>

            <p>Cadastre novas receitas.</p>

            <a href="/entradas">
                Nova Entrada
            </a>

        </div>

        <!-- SALDO -->
        <div class="card resumo">

            <h2>Saldo Atual</h2>

            <h1>R$ {{saldo}}</h1>

            <canvas id="graficoPizza"></canvas>

        </div>

        <!-- SAÍDAS -->
        <div class="card saidas">

            <h2>Saídas</h2>

            <p>Cadastre seus gastos.</p>

            <a href="/saidas">
                Nova Saída
            </a>

        </div>

    </div>

    <!-- SEGUNDA LINHA -->
    <div class="bottom-row">

        <!-- GRÁFICO -->
        <div class="card grafico">

            <h2>Gráfico Financeiro</h2>

            <canvas id="graficoLinha"></canvas>

        </div>

        <!-- ÚLTIMAS TRANSAÇÕES -->
        <div class="card gastos">

            <h2>Últimas Transações</h2>

            <ul>

                % for t in transacoes:

                <li>
                    <strong>{{t["tipo"]}}</strong>
                    -
                    {{t["descricao"]}}
                    -
                    R$ {{t["valor"]}}
                </li>

                % end

            </ul>

            <a href="/transacoes">
                Ver Todas
            </a>

        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script src="/static/js/dashboard.js"></script>

</body>

</html>