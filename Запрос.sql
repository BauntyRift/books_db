select distinct  b.title, s.name as shop_name, sa.price, sa.date_sale
FROM sales sa
JOIN stocks st ON sa.id_stock = st.id
JOIN books b ON st.id_book = b.id
JOIN shops s ON st.id_shop = s.id
ORDER BY sa.date_sale DESC;
