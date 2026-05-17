SELECT 
    user_id,
    ROUND(AVG(activity_duration) FILTER (WHERE activity_type = 'free_trial'), 2) AS trial_avg_duration,
    ROUND(AVG(activity_duration) FILTER (WHERE activity_type = 'paid'), 2) AS paid_avg_duration
FROM useractivity m
WHERE EXISTS (
    SELECT 1 
    FROM useractivity s 
    WHERE m.user_id = s.user_id AND s.activity_type = 'paid'
)
GROUP BY user_id
ORDER BY user_id;
