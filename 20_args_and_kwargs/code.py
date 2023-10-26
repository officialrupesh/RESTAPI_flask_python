#python *args and **kwargs

# *args kasto vanda jaba hamilai kati ota args aucha tha nahuda use garne vane
#kwargs chai jaba kati ota keyword argument aucha vnane thaha hudina taba use garne


# def random(*u,**kwu):
    # print(u)
    # print(kwu)


# random(1,name =  "Rupesh")



def iterate(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is {value}")

iterate(name="Rupesh", lName = "Raut")