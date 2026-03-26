SELECT 
	sq.f AS id, 
	COUNT(DISTINCT sq.t) AS num
FROM (
    SELECT requester_id AS f, accepter_id AS t FROM requestaccepted
    UNION ALL
    SELECT accepter_id AS f, requester_id AS t FROM requestaccepted
) AS sq
GROUP BY sq.f
ORDER BY num DESC
LIMIT 1;
