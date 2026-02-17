-- Count how many reviews you inserted
SELECT COUNT(*) FROM reviews;
-- Count how many reviews per bank
SELECT b.bank_name, COUNT(r.review_id) AS total_reviews
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
ORDER BY total_reviews DESC;
-- Check average rating per bank
SELECT b.bank_name, AVG(r.rating) AS avg_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
-- Check how many positive/negative/neutral
SELECT sentiment_label, COUNT(*) 
FROM reviews
GROUP BY sentiment_label;

