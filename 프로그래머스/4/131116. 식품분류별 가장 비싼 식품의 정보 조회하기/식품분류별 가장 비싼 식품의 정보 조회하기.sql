-- 코드를 입력하세요

select category, price MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where category REGEXP '과자|국|김치|식용유' and price in ( SELECT max(price) 
             from FOOD_PRODUCT
             where category in ('과자', '국', '김치', '식용유')
             group by category)
 order by MAX_PRICE desc