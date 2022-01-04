import ldap

def ldap_connect(username, password):
    result = {}
    username_full = username + "@mbu"
    l = ldap.initialize("ldap://10.0.3.10")
    try:
        l.protocol_version = ldap.VERSION3
        l.set_option(ldap.OPT_REFERRALS, 0)
        l.simple_bind_s(username_full, password)
        base = "dc=mbu, dc=invalid"
        search_filter = "(&(objectClass=user)(sAMAccountName=" + username +"))"
        info = l.search_s(base, ldap.SCOPE_SUBTREE, search_filter)
        result['data'] = info[0][1]['description'][0].decode('utf-8')
        result['boolen'] = True
    except ldap.INVALID_CREDENTIALS:
        result['data'] = 'Invalid Credentials'
        result['boolen'] = False
    except ldap.SERVER_DOWN:
        result['data'] = 'Server down'
        result['boolen'] = False
    except ldap.LDAPError as err:
        if type(err.message) == dict and err.message.has_key('desc'):
            result['data'] = 'Other LDAP error: ' + err.message['desc']
            result['boolen'] = False
        else:
            result['data'] = 'Other LDAP error: ' + err
            result['boolen'] = False
    finally:
        l.unbind()
    print(result)
    return(result)
