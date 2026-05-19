-- 1. Which production lines have the highest defect rates?
SELECT 
    l.line_name,
    COUNT(i.inspection_id) as total_inspections,
    SUM(CASE WHEN i.status = 'Defective' THEN 1 ELSE 0 END) as total_defects,
    ROUND(CAST(SUM(CASE WHEN i.status = 'Defective' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(i.inspection_id) * 100, 2) as defect_rate_percent
FROM inspections i
JOIN lines l ON i.line_id = l.line_id
GROUP BY l.line_name
ORDER BY defect_rate_percent DESC;

-- 2. Are defects increasing or decreasing over time?
SELECT 
    strftime('%Y-%m', date) as month,
    COUNT(*) as total_inspections,
    SUM(CASE WHEN status = 'Defective' THEN 1 ELSE 0 END) as total_defects
FROM inspections
GROUP BY month
ORDER BY month;

-- 3. Which defect types are most frequent by shift?
SELECT 
    shift,
    defect_type,
    COUNT(*) as frequency
FROM inspections
WHERE status = 'Defective'
GROUP BY shift, defect_type
ORDER BY shift, frequency DESC;

-- 4. Which period of the day concentrates the most non-conformities?
SELECT 
    shift,
    COUNT(*) as total_defects
FROM inspections
WHERE status = 'Defective'
GROUP BY shift
ORDER BY total_defects DESC;

-- 5. What is the estimated rework cost per line?
SELECT 
    l.line_name,
    SUM(p.unit_rework_cost) as total_rework_cost
FROM inspections i
JOIN products p ON i.product_id = p.product_id
JOIN lines l ON i.line_id = l.line_id
WHERE i.status = 'Defective'
GROUP BY l.line_name
ORDER BY total_rework_cost DESC;
