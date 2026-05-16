SELECT employee_id
FROM employees NATURAL FULL JOIN salaries
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id;
