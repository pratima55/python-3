def bs_to_ad(bs_year):
    ad_year = bs_year - 57
    return ad_year

def ad_to_bs(ad_year):
    bs_year = ad_year + 57
    return bs_year

converted_to_ad = bs_to_ad(2081)
converted_to_bs = ad_to_bs(2024)


print(f"{bs_year} BS is equa; to {converted_to_ad} AD")
print(f"{ad_year} AD is equal to {converted_to_bs} BS.")