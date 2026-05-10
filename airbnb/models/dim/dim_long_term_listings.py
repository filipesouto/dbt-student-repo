def model(dbt, session):
    listings = dbt.ref("dim_listings_cleansed")

    return (listings.filter(listings["MINIMUM_NIGHTS"] >= 30)
            .select("LISTINN_ID", "LISTING_NAME", "PRICE"))