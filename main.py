from booking.booking import Booking

try:
    with Booking() as bot:
        #bot.land_first_page()
        bot.choose_travel_type()
        #bot.change_currency(currency='IQD')
        #bot.select_source('New York')
        #bot.destination_place('Berlin')
        #bot.choosing_dates('Friday September 8, 2023','Sunday October 8, 2023')
        #bot.adults_number(3)
        #bot.click_search()
        #bot.apply_filtrations()
        #print(len(bot.report_results()))
except Exception as e:
    if 'in PATH' in str(e):
        print("You should path chrome driver in your path")
    else:
        raise