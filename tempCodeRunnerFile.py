
    page = driver.page_source

    print("I am here 3")
    soup = BeautifulSoup(page,features='html.parser')

# Find the div with the specified class name