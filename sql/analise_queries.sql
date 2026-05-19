-- 1. Quais linhas de produção têm maior taxa de defeito?
SELECT 
    l.nome_linha,
    COUNT(i.id_inspecao) as total_inspecoes,
    SUM(CASE WHEN i.status = 'Defeituoso' THEN 1 ELSE 0 END) as total_defeitos,
    ROUND(CAST(SUM(CASE WHEN i.status = 'Defeituoso' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(i.id_inspecao) * 100, 2) as taxa_defeito_percent
FROM inspecoes i
JOIN linhas l ON i.id_linha = l.id_linha
GROUP BY l.nome_linha
ORDER BY taxa_defeito_percent DESC;

-- 2. Os defeitos aumentaram ou diminuíram nos últimos meses?
SELECT 
    strftime('%Y-%m', data) as mes,
    COUNT(*) as total_inspecoes,
    SUM(CASE WHEN status = 'Defeituoso' THEN 1 ELSE 0 END) as total_defeitos
FROM inspecoes
GROUP BY mes
ORDER BY mes;

-- 3. Quais tipos de defeito são mais frequentes por turno?
SELECT 
    turno,
    tipo_defeito,
    COUNT(*) as frequencia
FROM inspecoes
WHERE status = 'Defeituoso'
GROUP BY turno, tipo_defeito
ORDER BY turno, frequencia DESC;

-- 4. Qual período do dia concentra mais não conformidades?
SELECT 
    turno,
    COUNT(*) as total_defeitos
FROM inspecoes
WHERE status = 'Defeituoso'
GROUP BY turno
ORDER BY total_defeitos DESC;

-- 5. Qual o custo estimado de retrabalho por linha?
SELECT 
    l.nome_linha,
    SUM(p.custo_unitario_retrabalho) as custo_total_retrabalho
FROM inspecoes i
JOIN produtos p ON i.id_produto = p.id_produto
JOIN linhas l ON i.id_linha = l.id_linha
WHERE i.status = 'Defeituoso'
GROUP BY l.nome_linha
ORDER BY custo_total_retrabalho DESC;
