# MAIN FUNCTION
def myGreengraph(location_1, location_2):

    #Define imports
    from geolocation import geolocate
    from obtain_url import map_at
    from green_count import count_green_in_png
    from green_show import show_green_in_png
    from green_points import location_sequence

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    import inspect


    # Check if input contains only 2 Locations
    if len(inspect.getargspec(myGreengraph)[0]) < 0 & len(inspect.getargspec(myGreengraph)[0]) > 2:
       raise TypeError("The input should contains only 2 Locations")

    # Check if any input is not a "string" type
    if isinstance(location_1, str) != isinstance(location_2, str):
        raise TypeError("Expected Input Locations as Strings!");


    print location_1
    print location_2

    tmp_location_1 = geolocate(location_1)
    tmp_location_2 = geolocate(location_2)

     # Check if the dimensions of the output value of "geolocate" array are 2
    if len(tmp_location_1) < 2 | len(tmp_location_2) < 2:
        raise TypeError("Something wrong happened with the geolocate function!");

    print tmp_location_1
    print tmp_location_2

    with open('greenLocation1.png','w') as green_1:
            green_1.write(show_green_in_png(map_at(*tmp_location_1,zoom=10,satellite=True)))

    with open('greenLocation2.png','w') as green_2:
        green_2.write(show_green_in_png(map_at(*tmp_location_2,zoom=10,satellite=True)))

    plt.plot([count_green_in_png(map_at(*location, zoom=10, satellite=True))
            for location in location_sequence(tmp_location_1,tmp_location_2,10)])

    plt.savefig('myGreengraph.png')

    print("The Greengraph has been created successfully!")


