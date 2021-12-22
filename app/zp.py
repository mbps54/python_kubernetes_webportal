#!/usr/bin/python3
from pprint import pprint


##############################       USER INPUT     #############################
data = {}
'''
data['BASE_USDTRY'] = 8.64
data['BASE_USDRUB'] = 74.89
data['PROCENT'] = 0.185
data['Kk'] = 1
data['KPI'] = 1

data['CURRENT_USDRUB'] = 74
data['CURRENT_USDTRY'] = 14
data['CURRENT_TRYRUB'] = 5
data['oklad'] = 5000
data['isn'] = 3439
data['extra'] = 1000
data['targetkpi'] = 15000
'''

#############################          MAIN        #############################
def zp(data):
    BASE_USDTRY = data['BASE_USDTRY']
    BASE_USDRUB = data['BASE_USDRUB']
    PROCENT = data['PROCENT']
    Kk = data['Kk']
    KPI = data['KPI']
    CURRENT_USDRUB = data['CURRENT_USDRUB']
    CURRENT_USDTRY = data['CURRENT_USDTRY']
    CURRENT_TRYRUB = data['CURRENT_TRYRUB']
    oklad = data['oklad']
    isn = data['isn']
    extra = data['extra']
    targetkpi = data['targetkpi']
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
    return result
