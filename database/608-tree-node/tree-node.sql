SELECT 
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN NOT EXISTS (SELECT 1 FROM tree AS sub WHERE main.id = sub.p_id) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM tree AS main;
