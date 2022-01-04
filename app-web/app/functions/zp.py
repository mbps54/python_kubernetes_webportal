from functions.documents_functions import round_a


############################## POSSIBLE USER INPUT #############################
"""
data = {}
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
"""


#############################          MAIN        #############################
def zp(data):
    BASE_USDTRY = data["BASE_USDTRY"]
    BASE_USDRUB = data["BASE_USDRUB"]
    PROCENT = data["PROCENT"]
    Kk = data["Kk"]
    KPI = data["KPI"]
    CURRENT_USDRUB = data["CURRENT_USDRUB"]
    CURRENT_USDTRY = data["CURRENT_USDTRY"]
    CURRENT_TRYRUB = data["CURRENT_TRYRUB"]
    oklad = round_a(data['oklad'])
    isn = round_a(data["isn"])
    extra = round_a(data["extra"])
    targetkpi = round_a(data["targetkpi"])
    result = {}
    #############################      KOEFFICENTS     #############################
    Rk = round_a((BASE_USDRUB / CURRENT_USDRUB) * Kk, 4)
    Kv = round_a((CURRENT_USDTRY / BASE_USDTRY) * Rk, 4)

    #############################           EZP        #############################
    indincome = round_a((oklad + isn) * PROCENT)
    bzp = oklad + isn + indincome
    ezp = round_a(bzp / BASE_USDTRY)

    #############################           ZP         #############################
    zp_extra = round_a((ezp * CURRENT_USDTRY * Rk) - bzp)
    if zp_extra < 0:
        zp_extra = 0
    extra_2 = round_a(extra*Kv)
    if extra_2 < extra:
        extra_2 = extra
    zp_TRY = round_a(zp_extra + bzp)
    zp_RUB = round_a(zp_TRY * CURRENT_TRYRUB)
    zp_USD = round_a(zp_TRY / CURRENT_USDTRY)
    result["zp_TRY"] = zp_TRY
    result["zp_RUB"] = zp_RUB
    result["zp_USD"] = zp_USD
    result["Rk"] = Rk
    result["Kv"] = Kv
    result["ezp"] = ezp
    result["indincome"] = indincome
    result["zp_extra"] = zp_extra
    result["extra_2"] = extra_2
    result["Kv"] = Kv
    result["Rk"] = Rk

    #############################         EBONUS       #############################
    indbonus = round_a(targetkpi * PROCENT)
    ebonus = round_a((targetkpi + targetkpi * PROCENT) / BASE_USDTRY)

    #############################         BONUS        #############################
    bonus_dop = round_a(
        (ebonus * KPI * CURRENT_USDTRY * Rk) - (targetkpi + indbonus) * KPI
    )
    if indbonus < 0:
        indbonus = 0
    if bonus_dop < 0:
        bonus_dop = 0
    bonus_TRY = round_a(targetkpi + indbonus + bonus_dop)
    bonus_RUB = round_a(bonus_TRY * CURRENT_TRYRUB)
    bonus_USD = round_a(bonus_TRY / CURRENT_USDTRY)
    result["bonus_TRY"] = bonus_TRY
    result["bonus_RUB"] = bonus_RUB
    result["bonus_USD"] = bonus_USD
    result["ebonus"] = ebonus
    result["indbonus"] = indbonus
    result["bonus_dop"] = bonus_dop
    result["bonus_plus"] = indbonus + bonus_dop

    #############################        RESULT        #############################
    return result