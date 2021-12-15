#!/usr/bin/python3
from pprint import pprint

#############################        BASE VARS     #############################
BASE_USDTRY = 8.64
BASE_USDRUB = 75
PROCENT = 0.185
Kk = 1
KPI = 1

#############################         CURRENCY     #############################
CURRENT_USDRUB = 75.0
CURRENT_USDTRY = 13.5
CURRENT_TRYRUB = 5.1

#############################       USER INPUT     #############################
oklad = 5000
isn = 3439
extra = 1000
targetkpi = 15000

#############################          MAIN        #############################
def income(BASE_USDTRY,
           BASE_USDRUB,
           PROCENT,
           Kk,
           KPI,
           CURRENT_USDRUB,
           CURRENT_USDTRY,
           CURRENT_TRYRUB,
           oklad,
           isn,
           extra,
           targetkpi
        ):
    result = {}
#############################      KOEFFICENTS     #############################
    Rk = round((BASE_USDRUB/CURRENT_USDRUB)*Kk, 4)
    Kv = round((CURRENT_USDTRY/BASE_USDTRY)*Rk, 3)

#############################           EZP        #############################
    indincome = round((oklad + isn)*PROCENT)
    bzp = oklad + isn + indincome
    ezp = round(bzp/BASE_USDTRY)

#############################           ZP         #############################
    zp_extra = round((ezp*CURRENT_USDTRY*Rk) - bzp + extra*Kv - extra)
    zp_TRY = round(zp_extra + bzp + extra)
    zp_RUB = round(zp_TRY*CURRENT_TRYRUB)
    zp_USD = round(zp_TRY/CURRENT_USDTRY)
    result['zp_TRY'] = zp_TRY
    result['zp_RUB'] = zp_RUB
    result['zp_USD'] = zp_USD
    result['Rk'] = Rk
    result['Kv'] = Kv
    result['ezp'] = ezp
    result['indincome'] = indincome
    result['zp_extra'] = zp_extra


#############################         EBONUS       #############################
    indbonus = round(targetkpi*PROCENT)
    ebonus = round((targetkpi + targetkpi*PROCENT)/BASE_USDTRY)

#############################         BONUS        #############################
    bonus_dop = round((ebonus*KPI*CURRENT_USDTRY*Rk) - (targetkpi+indbonus)*KPI)
    bonus_TRY = round(targetkpi + indbonus + bonus_dop)
    bonus_RUB = round(bonus_TRY *CURRENT_TRYRUB)
    bonus_USD = round(bonus_TRY /CURRENT_USDTRY)
    result['bonus_TRY'] = bonus_TRY
    result['bonus_RUB'] = bonus_RUB
    result['bonus_USD'] = bonus_USD
    result['ebonus'] = ebonus
    result['indbonus'] = indbonus
    result['bonus_dop'] = bonus_dop

#############################        RESULT        #############################
    pprint(result)
    return result

i = income(BASE_USDTRY,
           BASE_USDRUB,
           PROCENT,
           Kk,
           KPI,
           CURRENT_USDRUB,
           CURRENT_USDTRY,
           CURRENT_TRYRUB,
           oklad,
           isn,
           extra,
           targetkpi
        )

print(f"\nЗАРПЛАТА\n"
      f"Оклад: {oklad}\n"
      f"ИСН: {isn} TRY\n"
      f"Инд. выплата: {i['indincome']} TRY\n"
      f"Доплата за совмещение: {extra} TRY\n"
      f"Доплата до эквивалента: {i['zp_extra']} TRY\n"
      f"Эквивалент заработной платы: {i['ezp']} У.Е.\n"
      f"Итого к начислению: {i['zp_TRY']} TRY\n"
      f"Итого к начислению: {i['zp_RUB']} RUB\n"
      f"Итого к начислению: {i['zp_USD']} USD\n\n"
      f"ПРЕМИЯ\n"
      f"Эквивалент целевого размера годовой премии: {i['ebonus']} У.Е.\n"
      f"Доплата до эквивалента: {i['bonus_dop']} TRY\n"
      f"Итого к начислению: {i['bonus_TRY']} TRY\n"
      f"Итого к начислению: {i['bonus_RUB']} RUB\n"
      f"Итого к начислению: {i['bonus_USD']} USD\n"
    )

