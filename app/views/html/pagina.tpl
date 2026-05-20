<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FinanceControl | Gestão Pessoal</title>
    
    <!-- CSS vinculado via rota estática -->
    <link rel="stylesheet" type="text/css" href="/static/css/helper.css">
</head>
<body>

    <header>
        <h1>FinanceControl v1.0</h1>
        <p>Sua liberdade financeira começa aqui.</p>
    </header>

    <main class="container">
        <!-- Resumo de Saldo (Estilizado via CSS) -->
        <section class="dashboard">
            <div class="card balance">
                <h3>Saldo Atual</h3>
                <p id="saldo-valor">R$ 0,00</p>
            </div>
        </section>

        <!-- Formulário Simples (Propósito Claro) -->
        <section class="card">
            <h2>Adicionar Nova Transação</h2>
            <div class="form-group">
                <input type="text" id="descricao" placeholder="Ex: Aluguel, Salário...">
                <input type="number" id="valor" placeholder="R$ 0,00">
                <button id="btn-add" class="btn-success">Registrar</button>
            </div>
        </section>

        <!-- Área de Feedback (Para provar o JS ativo) -->
        <section id="lista-transacoes">
            <h3>Últimas Atividades</h3>
            <ul id="historico">
                <li>Nenhuma transação registrada.</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>jeffh@MacBook-Air &copy; 2026 - Sistema de Controle Financeiro BMVC</p>
    </footer>

    <!-- JS vinculado via rota estática -->
    <script src="/static/js/helper.js"></script>
</body>
</html>