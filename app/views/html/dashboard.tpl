<!DOCTYPE html>
<html>

<head>

    <title>Dashboard</title>

    <link rel="stylesheet" href="/static/css/dashboard.css">

</head>

<body>

    <div class="topbar">

        <h1>Controle Financeiro</h1>

        <a href="/logout" class="btn-logout">
            Sair
        </a>

    </div>

    <div class="dashboard">

        <!-- Entradas -->

        <div class="card entradas">

            <h2>Entradas</h2>

            <p>Cadastre novas receitas.</p>

            <a href="/entradas">
                Nova Entrada
            </a>

        </div>

        <!-- Saldo -->

        <div class="card resumo">

            <h2>Saldo Atual</h2>

            <h1>R$ {{saldo}}</h1>

            <canvas id="graficoPizza"></canvas>

        </div>

        <!-- Saídas -->

        <div class="card saidas">

            <h2>Saídas</h2>

            <p>Cadastre seus gastos.</p>

            <a href="/saidas">
                Nova Saída
            </a>

        </div>

        <!-- Saídas Fixas -->

        <div class="card fixas">

            <h2>Saídas Fixas</h2>

            <p>Contas recorrentes.</p>

            <a href="/fixas">
                Gerenciar
            </a>

        </div>

        <!-- Gráfico -->

        <div class="card grafico">

            <h2>Gráfico Financeiro</h2>

            <canvas id="graficoLinha"></canvas>

        </div>

        <!-- Transações -->

        <div class="card gastos">

            <h2>Últimas Transações</h2>

            <ul>

            % for t in transacoes:

                <li>

                    {{t["tipo"]}}
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

        <!-- Cofre -->

        <div class="card cofre">

            <h2>Cofre</h2>

            <p>Reserva financeira.</p>

            <a href="/cofre">
                Acessar Cofre
            </a>

        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script src="/static/js/dashboard.js"></script>

</body>

</html>