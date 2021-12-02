import functions as f

runopt = True

while runopt:

    f.main_menu()
    opt = f.user_input()

    if opt == '1':
        f.deg_cel()

    elif opt == '2':
        f.len_met()

    elif opt == '3':
        f.wei_kil()

    elif opt == '4':
        f.vol_lit()

    elif opt == '5':
        f.mph_kph()


    if not f.convert_another():
        break
    else:
        pass
