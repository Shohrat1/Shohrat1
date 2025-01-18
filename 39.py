# ishgarler={"oraz": {"synag1":85,
#                     "synag2":90,  
#                     "synag3":0}
# }
# ady=input("Ady: ")
# if ady in ishgarler:
#     isleg=input("doly maglumat:(howa/yok)")
#     if isleg =="howa":
#         print(ishgarler[ady])
#     else:
#         mag=input("synag1/synag2/synag3")
#         print(ishgarler[ady][mag])
# else:
#     print(f"{ady}atly ishgar yok")                                        

ishgarler={"merdan": {"synag1":0,
                    "synag2":71,  
                    "synag3":0}
}
ady=input("Ady: ")
if ady in ishgarler:
    isleg=input("doly maglumat:(howa/yok)")
    if isleg =="howa":
        print(ishgarler[ady])
    else:
        mag=input("synag1/synag2/synag3")
        print(ishgarler[ady][mag])
else:
    print(f"{ady}atly ishgar yok")