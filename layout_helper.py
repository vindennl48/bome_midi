for i in range(3):
    names = 'mitch james jesse'.split()
    if i == 0:
        a = names[0]
        b = names[1]
        c = names[2]
    elif i == 1:
        a = names[1]
        b = names[2]
        c = names[0]
    elif i == 2:
        a = names[2]
        b = names[0]
        c = names[1]

    print("""
    l('hb_{0}_solo', '', [
        'if pp==127 then goto ON',
        'label OFF',
        'daw_{1}_{0}=solo_{1}_{0}',
        'hb_{1}_{0}=solo_{1}_{0}',
        'daw_{2}_{0}=solo_{2}_{0}',
        'hb_{2}_{0}=solo_{2}_{0}',
        'goto EXIT',
        'label ON',
        'solo_{1}_{0}=daw_{1}_{0}',
        'daw_{1}_{0}=0',
        'hb_{1}_{0}=0',
        'solo_{2}_{0}=daw_{2}_{0}',
        'daw_{2}_{0}=0',
        'hb_{2}_{0}=0',
        'label EXIT'])""".format(a,b,c))
