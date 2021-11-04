def searchAmazon(search, requests, BeautifulSoup):
    print('Gathering Amazon listings...')
    URL_a = 'https://www.amazon.com/s?k=' + search
    # get and search URL_a
    page = driver.get(URL_a)
    # parse this downloaded HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # results = soup.findAll('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
    results = soup.find(class_='s-desktop-width-max s-opposite-dir sg-row')
    listings = results.find_all('div', class_='s-card-container s-overflow-hidden s-include-content-margin s-latency-cf-section s-card-border')

    runs = 0
    # for listing in results:
    for listing in listings:
        if runs >= 1: break
        item_element = listing.find('span', class_='a-size-medium a-color-base a-text-normal')
        item_price = listing.find('span', class_='a-offscreen')
        if None in (item_element, item_price): continue
        print(item_element.text.strip()) #why strip(): remove extraneous characters
        print(item_price.text.strip())
        print()
        print()
        # print(soup.select_one('span.a-size-medium').get_text())
        runs += 1

    # save the price
    amazon_price = item_price.text.strip() # call strip() to remove extraneous characters
    amazon_price = amazon_price.replace('$', '') # then we can do math operation/comparsion
    amazon_price = float(amazon_price)

    # print('price is returned')
    return amazon_price, URL_a
