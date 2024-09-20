# 해당 기간을 포함하는 자동차 id를 제외하자


# select car_id
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where 
#     date_format(start_date, '%Y-%m-%d') between '2022-11-01' and '2022-11-30' or
#     date_format(end_date, '%Y-%m-%d') between '2022-11-01' and '2022-11-30' or
#     (date_format(start_date, '%Y-%m-%d') <= '2022-11-01' and date_format(start_date, '%Y-%m-%d') >= '2022-11-30'
#     )


select A.CAR_ID, A.car_type, ROUND((A.daily_fee * 30) * (1- (B.DISCOUNT_RATE/100))) FEE
from CAR_RENTAL_COMPANY_CAR A
left join (
            select CAR_TYPE, DISCOUNT_RATE from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
            where duration_type like '%30일%'
          ) B on A.CAR_TYPE = B.CAR_TYPE
where car_id not in (select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where 
    date_format(start_date, '%Y-%m-%d') between '2022-11-01' and '2022-11-30' or
    date_format(end_date, '%Y-%m-%d') between '2022-11-01' and '2022-11-30' or
    (date_format(start_date, '%Y-%m-%d') <= '2022-11-01' and date_format(end_date, '%Y-%m-%d') >= '2022-11-30'
    ))
    and A.car_type REGEXP '세단|SUV' and
    ( ROUND((A.daily_fee * 30) * (1- (B.DISCOUNT_RATE/100))) >= 500000 and
        ROUND((A.daily_fee * 30) * (1- (B.DISCOUNT_RATE/100))) <= 2000000 )
order by fee desc, car_type, car_id desc 

# SELECT a.car_id,a.CAR_TYPE,ROUND(a.DAILY_FEE * 30 * (100 - b.DISCOUNT_RATE) / 100, 0) AS FEE
# FROM CAR_RENTAL_COMPANY_CAR as a join 
# (select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where DURATION_TYPE ='30일 이상') b 
# on a.CAR_TYPE=b.CAR_TYPE
# where a.CAR_TYPE in ('세단','suv')
# and a.car_id not in (
#     select car_id
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     where END_DATE>='2022-11-01'
#     and START_DATE<'2022-12-01'
# )
# group by a.car_id
# having FEE BETWEEN 500000 AND 1999999
# order by FEE DESC,CAR_TYPE ASC,CAR_ID DESC

















# -- 코드를 입력하세요
# SELECT DISTINCT C.car_id, C.car_type, ROUND(C.daily_fee * (1- T.discount_rate * 0.01) * 30,0) AS FEE
# FROM CAR_RENTAL_COMPANY_CAR C
# LEFT OUTER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON H.car_id = C.car_id
# LEFT OUTER JOIN (SELECT CAR_TYPE, DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE = '30일 이상') T ON T.car_type = C.car_type
# WHERE c.car_id not in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where end_date > '2022-11-01' and start_date < '2022-12-01')
# # GROUP BY C.CAR_ID
# HAVING CAR_TYPE IN ('SUV', '세단') AND (500000 <= FEE AND FEE <= 2000000)
# ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC