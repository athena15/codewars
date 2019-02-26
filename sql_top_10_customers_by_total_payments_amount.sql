--    https://www.codewars.com/kata/sql-basics-top-10-customers-by-total-payments-amount/train/sql

--    Overview
--
--    For this kata we will be using the DVD Rental database.
--
--    Your are working for a company that wants to reward its top 10 customers with a free gift. You have been asked to generate a simple report that returns the top 10 customers by total amount spent. Total number of payments has also been requested.
--
--    The query should output the following columns:
--
--        customer_id [int4]
--        email [varchar]
--        payments_count [int]
--        total_amount [float]
--
--    and has the following requirements:
--
--        only returns the 10 top customers, ordered by total amount spent

-- Replace with your query (in pure SQL)
SELECT c.customer_id, c.email, COUNT(c.customer_id) as payments_count, CAST(SUM(p.amount) AS FLOAT) as total_amount
FROM payment p
JOIN customer c
ON p.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_amount DESC
LIMIT 10;