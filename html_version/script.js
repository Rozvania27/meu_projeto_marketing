document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('marketingChart').getContext('2d');

    // Inicialização do Gráfico com Chart.js
    const marketingChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['B2B Enterprise', 'E-commerce Retail', 'SaaS Self-Service'],
            datasets: [
                {
                    label: 'Abertura (%)',
                    data: [28.5, 22.1, 24.8],
                    backgroundColor: '#4f46e5'
                },
                {
                    label: 'CTR (%)',
                    data: [14.2, 10.5, 12.8],
                    backgroundColor: '#06b6d4'
                },
                {
                    label: 'Conversão (%)',
                    data: [4.5, 3.1, 3.9],
                    backgroundColor: '#10b981'
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 35
                }
            }
        }
    });

    // Simulação interativa simples dos checkboxes
    const checkboxes = document.querySelectorAll('.filter-check');
    checkboxes.forEach(chk => {
        chk.addEventListener('change', () => {
            // Atualiza os cards estáticos para demonstrar reatividade visual
            const activeCount = Array.from(checkboxes).filter(c => c.checked).length;
            document.getElementById('kpi-total').innerText = (activeCount * 333).toLocaleString();
        });
    });
});